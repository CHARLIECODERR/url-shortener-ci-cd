from flask import Flask, request, redirect, render_template_string, render_template
import hashlib

app = Flask(__name__)

# In-memory dictionary to store URL mappings
url_map = {}

# Route for the homepage (index)
@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        original_url = request.form['url']
        # Create a simple hash of the URL to shorten it
        shortened_url = hashlib.md5(original_url.encode()).hexdigest()[:6]
        url_map[shortened_url] = original_url
        short_url = f"/{shortened_url}"
    
    return render_template('index.html', short_url=short_url)

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
