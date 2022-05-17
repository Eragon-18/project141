from flask import Flask, jsonify, request
import csv

all_articles = []

with open('articles.csv', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked = []
not_liked = []

app = Flask(__name__)

@app.route('/get-article')
def getArticle():
    return jsonify({'data': all_articles[0], 'status': 'success'})

@app.route('/liked-article', methods = ['POST'])
def likedArticle():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked.append(article)
    return jsonify({'status': 'success'}), 201

@app.route('/not-liked', methods = ['POST'])
def notLiked():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked.append(article)
    return jsonify({'status': 'success'}), 201

if __name__ == '__main__':
    app.run()