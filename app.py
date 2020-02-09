from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quizMain():
    return render_template('quiz.html')

@app.route('/quizType1')
def quizType1():
    return render_template('quiz_type1.html')

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)