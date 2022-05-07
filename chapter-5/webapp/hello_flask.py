from flask import Flask

app = Flask(name)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

app.run()