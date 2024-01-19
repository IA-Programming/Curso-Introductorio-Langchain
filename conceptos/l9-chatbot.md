# Lección 9: Chatbot

## Detallamiento: 

Los chatbots son uno de los casos de uso centrales de LLM. Las características principales de los chatbots son que pueden tener conversaciones prolongadas y tener acceso a la información que los usuarios quieren saber.

Aparte de los prompts básicos y los LLM, la memoria y la recuperación son componentes clave de un chatbot. La memoria permite que un chatbot recuerde interacciones pasadas, y la recuperación proporciona al chatbot información actualizada y específica del dominio.

La interfaz del modelo de chat se basa en mensajes en lugar de texto sin procesar. Varios componentes son importantes considerar para el chat:

- `modelo de chat`: Consulta [aquí](https://python.langchain.com/docs/integrations/chat) para ver una lista de integraciones de modelos de chat y [aquí](https://python.langchain.com/docs/modules/model_io/chat) para obtener documentación sobre la interfaz del modelo de chat en LangChain. También se pueden utilizar `LLMs` (ver [aquí](https://python.langchain.com/docs/modules/model_io/llms)) para chatbots, pero los modelos de chat tienen un tono más conversacional y admiten nativamente una interfaz de mensaje.

- `prompt template`: Las plantillas de prompts facilitan el ensamblaje de prompts que combinan mensajes predeterminados, entrada del usuario, historial de chat y (opcionalmente) contexto recuperado adicional.

- `memoria`: Consulta [aquí](https://python.langchain.com/docs/modules/memory/) para obtener documentación detallada sobre los tipos de memoria.

- `retriever`(opcional): Consulta [aquí](https://python.langchain.com/docs/modules/data_connection/retrievers) para obtener documentación detallada sobre los sistemas de recuperación. Estos son útiles si deseas construir un chatbot con conocimientos específicos del dominio.
 

- Consulta el [notebook](./lab/l9-chatbot.ipynb) para ver la implementación completa.


## Referencias

Curso principal:
- https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/8/chatbot

Langchain Fuentes:
- https://python.langchain.com/docs/use_cases/chatbots

Streamlit Fuentes:
- https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps


