from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def vectorize(Text):
    return TfidfVectorizer().fit_transform(Text).toarray()

def similarity(doc1, doc2):
    return cosine_similarity([doc1, doc2])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    uploaded_files = request.files.getlist("files")
    filenames = []
    contents = []

    for file in uploaded_files:
        if file.filename == '':
            continue
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        filenames.append(file.filename)
        contents.append(open(filepath, encoding='utf-8').read())

    if len(contents) < 2:
        return render_template('index.html', error="Please upload at least two text files.")

    vectors = vectorize(contents)
    s_vectors = list(zip(filenames, vectors))
    results = []

    for i, (fileA, vecA) in enumerate(s_vectors):
        for j in range(i + 1, len(s_vectors)):
            fileB, vecB = s_vectors[j]
            sim_score = similarity(vecA, vecB)[0][1]
            results.append({
                'file1': fileA,
                'file2': fileB,
                'score': f"{sim_score * 100:.2f}%"
            })

    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
