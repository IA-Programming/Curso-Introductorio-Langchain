# Lección 5: Cadenas

## Resumen

Una Chain en Langchain se refiere a una secuencia estructurada de llamadas a componentes, como modelos de lenguaje o herramientas de procesamiento de datos. Las Chains en Langchain permiten encadenar varios componentes juntos para construir aplicaciones más complejas. 

## Langchain analisis

Hay dos enfoques principales para crear Chains en Langchain:

• **Enfoque heredado**: Utiliza la interfaz Chain para construir Chains personalizadas. Esta interfaz permite llamar a los componentes en secuencia y puede ser utilizada en combinación con el LangChain Expression Language (LCEL) para una mayor flexibilidad y funcionalidad.

• **Enfoque LCEL**: Utiliza el LangChain Expression Language (LCEL) para componer Chains de manera intuitiva y legible. LCEL proporciona soporte de primera clase para funciones como streaming, llamadas asíncronas, agrupamiento, paralelización, reintentos y más.


Langchain ofrece una variedad de Chains incorporadas y herramientas para diferentes casos de uso, como interactuar con APIs, recuperación conversacional, combinación de documentos, consultas a bases de datos y más. Estas Chains se pueden combinar y personalizar según las necesidades de la aplicación.

### Casos de uso
Algunos casos de uso de las Chains en Langchain son:

• Construir cadenas de llamadas a modelos de lenguaje para realizar tareas como responder preguntas o generar texto.
• Tener conversaciones con documentos utilizando una cadena de recuperación conversacional.
• Formatear y reducir documentos para que se ajusten a la ventana de contexto de un modelo de lenguaje.
• Rerankear documentos basados en la confianza de las respuestas de un modelo de lenguaje utilizando la cadena MapRerankDocumentsChain.

Estos son solo algunos ejemplos de los casos de uso de las Chains en Langchain. Las Chains ofrecen flexibilidad y modularidad para construir aplicaciones basadas en modelos de lenguaje y herramientas de procesamiento de lenguaje natural.

Consulta el [notebook](./lab/l5-cadenas.ipynb) para ver más ejemplos de código.

## Referencias

Curso principal:
- https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/5/inferring

Presentación del Contenedor de Inferencia LLM de Hugging Face para Amazon SageMaker:
- https://huggingface.co/blog/sagemaker-huggingface-llm