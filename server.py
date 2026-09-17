from flask import Flask, redirect

# A simple server which accepts an http call (e.g. 0.0.0.0/rungameid/12345) and redirects to the steam://rungameid/12345 URL. This is needed because the Stream Deck software does not allow direct steam:// links.


def create_app():
    flask_app = Flask("Steam Protocol Redirect")

    @flask_app.route("/")
    def index():
        return "Steam Protocol Redirect Server is running."

    @flask_app.route("/rungameid/<int:game_id>")
    def run_game(game_id):
        steam_url = f"steam://rungameid/{game_id}"
        return redirect(steam_url)

    return flask_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
