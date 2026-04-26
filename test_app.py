import pytest
from database import SessionLocal, Base, engine
from crud import create_student, get_student, delete_student

# Setup test DB
Base.metadata.create_all(bind=engine)

def test_create_student():
    db = SessionLocal()
    student = create_student(db, "Teja", 21, "CSE")

    assert student.id is not None
    assert student.name == "Teja"

def test_get_student():
    db = SessionLocal()
    student = create_student(db, "Ravi", 22, "ECE")

    fetched = get_student(db, student.id)

    assert fetched.name == "Ravi"

def test_delete_student():
    db = SessionLocal()
    student = create_student(db, "Kiran", 23, "IT")

    result = delete_student(db, student.id)

    assert result is True