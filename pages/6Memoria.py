import streamlit as st

st.set_page_config(page_title="Aprendiendo LangChain | Memoria", page_icon="💡")

st.header('💡 Memoria')

st.write('''
Los LLMs son, por defecto, son estaticos, lo que significa que no tienen memoria incorporada. Pero a veces necesitamos memoria para implementar aplicaciones como sistemas conversacionales, que pueden tener que recordar información previa proporcionada por el usuario. Afortunadamente, LangChain proporciona varias soluciones de gestión de memoria, adecuadas para diferentes casos de uso.

Como hemos visto antes, los vector stores se refieren como memoria a largo plazo; en cambio, los métodos que veremos en esta sección se consideran memoria a corto plazo, ya que no persisten una vez que las interacciones están completas.
''')

st.subheader('ConversationBufferMemory')

st.write('''
Esta es la clase de memoria más sencilla y básicamente lo que hace es incluir los mensajes previos en el nuevo mensaje de LLM. Puedes intentar tener una conversación con el chatbot, luego hacer preguntas sobre el mensaje anterior y el LLM podrá responderlas.
''')

st.code('''
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), temperature=0.0)

memory = ConversationBufferMemory()
        
chain = ConversationChain(llm=llm, memory=memory)

chain.predict(input=prompt)
''')

st.subheader('ConversationBufferWindowMemory')

st.write('''
Por supuesto, la conversación puede extenderse y incluir toda la historia del chat en el prompt puede volverse ineficiente en costo, ya que los prompts más largos resultan en un mayor uso de tokens de LLM. Para optimizar este comportamiento, LangChain proporciona otros tres tipos de memoria. La MemoryBufferWindowConversation nos permite decidir cuántos mensajes del historial del chat debe recordar el sistema, utilizando un parámetro simple:
''')

st.code('''
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), temperature=0.0)

# 2 es el numero de mensajes almacenados en la memoria
memory = ConversationBufferWindowMemory(k=2)
        
chain = ConversationChain(llm=llm, memory=memory)

chain.predict(input=prompt)
''')

st.subheader('ConversationTokenBufferMemory')

st.write('''
Muy similar a la memoria anterior, el tipo ConversationTokenBufferMemory nos permite ser más específicos sobre la cantidad de tokens que queremos usar en nuestros prompts, y contiene el contenido almacenado para cumplir con ese límite. Debemos pasar el LLM como parámetro, para calcular el número de tokens.
''')

st.code('''
from langchain.chains import ConversationChain
from langchain.memory import ConversationTokenBufferMemory

llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), temperature=0.0)

# limitamos a 50 tokens
memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=50)
''')

st.subheader('ConversationSummaryMemory')

st.write('''
Finalmente, si no queremos cortar arbitrariamente la memoria basándonos en una longitud fija, podemos usar la ConversationSummaryMemory, que aún nos permite definir un límite de tokens, pero pasa como memoria un resumen de las interacciones anteriores. De esta manera, aún podemos mantener bajo control la memoria a corto plazo mientras retenemos la información más importante.
''')

st.code('''
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory

llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), temperature=0.0)

# limitado a 100 tokens and almacenado un resumen
memory = ConversationSummaryMemory(llm=llm, max_token_limit=100)
''')

st.info("Para nuestro proyecto final, utilizaremos la ConversationChain, otra cadena integrada de LangChain. Con el cual podremos elegir el tipo de memoria y comprender el uso de la memoria inspeccionar la memoria usando el metodo `dump`.", icon="ℹ️")

st.subheader('Referencias: ')

st.markdown('''
- [Conversation Buffer](https://python.langchain.com/docs/modules/memory/types/buffer)
- [Conversation Buffer Window](https://python.langchain.com/docs/modules/memory/types/buffer_window)
- [Conversation Token Buffer](https://python.langchain.com/docs/modules/memory/types/token_buffer)           
- [Conversation Summary](https://python.langchain.com/docs/modules/memory/types/summary)
''')

st.divider()

st.write('Un proyecto hecho por [BlazzByte](https://www.buymeacoffee.com/blazzmocompany) - \
Necesitas IA aprendizaje / Consulta? [Hablanos aqui](mailto:blazzmo.company@gmail.com)')
