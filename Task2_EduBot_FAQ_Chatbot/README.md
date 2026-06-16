# 🎓 Task 2 — EduBot: Smart College FAQ Assistant

## 📌 Project Overview
EduBot is an intelligent FAQ chatbot for college students built using 
Natural Language Processing (NLP) techniques.

The chatbot understands student questions and finds the most relevant 
answer from a FAQ database using text similarity matching.

## 🤖 Live Demo
🔗 **[Click here to use EduBot Live](https://huggingface.co/spaces/nandhini-k23/edubot-faq-chatbot)**

## 🚀 Project Links

| Platform | Link | Purpose |
|---|---|---|
| 🤗 Hugging Face | [Open Live Chatbot](https://huggingface.co/spaces/nandhini-k23/edubot-faq-chatbot) | Permanent live demo — works 24/7 |
| 📓 Google Colab | [Open Notebook](https://colab.research.google.com/drive/1I4C8U4EHjm5-5S-WpBFUj-39CergpoNb?usp=sharing) | Complete NLP code with outputs |

> 🤗 **Hugging Face** — Chatbot is permanently live. No setup needed. Just open and chat!
>
> 📓 **Google Colab** — See complete NLP code step by step with all outputs explained.

## 🧠 NLP Techniques Used
- **Tokenization** — Breaking sentences into individual words using NLTK
- **Stop Word Removal** — Removing common useless words
- **Stemming** — Reducing words to root form using PorterStemmer
- **TF-IDF Vectorization** — Converting text to numerical vectors
- **Cosine Similarity** — Finding most similar FAQ question mathematically

## 📚 Dataset
- 40 College related FAQ questions and answers
- Topics: Admissions, Exams, Certificates, Scholarships, Placements, 
  Hostel, Transport, Medical, Grievance

## 🛠️ Libraries Used
| Library | Purpose |
|---|---|
| NLTK | Natural Language Processing |
| Scikit-learn | TF-IDF and Cosine Similarity |
| Gradio | Chat User Interface |
| Pandas | Data Management |

## ✨ Features
- 🎯 Intelligent question matching using Cosine Similarity
- 📊 Confidence score displayed for every answer
- ⚡ Quick category buttons for instant answers
- 🌙 Animated dark theme UI
- 🤖 Robot avatar for bot messages
- 📱 Fully responsive design

## 🚀 How to Run
1. Open the Colab notebook
2. Run all cells from top to bottom
3. Click the Gradio public URL

## 📓 Colab Notebook
Open and run the complete project notebook with all NLP steps explained.

## 🏗️ Project Flow
User types question
↓
Preprocess text (lowercase, tokenize, remove stopwords, stem)
↓
Convert to TF-IDF vector
↓
Compare with all FAQ vectors using Cosine Similarity
↓
Return best matching answer with confidence score

## ⚠️ Limitations
This is a Retrieval Based chatbot — it can only answer questions 
present in the FAQ dataset. For questions outside the dataset it 
finds the closest match which may not always be accurate.

## 👩‍💻 Built By
Nandhini | CodeAlpha AI Internship | Task 2

## ⚠️ Limitations and Future Improvements

### Current Limitation
This is a Retrieval Based FAQ Chatbot.
It can only answer questions present in the FAQ dataset.
For questions outside the dataset it finds the closest 
match which may not always be accurate.

### Why This Happens
The chatbot uses TF-IDF and Cosine Similarity to find
the most similar FAQ. It has no automatic knowledge —
it only knows what we explicitly programmed into it.

### Future Improvements
- Add more FAQ questions to expand knowledge base
- Integrate with Generative AI model like GPT for unknown questions
- Implement intent classification for better matching
- Add feedback system so users can rate answers
- Support Tamil language questions
