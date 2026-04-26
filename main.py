from database import SessionLocal, engine, Base
from crud import create_student, get_student, delete_student
from models import Student

def main():
    # Initialize the database
    print("Initializing Database...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Create Students
        print("\nAdding students...")
        s1 = create_student(db, "Alice Johnson", 20, "Computer Science")
        s2 = create_student(db, "Bob Smith", 22, "Mechanical Engineering")
        print(f"Created: {s1.name} (ID: {s1.id})")
        print(f"Created: {s2.name} (ID: {s2.id})")
        
        # Get and Display Students
        print("\nFetching all students from DB:")
        students = db.query(Student).all()
        for s in students:
            print(f"- ID: {s.id}, Name: {s.name}, Age: {s.age}, Course: {s.course}")
            
        # Get specific student
        student_id = s1.id
        print(f"\nFetching student with ID {student_id}...")
        found = get_student(db, student_id)
        if found:
            print(f"Found: {found.name}")
            
        # Delete a student
        print(f"\nDeleting student with ID {s2.id}...")
        if delete_student(db, s2.id):
            print("Successfully deleted.")
        
        # Final list
        print("\nFinal Student List:")
        students = db.query(Student).all()
        for s in students:
            print(f"- ID: {s.id}, Name: {s.name}, Age: {s.age}, Course: {s.course}")

    finally:
        db.close()

if __name__ == "__main__":
    main()
