from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is for check the jenkins poll scm'
