from sqlalchemy.orm import Session
from models import Student

def create_student(db: Session, name, age, course):
    student = Student(name=name, age=age, course=course)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_student(db: Session, student_id):
    return db.query(Student).filter(Student.id == student_id).first()

def delete_student(db: Session, student_id):
    student = get_student(db, student_id)
    if student:
        db.delete(student)
        db.commit()
        return True
    return False