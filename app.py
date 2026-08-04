from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Embed Player</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            background-color: #000;
            overflow: hidden;
            position: relative;
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
        /* Transparent shield over the video */
        #ad-shield {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 999;
            background: rgba(0, 0, 0, 0); /* Invisible */
            cursor: pointer;
        }
    </style>
</head>
<body>

    <div id="ad-shield" onclick="removeShield()"></div>

    <iframe 
        src="{{ embed_url }}" 
        allowfullscreen>
    </iframe>

    <script>
        function removeShield() {
            // Absorbs the initial click that would normally open an ad popup
            const shield = document.getElementById('ad-shield');
            shield.style.display = 'none';
        }
    </script>
</body>
</html>
"""

# Movie Route: Handles URLs like /94997
@app.route('/<movie_id>')
def serve_movie(movie_id):
    embed_url = f"https://www.vidking.net/embed/movie/{movie_id}?color=e50914"
    return render_template_string(HTML_TEMPLATE, embed_url=embed_url)

# Series Route: Handles URLs like /94997/1/1
@app.route('/<show_id>/<season>/<episode>')
def serve_series(show_id, season, episode):
    embed_url = f"https://www.vidking.net/embed/tv/{show_id}/{season}/{episode}?color=e50914"
    return render_template_string(HTML_TEMPLATE, embed_url=embed_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)