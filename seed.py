from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
import os
from dotenv import load_dotenv

from models import Group, Teacher, Subject, Student, Grade

# Завантаження змінних середовища
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL не знайдено в .env файлі")

# Підключення до БД
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Ініціалізація Faker
fake = Faker()

# Очистка таблиць у правильному порядку
session.query(Grade).delete()
session.query(Student).delete()
session.query(Subject).delete()
session.query(Teacher).delete()
session.query(Group).delete()
session.commit()

# Створення груп (3)
groups = [Group(name=f"Group-{i+1}") for i in range(3)]
session.add_all(groups)
session.commit()

# Створення викладачів (3–5)
teachers = [Teacher(name=fake.name()) for _ in range(random.randint(3, 5))]
session.add_all(teachers)
session.commit()

# Створення предметів (5–8), кожен з випадковим викладачем
subject_names = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology",
    "History",
    "Literature",
    "English",
    "Geography",
]
selected_subjects = random.sample(subject_names, random.randint(5, 8))
subjects = [
    Subject(name=name, teacher=random.choice(teachers)) for name in selected_subjects
]
session.add_all(subjects)
session.commit()

# Створення студентів (30–50), з прив'язкою до груп
students = [
    Student(name=fake.name(), group=random.choice(groups))
    for _ in range(random.randint(30, 50))
]
session.add_all(students)
session.commit()

# Створення оцінок для кожного студента з усіх предметів (до 20 на предмет)
grades = []
for student in students:
    for subject in subjects:
        for _ in range(random.randint(10, 20)):
            grades.append(
                Grade(
                    student=student,
                    subject=subject,
                    grade=random.randint(3, 12),
                    date=fake.date_between(start_date="-6M", end_date="today"),
                )
            )
session.add_all(grades)
session.commit()

session.close()
print("База наповнена тестовими даними.")