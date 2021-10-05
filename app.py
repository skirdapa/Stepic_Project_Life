from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route("/")
def index():
    GameOfLife(width=25, height=25)
    return render_template("index.html")


@app.route("/live")
def live():
    universe = GameOfLife()
    if universe.life_counter > 0:
        universe.form_new_generation()
    universe.next_count()
    return render_template("live.html", universe=universe)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
