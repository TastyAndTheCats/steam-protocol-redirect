from flask import Flask, request, render_template_string

# A simple server which accepts an http call (e.g. 0.0.0.0/rungameid/12345) and redirects to the steam://rungameid/12345 URL. This is needed because the Stream Deck software does not allow direct steam:// links.


def create_app():
    flask_app = Flask("Steam Protocol Redirect")

    @flask_app.route("/")
    def index():
        return "Steam Protocol Redirect Server is running."

    @flask_app.route("/rungameid/<int:game_id>")
    def run_game(game_id):
        steam_url = f"steam://rungameid/{game_id}"

        # HTML with JavaScript to open new tab and close current one
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Redirecting...</title>
            <script>
                window.onload = function() {{
                    // Open in a new tab
                    window.open("{steam_url}", "_blank");
                    // Close current tab
                    window.close();
                }};
            </script>
        </head>
        <body>
            <p>Redirecting to <a href="{steam_url}" target="_blank">{steam_url}</a>...</p>
        </body>
        </html>
        """
        return render_template_string(html_content)

    return flask_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
