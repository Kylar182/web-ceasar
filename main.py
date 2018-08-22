from flask import Flask, request 
from ceasar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>        
        <form method="post">
            <input type"text" name="rot" value="0"/>
                <textarea name="text">
                {0}
                </textarea>
            <input type="submit"/>            
        </form>
    </body>
</html> 
"""

@app.route("/")
def index():
    return form

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '</h1>'

@app.route("/", methods=['POST'])
def encrypt():
    rRot = int(request.form["rot"])
    tText = request.form["text"]
    return '<h1>' + rotate_string(tText, rRot) + '</h1>'

app.run()