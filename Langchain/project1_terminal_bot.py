# 1 Terminal Q&A bot You type a question in the terminal, it answers using a fixed prompt template (e.g. "answer like a senior dev"). No memory, no files — just prompt → LLM → clean text output. Concepts: PromptTemplate, LCEL (prompt | llm | parser), StrOutputParser

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = '''
You are helpful ai assistance. Give short and humble answer to the user. do not think so much .. just give pure and final output
'''

prompt = ChatPromptTemplate([
    ('system',SYSTEM_PROMPT),
    ('human','{user_query}')
])

llm = ChatGroq(model = 'qwen/qwen3.8-27b')

chain = prompt | llm | StrOutputParser()

while True:
    user_query = input('\n[USER]: ')

    if user_query == 'q':
        break

    print('[AI]: ',end=" ",flush=True)

    for i in chain.stream({'user_query':user_query}):
        print(i,end='',flush=True)