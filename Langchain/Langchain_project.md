# Langchain Project

1. Terminal Q&A bot You type a question in the terminal, it answers using a fixed prompt template (e.g. "answer like a senior dev"). No memory, no files — just prompt → LLM → clean text output. Concepts: PromptTemplate, LCEL (prompt | llm | parser), StrOutputParser

2. Multi-turn CLI chat Same as #1 but now it remembers earlier messages in the same session — you can say "explain that again simpler" and it knows what "that" means. Concepts: RunnableWithMessageHistory, ChatMessageHistory, session/thread IDs

3. Meeting-notes / lecture-notes summarizer Feed it a .txt or .pdf of your class notes; it splits the file into chunks and produces a clean summary, even for files too long to fit in one prompt. Concepts: Document loaders (TextLoader/PyPDFLoader), RecursiveCharacterTextSplitter, map-reduce summarize chain

4. "Ask my notes" RAG app Dump a folder of your own notes/PDFs in; ask it questions in plain English and it retrieves the relevant chunks and answers from your material, not general knowledge. Concepts: Embeddings, Chroma/FAISS vectorstore, retriever, RAG chain (LCEL or RetrievalQA)

5. Resume / support-ticket classifier Give it a raw ticket or resume text; it returns a strict JSON object (category, priority, tags) instead of free-text — validated against a schema you define. Concepts: Pydantic output schema, .with_structured_output() / PydanticOutputParser, few-shot examples

6. Code-explainer with function calling You paste a filename or a math expression; the LLM decides to call a real Python tool (e.g. "read this file" or "compute this") instead of guessing the answer itself. Concepts: Tool definition, .bind_tools(), tool-calling LLM, parsing tool_calls

7. Web research assistant Ask "what's the latest on X" — it searches the web itself (via a search tool), reads results, and loops until it has enough to answer. Your first real autonomous agent. Concepts: Prebuilt ReAct agent (create_react_agent), search tool (Tavily/DuckDuckGo), AgentExecutor

8. Support-ticket router Incoming ticket text gets automatically routed to a different prompt/chain depending on its type (billing vs technical vs general) — one input, different code paths. Concepts: RunnableBranch / routing chains, sequential chains, conditional prompting

9. Streaming chatbot with token tracking Same chat as #2, but responses now stream token-by-token like ChatGPT's UI, and every response logs how many tokens/cost it used. Concepts: .stream(), custom BaseCallbackHandler, token/cost logging

10. Capstone: Personal Knowledge Assistant One app that combines everything above: load your notes, chat with memory, retrieve relevant chunks, call tools when needed, and return structured answers when asked for structured data. Concepts: All of 1–9 combined