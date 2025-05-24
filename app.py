from flask import Flask, request, redirect, render_template_string
import hashlib

app = Flask(__name__)

# In-memory dictionary to store URL mappings
url_map = {}

# Route for the homepage (index)
@app.route('/')
def index():
    return render_template_string("""
        <h1>URL Shortener</h1>
        <form action="/shorten" method="post">
            <label for="url">Enter URL to shorten:</label>
            <input type="text" id="url" name="url" required>
            <input type="submit" value="Shorten">
        </form>
    """)

# Route to handle URL shortening
@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    # Create a simple hash of the URL to shorten it
    shortened_url = hashlib.md5(original_url.encode()).hexdigest()[:6]
    url_map[shortened_url] = original_url
    return f"Shortened URL: <a href='/{shortened_url}'>/{shortened_url}</a>"

# Route to redirect to the original URL using the shortened URL
@app.route('/<shortened_url>')
def redirect_to_url(shortened_url):
    original_url = url_map.get(shortened_url)
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
