import streamlit as st
import langchain_helper
st.title('✍️🤖 BlogMaker : Your AI Writing Companion')

st.subheader('Now you can make a blog with the help of AI, BlogMaker is your new AI Companion')

with st.sidebar:
    st.title('Blog Details')
    st.subheader('Enter Blog Detail that you want to make')

    blog_title = st.text_input("Blog Title")

    keyword = st.text_area("Enter Key words(Comma Separted)")

    num_words = st.slider('Number of words',min_value=200,max_value=2000,step=100)

    button = st.button('Generate Blog')

    blog_content = f"Generating a {num_words}-word blog on '{blog_title}'. with keywords '{keyword}' and give detail about keywords regarding topic. it should completed if it takes some more number of words that's okay."
    respone = langchain_helper.generate_text(blog_content,num_words+2000)


if button:
    st.write(respone.strip())