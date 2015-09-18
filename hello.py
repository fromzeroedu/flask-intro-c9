import os

from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'logged in'
    else:
        return '<form method="post" action="/login"><input type="text" /><p><button type="submit">Submit</button></form>'

if __name__ == '__main__':
    app.debug = True
    app.run(app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 5000))))
