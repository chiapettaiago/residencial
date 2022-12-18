import mysql.connector 
import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

conector = mysql.connector.connect(
    host='starkserver.ddns.net',
    user="chiapettaiago",
    password='eduardaamor15',
    database='dados_domesticos'
)

cursor = conector.cursor()

#Códigos do Streamlit
st.title("Neverland")
st.sidebar.title("Opções")
financeiro = st.sidebar.selectbox("Financeiro", ["Selecionar...", "Dívidas", "Entradas"])
if financeiro == "Dívidas":
    st.header("Relação de Dívidas")
    comando_read = f'SELECT * FROM dbdividas WHERE SIT = 0'
    cursor.execute(comando_read)
    resultado = cursor.fetchall()
    st.dataframe(resultado, width=500)

    st.subheader("Total das Dívidas")
    comando_read_soma = f'SELECT SUM(VALOR) FROM dbdividas'
    cursor.execute(comando_read_soma)
    resultadosoma = cursor.fetchall()
    st.table(resultadosoma)

    st.header("Inserir nova Dívida")
    col1, col2 = st.columns(2)
    with col1:
        nome_dividas = st.text_input("Insira aqui a Identificação da dívida")
        venc_dividas = st.date_input("Data de vencimento da dívida")
    with col2:    
        valor_dividas = st.number_input("Valor da Divida")
        situacao_divida = st.text_input("Paga ou Não Paga")
    if st.button("Inserir"):
        comando_create = f'INSERT INTO dbdividas (NOME, VENC, VALOR, SIT) VALUES ("{nome_dividas}", "{venc_dividas}", {valor_dividas}, {situacao_divida}) '
        cursor.execute(comando_create)
        conector.commit()


#CRUD
#comando_create = f'INSERT INTO dbdividas (NOME, VENC, VALOR, SIT) VALUES ("Aluguel", "2021-10-01", 680, TRUE) '
#cursor.execute(comando_create)
#conector.commit()


cursor.close()
conector.close()