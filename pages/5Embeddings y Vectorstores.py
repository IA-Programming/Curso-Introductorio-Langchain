import streamlit as st
from langchain_openai import OpenAIEmbeddings

st.set_page_config(page_title="Aprendiendo LangChain | Embeddings and Vector Stores", page_icon="📈")

st.header('📈 Embeddings and Vector Stores')

from st_components.st_init import password, markdownsettings

if 'OPENAI_API_KEY' not in st.session_state:
    markdownsettings()
    password()
    
else:
    markdownsettings()
    st.success('Exitosamente colocado tu api key', icon='🎉')

st.write('''
Los embeddings no son un concepto que pertenezca a LangChain, pero son un elemento muy importante en el ecosistema de inteligencia artificial y específicamente en el procesamiento del lenguaje natural. Cada pieza de contenido debe ser convertida en un embedding para ser "entendida y procesada" por un LLM. Incluso cuando se utiliza la interfaz de ChatGPT, las entradas se convierten (en segundo plano) en embeddings antes de ser procesadas. Podemos pensar en los embeddings como una representación numérica/vectorial del contenido.
         
Como de costumbre, hagámoslo práctico con un ejemplo:
''')

st.code('''
import os
from langchain_openai import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'))

response = embeddings_model.embed_query(text)
''')

with st.form("embedding"):

    text = st.text_input("Insertar texto a ser convertido en embedding")

    execute = st.form_submit_button("🚀 Ejecutar")

    if execute and text and 'OPENAI_API_KEY' in st.session_state:

        embeddings_model = OpenAIEmbeddings(api_key=st.session_state.get('OPENAI_API_KEY'))

        response = embeddings_model.embed_query(text)

        st.json(response)
    elif execute and 'OPENAI_API_KEY' not in st.session_state:
        st.warning('⚠️ Necesitas colocar tu OpenAI Apikey arriba en el principio de la pagina')

st.write('''
En el ejemplo anterior, convertimos una sola pieza de texto en un embedding, pero recuerda que los LLM pueden interactuar con casi cualquier tipo de contenido, siempre y cuando podamos convertirlo en un embedding. Podemos trabajar con imágenes, videos, PDFs e incluso con formatos propietarios de terceros.
''')

st.markdown('## Referencias')

st.markdown('''
- [Text embedding models](https://python.langchain.com/docs/integrations/text_embedding)
- [OpenAI Embeddings](https://python.langchain.com/docs/integrations/text_embedding/openai)
''')

st.subheader('Vector stores')

st.write('''
Otro concepto muy importante en LangChain es el vector store. Así como los embeddings son representaciones vectoriales de datos, los vector stores son formas de almacenar embeddings e interactuar con ellos ejecutando consultas y operaciones. Los vector stores pueden ser bases de datos (como por ejemplo: Pinecone, Vectara) o simplemente índices en memoria (como por ejemplo: DocArrayInMemorySearch). Las bases de datos vectoriales a menudo se denominan "memoria a largo plazo" para la inteligencia artificial, porque por supuesto, los datos almacenados son persistentes.
''')

st.write('''
En la sección "Hands-on Projects", veremos algunas aplicaciones de muestra que hacen un buen uso de embeddings, cargadores de documentos y vector stores.
''')

st.divider()

st.write('Un proyecto hecho por [BlazzByte](https://www.buymeacoffee.com/blazzmocompany) - \
Necesitas IA aprendizaje / Consulta? [Hablanos aqui](mailto:blazzmo.company@gmail.com)')