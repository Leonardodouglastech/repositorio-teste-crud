import streamlit as st

from funcoesCrud import cadastrar

#cadastro
st.title('Sistema Dieguinho Alimentos - ME')

col1, col2 = st.columns(2)
containerCadastrar = st.container(border=True)
containerCadastrar.markdown('## Cadastro de Produtos ##')

with containerCadastrar:
    nome = st.text_input('Nome do produto', placeholder='Nome do produto com no máximo 50 caracteres')
    imagem = st.text_input('Imagem do produto', placeholder='Url da imagem do produto com até 100 caracteres')
    codigo = st.text_input('Código do produto', placeholder='Código do produto')
    preco = float(st.number_input('Preço produto'))
    btnCadastrarProduto = st.button('Cadastrar Produto')

if btnCadastrarProduto:
    cadastrar(nome, preco, codigo, imagem)
    st.write('Produto cadastrado com sucesso')


