# ⚽ Futbol Kuralları Chatbot'u (genai-chatbot)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-009688?style=for-the-badge&logo=langchain&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-8E44AD?style=for-the-badge&logo=google&logoColor=white)

Bu proje, Akbank GenAI Bootcamp kapsamında geliştirilmiş RAG (Retrieval-Augmented Generation) tabanlı bir chatbot'tur.

## 🚀 Canlı Uygulama

Projenin canlı demosunu ziyaret edin:
**[https://football-chatbook.streamlit.app/](https://football-chatbook.streamlit.app/)**

<img width="871" height="700" alt="image" src="https://github.com/user-attachments/assets/9af0c130-c334-4b0a-a580-a73370efbac7" />


---

## Projenin Amacı

Bu chatbot'un temel amacı, TFF 2024-2025 Futbol Oyun Kuralları kitapçığını bir bilgi kaynağı olarak kullanarak, futbol kuralları hakkındaki sorulara anında ve doğru yanıtlar vermektir. Bu araç, futbolseverlerin, hakem adaylarının, gazetecilerin veya öğrencilerin spesifik kural sorularına hızlıca ve güvenilir bir kaynaktan yanıt bulabilmesi için tasarlanmıştır.

## Veri Seti ve Hazırlanışı

* **Kaynak:** Projenin bilgi tabanı olarak [TFF 2024-2025 Futbol Oyun Kuralları PDF](https://www.tff.org/Resources/TFF/Documents/MHK/2024-2025/oyun-kurallari.pdf)'i kullanılmıştır.
* **Problem:** PDF'ten `PyMuPDF` gibi araçlarla otomatik metin çıkarma denemelerinde, özellikle şemalar ve tablolar içeren "Kural 11: Ofsayt" gibi bölümlerde metinlerin bozulduğu ve anlamsal bütünlüğün kaybolduğu tespit edilmiştir.
* **Çözüm:** Veri kalitesini ve chatbot'un doğruluğunu garanti altına almak için, PDF'teki metinler manuel olarak temizlenmiş ve `kurallar.txt` adında bir metin dosyası olarak projeye dahil edilmiştir. Uygulama, bu temizlenmiş dosyayı kaynak olarak kullanmaktadır.

## Geliştirme Süreci ve Metodoloji

Bu projenin RAG mimarisi, en uygun bileşenleri bulmak için Google Colab üzerinde prototiplenmiştir.

1.  **Prototipleme (Google Colab):** İlk denemeler, metin parçalama (`chunk_size`, `chunk_overlap`) ve embedding modelleri için bir test ortamı olarak Colab'de yapılmıştır.
2.  **Embedding Model Seçimi:**
    * Başlangıçta, hızlı ve popüler bir açık kaynak model olan `sentence-transformers/all-MiniLM-L6-v2` (Hugging Face) test edilmiştir.
    * Ancak, "ofsayt nedir?" gibi spesifik ve teknik sorularda bu modelin yeterli anlamsal derinliği sağlayamadığı ve yanlış metin parçalarını getirdiği görülmüştür.
    * Bu nedenle, daha yüksek anlamsal doğruluk ve daha iyi sorgu eşleşmesi sağlayan `Google text-embedding-004` modeline geçiş yapılmıştır.
3.  **Yerel Geliştirme (VS Code):** En uygun parametreler (chunk boyutu, embedding modeli, prompt şablonu) bulunduktan sonra proje, kalıcı bir web uygulaması oluşturmak için VS Code'a taşınmıştır.
4.  **Uygulama Arayüzü:** Prototip (`.ipynb`) formatından, `Streamlit` kullanılarak `app.py` adında interaktif bir chatbot uygulamasına dönüştürülmüştür.

## Kullanılan Ana Teknolojiler

* **Dil Modeli (LLM):** Google Gemini 1.5 Flash
* **Embedding Modeli:** Google text-embedding-004
* **Framework:** LangChain (LCEL ile RAG zinciri oluşturmak için)
* **Vektör Veritabanı:** ChromaDB (Yerel ve hızlı vektör araması için)
* **Arayüz:** Streamlit (İnteraktif web uygulaması için)
* **Dağıtım (Deployment):** Streamlit Community Cloud

## Çalışma Kılavuzu (Yerel Kurulum)

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
    .\venv\Scripts\activate
    
    # macOS/Linux için aktifleştirme:
    # source venv/bin/activate
    ```

3.  **Gerekli Paketleri Yükleyin:**
    `requirements.txt` dosyası ile projenin tüm bağımlılıklarını kurun.
    ```bash
    pip install -r requirements.txt
    ```

4.  **.env Dosyası Oluşturun (Çok Önemli):**
    `app.py` dosyasının çalışabilmesi için Google API anahtarınıza ihtiyacı vardır. Proje ana dizininde `.env` adında bir dosya oluşturun ve içine kendi API anahtarınızı aşağıdaki gibi ekleyin:
    ```
    GOOGLE_API_KEY="AIzaSy...ile_baslayan_kendi_anahtarınız"
    ```

5.  **Uygulamayı Çalıştırın:**
    Notebook yerine Streamlit uygulamasını çalıştırın:
    ```bash
    streamlit run app.py
    ```
    Uygulama, yerel tarayıcınızda (`http://localhost:8501`) açılacaktır.
