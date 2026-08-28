from langchain_groq import ChatGroq
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate([
    ('system','You are helpful ai assistance. give short answer'),
    MessagesPlaceholder(variable_name='history'),
    ('human','{input}')
])

llm = ChatGroq(model = 'qwen/qwen3.8-27b')

chain = prompt | llm | StrOutputParser()

store = {}

def get_session_id(session_id:str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]


main_chain = RunnableWithMessageHistory(
    chain,
    get_session_history=get_session_id,
    input_messages_key='input',
    history_messages_key='history',
)

session_id = input('\n[SESSION ID]: ')
config = {'configurable':{'session_id': session_id}}
while True:
    user_query = input('\n[USER]: ')

    if user_query == 'q':
        break

    print('[AI]: ',end=" ",flush=True)

    for i in main_chain.stream({'input':user_query},config=config):
        print(i,end='',flush=True)

print(store)