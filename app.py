
import flask  # pyright: ignore[reportMissingImports]

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
