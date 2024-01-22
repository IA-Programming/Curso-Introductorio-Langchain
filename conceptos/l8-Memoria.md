# Lección 8: Memoria

## Definition:

Estos elementos de memoria son utilizados en Langchain para almacenar y acceder a información de interacciones pasadas en una conversación, lo que permite a los sistemas conversacionales recordar y utilizar información previa durante la generación de respuestas.

## ConversationBufferMemory:

`ConversationBufferMemory` es una clase en Langchain que permite almacenar y gestionar el historial de conversaciones en un modelo de chat. Puede almacenar mensajes de entrada y salida en una variable de historial, ya sea como una cadena de texto o como una lista de mensajes. Esto es útil para mantener un registro de las interacciones anteriores en una conversación y utilizarlo como contexto para generar respuestas más coherentes y relevantes. También se puede utilizar en una cadena de conversación para mantener un seguimiento del historial durante una sesión de chat.

## ConversationBufferWindowMemory:

`ConversationBufferWindowMemory` es una clase en Langchain que se utiliza para almacenar y gestionar la memoria de conversaciones en una ventana deslizante. Esta memoria mantiene una lista de las interacciones más recientes en una conversación y solo utiliza las últimas K interacciones. Esto es útil para mantener un historial de interacciones recientes sin que la memoria se vuelva demasiado grande. Puede almacenar y cargar contextos de conversación, y también puede obtener el historial como una lista de mensajes. 0

## ConversationTokenBufferMemory:

`ConversationTokenBufferMemory` es una clase en Langchain que se utiliza para almacenar y gestionar el historial de interacciones en una conversación. Permite guardar el contexto de una conversación, incluyendo los mensajes de entrada y salida, en un búfer de memoria. Esta memoria se utiliza en cadenas de conversación para mantener un registro de las interacciones anteriores y utilizarlo como contexto para generar respuestas más coherentes y relevantes. También proporciona métodos para cargar y guardar el historial de la conversación.

## ConversationSummaryMemory:

`ConversationSummaryMemory` es un tipo de memoria en Langchain que crea un resumen de la conversación a medida que ocurre. Esta memoria es útil para condensar la información de la conversación a lo largo del tiempo, especialmente en conversaciones más largas donde mantener el historial completo de mensajes ocuparía demasiados tokens. Permite almacenar el resumen actual de la conversación en memoria y utilizarlo para inyectar el resumen de la conversación hasta el momento en una cadena de texto. También se puede utilizar el método `predict_new_summary` para obtener directamente un nuevo resumen de la conversación.

## Ejemplos:

Consulta el [notebook](./lab/l8-memoria.ipynb) para ver más ejemplos de código.

## Referencias

Curso principal:
- https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/5/inferring

Langchain Documentation:
- https://huggingface.co/blog/sagemaker-huggingface-llm
- https://python.langchain.com/docs/modules/memory/types/buffer_window
- https://python.langchain.com/docs/modules/memory/types/token_buffer
- https://python.langchain.com/docs/modules/memory/types/summary