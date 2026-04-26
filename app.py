from flask import Flask, render_template, request, redirect, url_for
from database import SessionLocal, engine, Base
from crud import create_student, get_student, delete_student
from models import Student
import os

app = Flask(__name__)

# Initialize database
Base.metadata.create_all(bind=engine)

@app.route('/')
def index():
    db = SessionLocal()
    try:
        students = db.query(Student).all()
        return render_template('index.html', students=students)
    finally:
        db.close()

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    age = request.form.get('age')
    course = request.form.get('course')
    
    if name and age and course:
        db = SessionLocal()
        try:
            create_student(db, name, int(age), course)
        finally:
            db.close()
            
    return redirect(url_for('index'))

@app.route('/delete/<int:student_id>', methods=['POST'])
def delete(student_id):
    db = SessionLocal()
    try:
        delete_student(db, student_id)
    finally:
        db.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Ensure templates and static folders exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    app.run(debug=True, port=5000)
