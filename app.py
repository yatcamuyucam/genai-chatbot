# app.py (Chatbot versiyonu)

import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter

# .env dosyasındaki değişkenleri ortam değişkeni olarak yükler
load_dotenv()

# --- Streamlit Arayüz Ayarları ---
st.set_page_config(page_title="Futbol Kuralları Chatbot'u", page_icon="⚽")
st.title("⚽ Futbol Oyun Kuralları Chatbot'u")
st.caption("TFF 2024-2025 Kural Kitabı ile konuşun")


# --- RAG Zincirini Fonksiyonlar İçinde Tanımlama (Cache'leme ile) ---

@st.cache_resource
def create_rag_chain():
    """Veritabanını oluşturur ve RAG zincirini kurar."""
    try:
        with open('kurallar.txt', 'r', encoding='utf-8') as f:
            text_data = f.read()
    except FileNotFoundError:
        st.error("Hata: 'kurallar.txt' dosyası bulunamadı.")
        return None

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=250)
    docs = text_splitter.create_documents([text_data])
    
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    vector_store = Chroma.from_documents(documents=docs, embedding=embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})

    template = """
# GÖREVİN
Sen, IFAB Futbol Oyun Kuralları kitabının dijital bir temsilcisisin. Sadece sana verilen EK BİLGİ'yi kullanarak cevap ver. Cevabını Markdown formatında, okunaklı paragraflar halinde yaz.

EK BİLGİ:
{context}

SORU: {question}

DETAYLI CEVAP:
"""
    prompt = PromptTemplate.from_template(template)
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.4,
        top_k=40,
        max_output_tokens=2048
        )

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

# RAG zincirini yükle
rag_chain = create_rag_chain()

# --- Sohbet Mantığı ---

# 1. Sohbet geçmişi için session_state'i başlat
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Merhaba! TFF 2024-2025 Futbol Oyun Kuralları hakkında ne bilmek istersin?"}]

# 2. Geçmiş mesajları ekrana yazdır
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Kullanıcıdan yeni bir girdi al
if prompt := st.chat_input("Ofsayt kuralını açıkla..."):
    # a. Kullanıcının mesajını sohbet geçmişine ekle ve ekrana yazdır
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # b. Asistanın cevabını oluştur ve ekrana yazdır
    if rag_chain is not None:
        with st.chat_message("assistant"):
            with st.spinner("Düşünüyor..."):
                response = rag_chain.invoke(prompt)
                st.markdown(response)
        # c. Asistanın cevabını da sohbet geçmişine ekle
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.error("Uygulama düzgün başlatılamadı.")