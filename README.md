# 🧩 Plagiarism Checker using Flask & Machine Learning

An **AI-powered plagiarism detection web app** built with **Flask** and **Scikit-learn**.  
It allows users to upload multiple text files and instantly check how similar they are using **TF-IDF Vectorization** and **Cosine Similarity**.  
The app features a **modern dark UI** with real-time similarity results.

---

## 🚀 Features

- 🧠 Detects similarity between multiple text files  
- 📂 Upload multiple `.txt` files at once  
- ⚡ Instant similarity calculation using **TF-IDF** + **Cosine Similarity**  
- 🎨 Stylish dark responsive interface (HTML + CSS + Flask Jinja templates)  
- 🧾 Displays similarity scores in an elegant results table  
- 🛡️ Built using pure **Python, Flask, and Scikit-learn**

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | Flask (Python) |
| **Machine Learning** | Scikit-learn |
| **Frontend** | HTML5, CSS3, Jinja2 |
| **Algorithm** | TF-IDF Vectorizer + Cosine Similarity |

---

## 📂 Folder Structure
PlagiarismChecker/
│
├── app.py                # Flask backend
├── uploads/              # Uploaded files
├── templates/
│   └── index.html        # Frontend HTML template
└── static/
└── style.css         # Dark theme styling

---

## ⚙️ Installation & Usage

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/Plagiarism-Checker.git
cd Plagiarism-Checker

2️⃣ Install dependencies
pip install flask scikit-learn

3️⃣ Run the Flask app
python app.py

4️⃣ Open in your browser
http://127.0.0.1:5000


🧮 How It Works


Each uploaded .txt file is read and converted into a TF-IDF vector.


The similarity between every pair of documents is calculated using cosine similarity.


The web app displays a clean comparison table showing file names and their similarity percentage.



🖼️ Screenshot


✨ Future Enhancements


📊 Downloadable PDF/Excel plagiarism report


🔍 Sentence-level similarity highlighting


🌐 Multi-language support


☁️ Cloud file storage integration



👨‍💻 Author
Arpit Singh
💼 Passionate Developer & AI Enthusiast
📧 Contact: [your-email@example.com]

🧠 Keywords
Python • Flask • Machine Learning • Scikit-learn • Plagiarism Detection • AI • TF-IDF • Cosine Similarity • NLP • Web App

⭐ If you like this project, give it a star on GitHub!

---




