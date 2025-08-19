# AI Document Editor

This project is a powerful research paper/document editor that leverages AI models (OpenAI or similar) to edit and enhance DOCX (and optionally PDF/CSV) files, following user-specified instructions and styles. The application is built using Streamlit for the interface and supports advanced editing workflows.

---

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Approach 1: Direct OpenAI API-based Editing](#approach-1-direct-openai-api-based-editing)
  - [Flow](#flow-for-approach-1)
- [Approach 2: CrewAI Agent-based Editing](#approach-2-crewai-agent-based-editing)
  - [Flow](#flow-for-approach-2)
- [Comparison & Recommendations](#comparison--recommendations)
- [Setup & Usage](#setup--usage)
- [License](#license)

---

## Features

- Upload DOCX (and optionally PDF/CSV) files for editing.
- Choose between different editing styles: Standard, Developmental, Proofreading.
- Select additional report features, e.g., research gaps, highlights, title, keywords, cover letter, etc.
- AI-powered rewriting and improving of text using OpenAI models.
- Optionally, measure semantic similarity and word retention ratio between the original and edited documents.
- Download the edited file as a DOCX.

---

## How It Works

The application is implemented in two main approaches:

---

## Approach 1: Direct OpenAI API-based Editing

**Description:**  
This method interacts directly with the OpenAI API. The uploaded document is split into manageable text groups, and each group is sent to the API for editing based on user-selected instructions and style. The process is as follows:

### Flow for Approach 1

<details>
<summary>Click to show ASCII flow</summary>

```
┌───────────────────────────┐
│   User Interface (Streamlit)  
└───────┬───────────────────┘
        │
        │
        ▼
┌───────────────────────────┐
│ User selects edit style   │
│ User uploads .docx file   │
│ User selects features     │
└───────┬───────────────────┘
        │
        │
        ▼
┌─────────────────────────────┐
│ User clicks "Edit Text"     │
└───────┬─────────────────────┘
        │
        ▼
┌───────────────────────────────┐
│ process_document()            │
│ - Read DOCX                   │
│ - Break text into groups      │
│ - Load instructions           │
│ - Combine features & instr.   │
└───────┬───────────────────────┘
        │
        ▼
┌──────────────────────────────────────┐
│ process_text_with_api()              │
│ - For each text group:               │
│   - Send to OpenAI API               │
│   - Post-process response with style │
└───────┬──────────────────────────────┘
        │
        ▼
┌─────────────────────────────┐
│ Aggregate all responses     │
│ Return final edited text    │
└───────┬─────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────┐
│ Show output in Streamlit:                   │
│ - Display response                          │
│ - (If model loaded) Calculate similarity &  │
│   word retention                            │
│ - Download edited DOCX                      │
└─────────────────────────────────────────────┘
```
</details>

---

## Approach 2: CrewAI Agent-based Editing

**Description:**  
This approach uses the CrewAI framework, which allows defining agents, tasks, and crews for more modular and advanced workflows. Each text group is assigned to an AI agent as a "Task," and the CrewAI system manages the editing process.

### Flow for Approach 2

<details>
<summary>Click to show ASCII flow</summary>

```
┌─────────────────────────────┐
│ Streamlit User Interface    │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ User selects:               │
│ - Edit style                │
│ - Uploads DOCX/PDF/CSV      │
│ - Features to include       │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│ On "Edit Text" Button       │
└────────────┬────────────────┘
             ▼
┌──────────────────────────────────────────┐
│ process_document()                       │
│ - Read docx file                         │
│ - Text break (split into groups)         │
│ - Load instructions based on style       │
│ - Collect feature instructions           │
│ - Combine instructions                   │
└────────────┬─────────────────────────────┘
             ▼
┌──────────────────────────────────────────┐
│ process_text_with_api()                  │
│ For each text group:                     │
│   ├─ Create CrewAI LLM Agent             │
│   ├─ Create editing Task                 │
│   ├─ Create Crew, assign task            │
│   ├─ Kick off Crew to edit group         │
│   └─ Collect result into output text     │
└────────────┬─────────────────────────────┘
             ▼
┌─────────────────────────────┐
│ Aggregate edited text groups│
│ to form final output        │
└────────────┬────────────────┘
             ▼
┌──────────────────────────────┐
│ Calculate Similarity & Ratio │
│ - Semantic similarity        │
│ - Word retention             │
└────────────┬─────────────────┘
             ▼
┌──────────────────────────────┐
│ Show output in Streamlit:    │
│ - Display edited text        │
│ - Show similarity, retention │
│ - Download as DOCX           │
└──────────────────────────────┘
```
</details>

---

## Comparison & Recommendations

| Feature                | Approach 1 (Direct) | Approach 2 (CrewAI) |
|------------------------|--------------------|---------------------|
| Simplicity             | ⭐⭐⭐⭐⭐             | ⭐⭐⭐                |
| Flexibility            | ⭐⭐⭐               | ⭐⭐⭐⭐⭐              |
| Multi-step Workflows   | ⭐⭐                | ⭐⭐⭐⭐⭐              |
| Dependencies           | Minimal            | More (CrewAI, etc.) |
| Best for               | Quick edits, MVP   | Advanced, extensible agent-based editing |

- **Choose Approach 1** if you want a quick, straightforward setup with minimal dependencies.
- **Choose Approach 2** for advanced, modular editing with potential for collaborative or multi-step workflows.

---

## Setup & Usage

1. **Clone the repo and install requirements:**  
   Make sure to install all dependencies listed in `requirements.txt` (including `streamlit`, `python-docx`, `openai`, `crewai`, `sentence-transformers`, etc.)

2. **Set your OpenAI API key:**  
   Configure your API key in `.streamlit/secrets.toml`:
   ```
   [api_key]
   api_key = "sk-..."
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

4. **Follow the on-screen instructions to upload your document and select editing options.**

---

## License

This project is licensed under the MIT License.

---

**Enjoy seamless, AI-powered document editing with the flexibility to choose the workflow that best fits your needs!**
