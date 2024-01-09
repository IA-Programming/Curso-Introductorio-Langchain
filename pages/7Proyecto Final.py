import streamlit as st

st.set_page_config(page_title="Aprendiendo LangChain | OpenAI Chatbot", page_icon="🤖")

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory, ConversationTokenBufferMemory, ConversationSummaryMemory, StreamlitChatMessageHistory

st.title('Proyecto Final: OpenAI Chatbot')

from st_components.st_init import password

if 'OPENAI_API_KEY' not in st.session_state:
    password()
    
else:
    st.success('Exitosamente colocado tu api key', icon='🎉')

# Optionally, specify your own session_state key for storing messages
msgs = StreamlitChatMessageHistory()

memory_type = st.selectbox(
    'Tipo de Memoria',
    ('ConversationBufferMemory', 'ConversationBufferWindowMemory', 'ConversationTokenBufferMemory', 'ConversationSummaryMemory')
)

# Display previous chat messages from history
avatars = {"human": "user", "ai": "assistant"}
for msg in msgs.messages:
    st.chat_message(avatars[msg.type]).markdown(msg.content)

prompt = st.chat_input("Hey, how can I help you today?", disabled=True if 'OPENAI_API_KEY' not in st.session_state else False)

if prompt:

    if "memory_type" in st.session_state and st.session_state.memory_type != memory_type:

        del st.session_state.conversation

    if "conversation" not in st.session_state:

        llm = ChatOpenAI(api_key=st.session_state.get('OPENAI_API_KEY'), temperature=0.0)

        if memory_type == "ConversationBufferWindowMemory":

            memory = ConversationBufferWindowMemory(chat_memory=msgs, k=2)

        elif memory_type == "ConversationTokenBufferMemory":

            # limit to 50 tokens
            memory = ConversationTokenBufferMemory(chat_memory=msgs, llm=llm, max_token_limit=50)

        elif memory_type == "ConversationSummaryMemory":

            memory = ConversationSummaryMemory(llm=llm, chat_memory=msgs)

        else:

            memory = ConversationBufferMemory(chat_memory=msgs)
            
        
        chain = ConversationChain(llm=llm, memory=memory)
        
        st.session_state.conversation = chain

        st.session_state.memory = memory

        st.session_state.memory_type = memory_type

    st.chat_message(name='user').write(prompt)
    
    response = st.session_state.conversation.predict(input=prompt)

    st.chat_message(name='assistant').write(response)

    st.json(st.session_state.memory.load_memory_variables({}))