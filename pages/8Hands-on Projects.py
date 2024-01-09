import streamlit as st

st.set_page_config(page_title="Aprendiendo LangChain | Hands-on Projects", page_icon="🙌")

st.header('🙌 Hands-on Projects')

st.write('''
¡No hay mejor forma de aprender un nuevo lenguaje o marco de trabajo que poniéndote manos a la obra y construyendo tus propias herramientas utilizando LangChain e Inteligencia Artificial! La teoría nunca es suficiente, necesitas enfrentarte a casos de uso reales, escribir código, atascarte y encontrar soluciones. En esta sección encontrarás algunos proyectos de demostración seleccionados específicamente para este curso, que se asemejan a escenarios que pueden resultar útiles para muchas empresas, ¡o que se pueden ampliar para crear herramientas interesantes!

¡Todos los proyectos son de código abierto y encontrarás un enlace al código en GitHub!
''')

st.info('¡Esta sección se actualizará periódicamente con nuevos proyectos! ¡Sígueme en [Blazzmo Company](https://www.buymeacoffee.com/blazzmocompany) para recibir notificaciones!', icon="🆕")

st.subheader('Demo Project #1 | Invoice Data Extractor')

st.write('https://invoice-data-extractor.streamlit.app/')

st.write('''
¡El procesamiento manual de facturas pertenece al pasado! Simplemente suelta una factura en esta aplicación y obtén los datos extraídos y formateados como JSON.
''')

st.divider()

st.subheader('Demo Project #2 | Basic QA Over Custom Data')

st.write('https://langchain-basic-qna.streamlit.app/')

st.write('''
Las IAs conocen mucha información, pero no tienen acceso a nuestros archivos privados, conversaciones por correo electrónico, chats, documentos de trabajo, etc. En esta demostración veremos cómo construir un sistema que puede "aprender" e interactuar con nuestros datos personalizados.
''')

st.divider()

st.subheader('Demo Project #3 | Summarization and Useful Chain Types')

st.write('https://langchain-summarization.streamlit.app/')

st.write('''
Veamos cómo podemos resumir fácilmente el contenido web utilizando una cadena específica para ese propósito, y cómo podemos aprovechar diferentes tipos de cadenas para producir resultados diversos y sortear los límites de tokens de LLM.
''')

st.divider()

st.subheader('Demo Project #4 | WordPress Code Assistant')

st.write('https://wordpress-code-assistant.streamlit.app/')

st.write('''
Con esta demostración comenzamos a ir más allá de los tutoriales "hechos para aprender", creando una herramienta que realmente puede ayudar a los desarrolladores de WordPress en la rutina diaria de trabajo: un asistente de codificación de WordPress que puede escribir código, explicarlo e incluso verificar sus propias soluciones.
''')

st.divider()

st.subheader('Demo Project #5 | Convert Voice Memos to Text')

st.write('https://langchain-audio-to-text.streamlit.app/')

st.write('''
Pasemos al procesamiento de texto y divirtámonos transcribiendo automáticamente notas de audio, y post-procesándolas para producir resúmenes, cambiar el tono o combinarlas en documentos específicos para determinados objetivos.
''')

st.divider()

st.write('Un proyecto hecho por [BlazzByte](https://www.buymeacoffee.com/blazzmocompany) - \
Necesitas IA aprendizaje / Consulta? [Hablanos aqui](mailto:blazzmo.company@gmail.com)')