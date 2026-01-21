import os
from pathlib import Path

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


def log(msg: str):
    print(f"[rag_search] {msg}", flush=True)


def load_query_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("Query email is empty")
    return text


def main():
    base_dir = Path(__file__).resolve().parent.parent

    query_path = base_dir / "queries" / "client_email_01.txt"
    persist_dir = os.getenv("CHROMA_PERSIST_DIR", "chroma_db")
    collection_name = os.getenv("CHROMA_COLLECTION", "bess_public")
    model_name = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2",
    )

    log(f"Loading customer email from: {query_path}")
    query_text = load_query_text(query_path)

    log("Loading embedding model...")
    embedder = SentenceTransformer(model_name)

    log("Connecting to Chroma...")
    client = chromadb.PersistentClient(
        path=persist_dir,
        settings=Settings(anonymized_telemetry=False),
    )

    collection = client.get_collection(collection_name)

    log("Computing query embedding...")
    query_embedding = embedder.encode([query_text])[0]

    log("Running semantic search (top_k=3)...")
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3,
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    # ---- FILTERING ----
    MIN_CHARS = 200
    filtered = []
    seen_docs = set()

    for doc, meta in zip(documents, metadatas):
        if len(doc.strip()) < MIN_CHARS:
            continue

        doc_id = meta.get("doc_id")
        if doc_id in seen_docs:
            continue

        seen_docs.add(doc_id)
        filtered.append((doc, meta))

    print("\n=== TOP MATCHING PRODUCT DOCUMENTATION (FILTERED) ===\n")

    for i, (doc, meta) in enumerate(filtered, start=1):
        print(f"--- Match #{i} ---")
        print(f"Source: {meta.get('source_path')}")
        print(doc[:600])
        print()

    print("=== END ===\n")


if __name__ == "__main__":
    main()
