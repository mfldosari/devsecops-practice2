from flask import Flask, request, render_template_string, make_response
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST', 'db')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'appdb')
DB_USER = os.environ.get('DB_USER', 'appuser')
DB_PASS = os.environ.get('DB_PASS', 'apppassword')

def get_conn():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    query = ""
    if request.method == 'POST':
        query = request.form.get('query', '')
        try:
            # VULNERABLE: Directly using user input in SQL (SQL Injection)
            conn = get_conn()
            cur = conn.cursor()
            cur.execute(query)
            if cur.description is not None:
                # Query returned rows
                result = cur.fetchall()
            else:
                # Query did not return rows (e.g., INSERT/UPDATE)
                result = 'Query executed.'
            cur.close()
            conn.close()
        except Exception as e:
            error = str(e)
    return render_template_string('''
        <h2>PostgreSQL Web Interface (Vulnerable)</h2>
        <form method="post">
            <input name="query" value="{{ query|e }}" style="width:400px;" />
            <input type="submit" value="Run" />
        </form>
        {% if result %}<pre>{{ result|e }}</pre>{% endif %}
        {% if error %}<pre style="color:red;">{{ error|e }}</pre>{% endif %}
        <p style="color:red;">Warning: This app is intentionally vulnerable to SQL injection for testing purposes.</p>
    ''', result=result, error=error, query=query)

@app.after_request
def set_security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'  # Anti-clickjacking
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self';"  # Improved CSP
    response.headers['Permissions-Policy'] = 'geolocation=()'
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    # Remove Server header if possible
    if 'Server' in response.headers:
        del response.headers['Server']
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
