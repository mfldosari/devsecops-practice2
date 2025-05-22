from flask import Flask, request, render_template_string
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
            try:
                result = cur.fetchall()
            except Exception:
                result = 'Query executed.'
            cur.close()
            conn.close()
        except Exception as e:
            error = str(e)
    return render_template_string('''
        <h2>PostgreSQL Web Interface (Vulnerable)</h2>
        <form method="post">
            <input name="query" value="{{query}}" style="width:400px;" />
            <input type="submit" value="Run" />
        </form>
        {% if result %}<pre>{{result}}</pre>{% endif %}
        {% if error %}<pre style="color:red;">{{error}}</pre>{% endif %}
        <p style="color:red;">Warning: This app is intentionally vulnerable to SQL injection for testing purposes.</p>
    ''', result=result, error=error, query=query)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
