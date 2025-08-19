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

1. **User selects edit style, uploads DOCX, and chooses features.**
2. **On 'Edit Text' button click:**
   - Read the DOCX file and extract text.
   - Split text into smaller groups for processing.
   - Load the corresponding editing instructions and combine with feature prompts.
   - For each group:
     - Send the text and instructions to the OpenAI API.
     - (For "Developmental" style, apply further processing.)
     - Aggregate all responses into the final edited text.
3. **Display Results:**
   - Show the edited text in the app.
   - If enabled, compute and display semantic similarity and word retention ratio.
   - Provide a download button for the edited DOCX.

**Advantages:**  
- Simple and straightforward.
- Fewer dependencies.

**Disadvantages:**  
- Less modular; harder to scale for multi-agent or multi-step workflows.

---

## Approach 2: CrewAI Agent-based Editing

**Description:**  
This approach uses the CrewAI framework, which allows defining agents, tasks, and crews for more modular and advanced workflows. Each text group is assigned to an AI agent as a "Task," and the CrewAI system manages the editing process.

### Flow for Approach 2

1. **User selects edit style, uploads DOCX/PDF/CSV, and chooses features.**
2. **On 'Edit Text' button click:**
   - Read and extract the document text.
   - Split text into manageable groups.
   - Load editing instructions and combine with selected feature prompts.
   - For each group:
     - Create a dedicated CrewAI agent with the desired role and context.
     - Assign an editing task to the agent.
     - Launch a Crew (a managed set of agents/tasks) to process the group.
     - Collect the agent's output.
   - Aggregate all group outputs into the final edited text.
3. **Display Results:**
   - Show the edited text in the app.
   - Compute and display semantic similarity and word retention ratio.
   - Provide a download button for the edited DOCX.

**Advantages:**  
- Highly modular, enabling future expansion (e.g., multi-agent collaboration, complex workflows).
- Clear separation of roles and tasks.
- Easier integration with other CrewAI-based features.

**Disadvantages:**  
- More dependencies and setup required.
- Slightly more complex codebase.

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
