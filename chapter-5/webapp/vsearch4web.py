from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None: 
    with open('vsearch.log', 'a') as log: 
        print(req, res, file=log)

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    the_title = "Here are your results:"
    the_results = str(search4letters(phrase, letters))
    log_request(request, the_results)
    return render_template('results.html', the_title=the_title, the_results=the_results, the_phrase=phrase, the_letters=letters)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome to search4letters on the web!")

@app.route('/viewlog') 
def view_the_log() -> str: 
    with open('vsearch.log') as log: 
        contents = log.read() 
        return escape(contents)

if __name__ == '__main__':
    app.run(debug=True)