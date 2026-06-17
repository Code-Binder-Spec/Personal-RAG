==================================================
 PERSONAL RAG • VECTOR DATABASE • AI RETRIEVAL PROJECTS
==================================================

A collection of Python RAG (Retrieval-Augmented Generation) projects focused on:

- Vector Databases (ChromaDB)
- Semantic Search & Embeddings
- LLM Integration (Groq)
- Conversational Memory
- PDF Text Extraction & Chunking
- Hallucination Defense

Each project in this repository was built to practice real RAG system design through hands-on development instead of only theoretical learning.

==================================================
📂 FOLDER: Root
📦 PROJECT 01 — family_ai.py
==================================================

TYPE:
Conversational Family Knowledge Assistant with Metadata-Based Person Filtering

DESCRIPTION:
A Python-based conversational RAG system that stores personal information about
family members inside a ChromaDB vector collection and answers natural language
questions about them using Groq's LLaMA 3.3 70B model. The system tracks the
"active person" across conversation turns, allowing the user to mention a name
once and continue asking follow-up questions without repeating it. Each person's
data is tagged with metadata for precise filtering, and full conversation history
is maintained for context-aware, continuous dialogue.

MAIN FEATURES:
✔ Persistent vector storage using ChromaDB
✔ Metadata-based filtering per family member
✔ Active-person state tracking across conversation turns
✔ Full conversation history passed to the LLM for context retention
✔ System-level prompt instructions for consistent behavior
✔ Hallucination defense — answers only from stored context
✔ Graceful handling of name-less queries (asks user to clarify)
✔ Environment variable based API key management (.env)
✔ Simple terminal-based chat loop with exit command

DATABASE:
allu.db

LEARNING FOCUS:
- Vector database persistence with ChromaDB
- Metadata tagging and filtered semantic search
- Conversational state management (active entity tracking)
- Multi-turn conversation history with LLMs
- System prompt design for behavior control
- Hallucination defense through strict context grounding
- Secure API key handling with environment variables

==================================================
📂 FOLDER: Root
📦 PROJECT 02 — pdfvault.py
==================================================

TYPE:
PDF Knowledge Vault with Custom Overlap-Based Chunking

DESCRIPTION:
A Python-based RAG system that extracts text from a PDF document, splits it into
fixed-size word chunks with manually implemented overlap, stores the chunks in a
ChromaDB vector collection, and answers user questions using Groq's LLaMA 3.3 70B
model. The chunking algorithm was designed and implemented from scratch to prevent
answers from being lost at chunk boundaries, with each chunk inheriting the last
50 words of the previous chunk for continuity. Multiple relevant chunks are
retrieved per query and combined before being passed to the model, ensuring
answers that span chunk boundaries are still answered correctly.

MAIN FEATURES:
✔ PDF text extraction using pypdf with layout-aware mode
✔ Custom word-count based chunking (200 words per chunk)
✔ Manually implemented chunk overlap (50-word continuity buffer)
✔ Persistent vector storage using ChromaDB
✔ Page-based metadata tagging per chunk
✔ Multi-chunk retrieval (top 3 results) for boundary-spanning answers
✔ Duplicate-aware prompt instructions to avoid repeated information
✔ Hallucination defense — explicitly states when answer isn't in the PDF
✔ Simple terminal-based query loop with exit command

DATABASE:
pdfvault.db

LEARNING FOCUS:
- PDF text extraction and layout handling
- Manual chunking algorithm design (fixed-size with overlap)
- Boundary-loss prevention in document retrieval
- Multi-chunk context combination for the LLM
- Metadata tagging for page-level traceability
- Retrieval count tuning (n_results) for coverage
- Prompt engineering for deduplication and grounded answers

==================================================
🛠 TECHNOLOGIES USED
==================================================

- Python
- ChromaDB
- Groq (LLaMA 3.3 70B)
- pypdf
- python-dotenv
- math
