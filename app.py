from os.path import exists
from flask import Flask
from flask import render_template, abort

app = Flask(__name__)

#
# to run:
#   flask run
#
#

@app.route('/<path:gantt_file>')
def index(gantt_file):

    filename = f"charts/{gantt_file}.gantt"

    if exists(filename):
        with open(filename, "r") as f:
            mermaid_code = f.read()
            return render_template(
                'index.html',
                title=f'Gantt - {gantt_file}',
                code=mermaid_code
                )
    else:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
