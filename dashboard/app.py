
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            return redirect(url_for('admin_homepage'))
    return render_template('login.html')

@app.route('/admin/homepage')
def admin_homepage():
    return render_template('admin/homepage.html')

if __name__ == '__main__':
    app.run(debug=True)
