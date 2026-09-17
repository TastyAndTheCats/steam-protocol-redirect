from flask import Flask, redirect

# A simple server which accepts an http call (e.g. 0.0.0.0/rungameid/12345) and redirects to the steam://rungameid/12345 URL. This is needed because the Stream Deck software does not allow direct steam:// links.


app = Flask("Steam Protocol Redirect")


@app.route("/")
def index():
    return "Steam Protocol Redirect Server is running."


@app.route("/rungameid/<int:game_id>")
def run_game(game_id):
    steam_url = f"steam://rungameid/{game_id}"
    return redirect(steam_url)


app.run(host="0.0.0.0", port=5000)
