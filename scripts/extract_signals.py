import json
from pathlib import Path
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3:8b"


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def render_prompt(template: str, email_text: str) -> str:
    return template.replace("{{customer_email}}", email_text)


def extract_signals(email_text: str, prompt_template: str) -> dict:
    prompt = render_prompt(prompt_template, email_text)

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=180)
    response.raise_for_status()

    raw = response.json()["response"]
    return json.loads(raw)


def main():
    base_dir = Path(__file__).resolve().parent.parent

    email_path = base_dir / "queries" / "client_email_01.txt"
    prompt_path = base_dir / "prompts" / "extract_signals_prompt.md"

    email_text = load_text(email_path)
    prompt_template = load_text(prompt_path)

    signals = extract_signals(email_text, prompt_template)

    print("\n=== EXTRACTED SIGNALS ===\n")
    print(json.dumps(signals, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
