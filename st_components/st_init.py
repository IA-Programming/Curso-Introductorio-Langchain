import streamlit as st
from openai import OpenAI

def password():
    st.markdown('<style>\
                .css-w770g5{width: 100%;}\
                .css-b3z5c9{width: 100%;}\
                .stButton>button{width: 100%;}\
                </style>', unsafe_allow_html=True)
    with st.expander("ℹ️ Coloca aqui tu OpenAI API"):
        st.warning("⚠️ Necesitas colocar tu OpenAI Apikey. puedes conseguirlo [aqui](https://platform.openai.com/account/api-keys).")
        st.subheader('OpenAI API Key')
        def submit():
            
            if not (st.session_state.widget.startswith('sk-') and len(st.session_state.widget)==51):
                st.session_state.widget = ''

        openai_api_key = st.text_input('Enter OpenAI API token:', key='widget', on_change=submit, type="password")
        
        validar=st.button('Validar 🚀', key='Validar')
        if validar and openai_api_key: 
            with st.spinner('🚀 Validando en...'):
                
                try:
                    client = OpenAI(api_key=st.session_state.widget)
                    respuesta = client.chat.completions.create(
                    model="gpt-3.5-turbo-16k",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": "Hello!"}
                    ]
                    )
                    st.session_state['OPENAI_API_KEY']=openai_api_key
                    st.rerun()
                except Exception as e:
                    st.error(e)
                    st.info("⚠️ Por favor revisa tus credenciales y intenta otra vez.")
                    st.warning("⚠️ Si tu no tienes una cuenta, te puedes registrar [here](https://platform.openai.com/account/api-keys).")
                    from time import sleep
                    sleep(3)
                    st.rerun()