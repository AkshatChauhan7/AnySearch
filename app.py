import os
from flask import Flask, render_template, request, redirect, url_for, flash
from exa_py import Exa

try:
    from dotenv import load_dotenv
    load_dotenv() 
    print("Loaded environment from .env file")
except ImportError:
    print("dotenv package not installed, using OS environment variables only")

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', 'dev-secret')


def get_exa_client():
    api_key = os.environ.get('EXA_API_KEY')
    if not api_key:
        return None
    return Exa(api_key)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.values.get('query', '').strip()
    if not query:
        flash('Please enter a search query', 'warning')
        return redirect(url_for('index'))

    client = get_exa_client()
    if client is None:
        flash('EXA_API_KEY is not set. Set the EXA_API_KEY environment variable and restart the app.', 'danger')
        return redirect(url_for('index'))

    try:
        domains_raw = request.values.get('domains', '') or ''
        domains = []
        for part in [d.strip() for d in domains_raw.split(',') if d.strip()]:
            if part.startswith('http://') or part.startswith('https://'):
                domains.append(part)
            else:
                domains.append('https://' + part)

        if domains:
            response = client.search(
                query,
                num_results=10,
                type='keyword',
                include_domains=domains,
            )
        else:
            response = client.search(
                query,
                num_results=10,
                type='keyword',
            )
    except Exception as e:
        flash(f'Error while searching: {e}', 'danger')
        return redirect(url_for('index'))

    results = []
    for r in getattr(response, 'results', []) or []:
        results.append({
            'title': getattr(r, 'title', '') or '',
            'url': getattr(r, 'url', '') or '',
            'snippet': getattr(r, 'snippet', '') or '',
        })

    return render_template('results.html', query=query, results=results, raw=response)


if __name__ == '__main__':
    api_key = os.environ.get('EXA_API_KEY')
    if not api_key:
        print("WARNING: EXA_API_KEY environment variable not set.")
        print("The app will use the .env file if available.")
        print("Otherwise, set this variable before running the app:")
        print("  - Windows: $env:EXA_API_KEY = 'your-key'")
        print("  - Linux/Mac: export EXA_API_KEY='your-key'")
        print("See README.md for more information.")
    else:
        print(f"Found API key in environment: {api_key[:5]}...{api_key[-4:]}")
    app.run(debug=True, host='127.0.0.1', port=5000)
