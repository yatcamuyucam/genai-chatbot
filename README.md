# Futbol Kuralları Chatbot'u (genai-chatbot)

Bu proje, Akbank GenAI Bootcamp kapsamında geliştirilmiş RAG (Retrieval-Augmented Generation) tabanlı bir chatbot'tur.

##  Projenin Amacı
Bu chatbot'un amacı, TFF 2024-2025 Futbol Oyun Kuralları kitapçığını bir bilgi kaynağı olarak kullanarak, futbol kuralları hakkındaki sorulara anında ve doğru yanıtlar vermektir.

## Kullanılan Teknolojiler
* **Dil Modeli (LLM):** Google Gemini 1.5 Flash
* **Embedding Modeli:** Google text-embedding-004
* **Framework:** LangChain
* **Vektör Veritabanı:** ChromaDB
* **Veri Kaynağı:** TFF 2024-2025 Futbol Oyun Kuralları PDF'i

## Çalışma Kılavuzu (Installation Guide)

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1.  **Projeyi Klonlayın:**
    ```bash
    git clone [https://github.com/yatcamuyucam/genai-chatbot.git](https://github.com/yatcamuyucam/genai-chatbot.git)
    cd genai-chatbot
    ```

2.  **Sanal Ortam Oluşturun ve Aktifleştirin:**
    ```bash
    # Sanal ortamı oluştur
    python -m venv venv

    # Windows için aktifleştirme:
    .\\venv\\Scripts\\activate
    
    # macOS/Linux için aktifleştirme:
    # source venv/bin/activate
    ```

3.  **Gerekli Paketleri Yükleyin:**
    `requirements.txt` dosyası ile projenin tüm bağımlılıklarını kurun.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Notebook'u Çalıştırın:**
    Jupyter Notebook veya Jupyter Lab'i başlatarak `futbol_chatbook.ipynb` dosyasını açın. Notebook içerisindeki hücreleri sırasıyla çalıştırmadan önce, Google API anahtarınızı ilgili hücreye eklemeyi unutmayın.
