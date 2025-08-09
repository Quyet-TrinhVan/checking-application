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

@app.route('/admin/setting')
def admin_setting():
    return render_template('admin/setting.html')

@app.route('/admin/setting_lecturer.html')
def setting_lecturer_partial():
    return render_template('admin/setting_lecturer.html')

@app.route('/admin/setting_student.html')
def setting_student_partial():
    return render_template('admin/setting_student.html')

@app.route('/admin/setting_course.html')
def setting_course_partial():
    return render_template('admin/setting_course.html')

@app.route('/admin/setting_room.html')
def setting_room_partial():
    return render_template('admin/setting_room.html')

if __name__ == '__main__':
    app.run(debug=True)
