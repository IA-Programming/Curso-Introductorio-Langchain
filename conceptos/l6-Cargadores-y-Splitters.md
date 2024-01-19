# Lección 6: Cargadores de Documentos y Splitters

## Cargadores de Documentos

### Resumen:

Los Document Loaders de Langchain son herramientas que se utilizan para cargar datos de diferentes fuentes en forma de documentos. Un documento es un fragmento de texto con metadatos asociados. Estos loaders permiten cargar datos desde una variedad de fuentes, como archivos de texto, páginas web, videos de YouTube, transcripciones de videos, entre otros. Los Document Loaders proporcionan un método de carga para obtener los datos como documentos desde la fuente configurada

### Casos de Uso:

Los Document Loaders de Langchain tienen una amplia gama de casos de uso. Algunos ejemplos incluyen:

• Cargar archivos de texto: Los Document Loaders pueden cargar archivos de texto simples, como archivos .txt, y convertirlos en documentos para su procesamiento posterior.
• Cargar contenido web: Puedes utilizar los Document Loaders para cargar el contenido de cualquier página web y convertirlo en documentos para su análisis o extracción de información.
• Cargar transcripciones de videos: Si tienes transcripciones de videos, los Document Loaders pueden cargarlas y convertirlas en documentos para su posterior procesamiento o análisis.
• Cargar datos de bases de datos: Los Document Loaders pueden cargar datos de bases de datos, como archivos CSV o consultas de BigQuery, y convertirlos en documentos para su análisis o manipulación.
• Cargar datos de servicios en la nube: Puedes utilizar los Document Loaders para cargar datos de servicios en la nube, como Azure Blob Storage o Dropbox, y convertirlos en documentos para su procesamiento.

Estos son solo algunos ejemplos de casos de uso para los Document Loaders de Langchain. Su flexibilidad y capacidad para cargar datos de diversas fuentes los convierten en una herramienta versátil para el procesamiento de datos.

## Splitters

### Resumen:

- Los Splitters de Langchain son herramientas que permiten dividir el texto en fragmentos más pequeños para adaptarlo a las necesidades de una aplicación.

### Casos de uso:

Los Splitters de Langchain tienen varios casos de uso en los que pueden ser útiles:

• Preparación de datos para modelos de lenguaje: Los Splitters permiten dividir documentos largos en fragmentos más pequeños que se ajusten al tamaño de ventana de contexto de un modelo de lenguaje. Esto es especialmente útil cuando se trabaja con modelos de lenguaje basados en Transformer.

• Procesamiento de texto estructurado: Los Splitters de HTML y Markdown son útiles para dividir documentos que contienen etiquetas y estructuras específicas de estos formatos. Esto permite trabajar con fragmentos de texto que conservan la estructura original.

• Análisis de código fuente: El Splitter de código es útil para dividir el código fuente en fragmentos más manejables. Esto puede ser útil para realizar análisis de código, extracción de características o cualquier tarea relacionada con el procesamiento de código.

• Conteo de tokens: Los Splitters de tokens, como el Splitters de tiktoken, son útiles para contar el número de tokens en un texto. Esto es importante para asegurarse de que el texto no exceda el límite de tokens permitido por un modelo de lenguaje.


Estos son solo algunos ejemplos de casos de uso de los Splitters de Langchain. Su versatilidad y capacidad de personalización los hacen útiles en una amplia gama de aplicaciones de procesamiento de texto.

### Ejemplos de Uso:

Aquí tienes algunos ejemplos de cómo usar los Splitters de Langchain con código:

- Ejemplo de uso del Splitter de Python:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

PYTHON_CODE = """
def hello_world():
    print("Hello, World!")

# Call the function
hello_world()
"""

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)
python_docs = python_splitter.create_documents([PYTHON_CODE])
print(python_docs)
```

- Ejemplo de uso del Splitter de JavaScript:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

JS_CODE = """
function helloWorld() {
  console.log("Hello, World!");
}

// Call the function
helloWorld();
"""

js_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.JS, chunk_size=60, chunk_overlap=0
)
js_docs = js_splitter.create_documents([JS_CODE])
print(js_docs)
```

- Ejemplo de uso del Splitter de Markdown:

```python

from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

markdown_text = """
# 🦜️🔗 LangChain

⚡ Building applications with LLMs through composability ⚡

## Quick Install

```bash
# Hopefully this code block isn't split
pip install langchain
```\
As an open-source project in a rapidly developing field, we are extremely open to contributions.
"""
md_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN, chunk_size=60, chunk_overlap=0
)
md_docs = md_splitter.create_documents([markdown_text])
print(md_docs)
```

Estos ejemplos muestran cómo utilizar los Splitters de Langchain para dividir el código en fragmentos más pequeños según el lenguaje de programación o el formato del texto. Cada ejemplo utiliza el Splitter correspondiente al lenguaje o formato específico.

## Cuaderno y Código

Consulta el [cuaderno](./lab/l6-cargador-de-documentos-y-splitters.ipynb) para ver los ejemplos de cada una de esas tareas mencionadas anteriormente.

## Referencias

Curso Principal:
- [https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/6/transforming](https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/6/transforming)

Langchain Documentation:

- [Chat Over Documents with Vectara](https://python.langchain.com/docs/integrations/providers/vectara/vectara_chat)
