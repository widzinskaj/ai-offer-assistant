# AI Offer Assistant

This repository contains a **public portfolio proof-of-concept** of an AI-powered assistant
that helps sales and technical teams **draft responses to client inquiries faster and more consistently**.

The project is inspired by real-world workflows in the **energy storage (BESS) sector**,
but **uses only synthetic or publicly describable data**.

> **Disclaimer**
> This is a personal portfolio project.
> It does **not** contain any confidential, proprietary, or internal data from any company.
> Real company materials (emails, datasheets, pricing) are **explicitly excluded** from this repository.

---

## Problem

Responding to client emails and preparing initial offer drafts for energy storage systems often:
- takes 30–60 minutes per inquiry,
- requires manually checking product parameters,
- involves translating non-technical client language into technical constraints.

This creates a bottleneck for sales and pre-sales teams.

---

## Solution (MVP Scope)

**AI Offer Assistant** demonstrates how a lightweight AI workflow can:

- interpret a **non-technical client email**,
- retrieve relevant product information from a small knowledge base,
- generate a **structured draft response or offer** (Markdown),
- highlight missing or unclear information.

The goal is **draft acceleration**, not full automation.

---

## What This Demo Does

- Input:  
  - a synthetic client email (plain text, non-technical language),
  - a small set of synthetic/public BESS product descriptions.
- Output:
  - draft response email / offer (Markdown),
  - list of assumptions,
  - checklist of missing client inputs.

---

## What This Demo Does NOT Do

- ❌ No real customer data  
- ❌ No real company products or pricing  
- ❌ No internal sales processes  
- ❌ No production deployment  

---

## Tech Stack (Planned for MVP)

| Layer | Tool |
|------|------|
| LLM | OpenAI / compatible API (configurable) |
| Embeddings | Sentence Transformers (local) |
| Vector DB | Chroma (local folder) |
| Orchestration | Python (simple scripts) |
| UI | CLI or minimal Streamlit demo |
| Output | Markdown files |

---

## Repository Structure

/data – synthetic / public product descriptions
/queries – sample client emails
/prompts – prompt templates
/docs – architecture, risks, business context
/local-demo – local-only demo (excluded from Git)
/scripts – ingestion and demo scripts
/tests – basic validation tests

---

## Roadmap

1. Define MVP scope and documentation ✅  
2. Add synthetic data and prompts  
3. Implement minimal RAG pipeline  
4. Generate draft offer responses  

---

## Author

Joanna Widzińska  
LinkedIn: https://www.linkedin.com/in/joanna-widzi%C5%84ska/

---

### Portfolio Notes

- Public, safe-to-share repository  
- Synthetic data only  
- Focused on **practical business value**, not model complexity  
- Designed as a starting point for company-specific adaptation
