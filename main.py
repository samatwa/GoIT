import argparse
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from models import Group, Teacher, Subject, Student, Grade

# Підключення до бази даних
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL не знайдено в .env файлі")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# CRUD операції
def create_teacher(name: str) -> None:
    """Створює нового викладача."""
    try:
        teacher = Teacher(name=name)
        session.add(teacher)
        session.commit()
        print(f"Створено викладача: {teacher.name} (id={teacher.id})")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при створенні викладача: {e}")


def list_teachers():
    """Виводить список всіх викладачів."""
    for teacher in session.query(Teacher).all():
        print(f"{teacher.id}: {teacher.name}")


def update_teacher(id: int, name: str) -> None:
    """Оновлює ім'я викладача за його ID."""
    try:
        teacher = session.query(Teacher).get(id)
        if teacher:
            teacher.name = name
            session.commit()
            print(f"Оновлено викладача з id={id}")
        else:
            print(f"Викладача з id={id} не знайдено")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при оновленні викладача: {e}")


def remove_teacher(id: int) -> None:
    """Видаляє викладача за його ID."""
    try:
        teacher = session.query(Teacher).get(id)
        if teacher:
            session.delete(teacher)
            session.commit()
            print(f"Видалено викладача з id={id}")
        else:
            print(f"Викладача з id={id} не знайдено")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при видаленні викладача: {e}")


def create_group(name: str) -> None:
    """Створює нову групу."""
    try:
        group = Group(name=name)
        session.add(group)
        session.commit()
        print(f"Створено групу: {group.name} (id={group.id})")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при створенні групи: {e}")


def list_groups():
    """Виводить список всіх груп."""
    for group in session.query(Group).all():
        print(f"{group.id}: {group.name}")


def update_group(id: int, name: str) -> None:
    """Оновлює ім'я групи за її ID."""
    try:
        group = session.query(Group).get(id)
        if group:
            group.name = name
            session.commit()
            print(f"Оновлено групу з id={id}")
        else:
            print(f"Групу з id={id} не знайдено")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при оновленні групи: {e}")


def remove_group(id: int) -> None:
    """Видаляє групу за її ID."""
    try:
        group = session.query(Group).get(id)
        if group:
            session.delete(group)
            session.commit()
            print(f"Видалено групу з id={id}")
        else:
            print(f"Групу з id={id} не знайдено")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при видаленні групи: {e}")


def create_subject(name: str, teacher_id: int) -> None:
    """Створює новий предмет."""
    try:
        subject = Subject(name=name, teacher_id=teacher_id)
        session.add(subject)
        session.commit()
        print(f"Створено предмет: {subject.name} (id={subject.id})")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при створенні предмета: {e}")


def list_subjects():
    """Виводить список всіх предметів."""
    for subject in session.query(Subject).all():
        print(f"{subject.id}: {subject.name}, викладач id={subject.teacher_id}")


def update_subject(id: int, name: str, teacher_id: int) -> None:
    """Оновлює ім'я предмета за його ID."""
    try:
        subject = session.query(Subject).get(id)
        if subject:
            subject.name = name
            subject.teacher_id = teacher_id
            session.commit()
            print(f"Оновлено предмет з id={id}")
        else:
            print(f"Предмет з id={id} не знайдено")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при оновленні предмета: {e}")


def remove_subject(id: int) -> None:
    """Видаляє предмет за його ID."""
    try:
        subject = session.query(Subject).get(id)
        if subject:
            session.delete(subject)
            session.commit()
            print(f"Видалено предмет з id={id}")
        else:
            print(f"Предмет з id={id} не знайдено")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при видаленні предмета: {e}")


def create_student(name: str, group_id: int) -> None:
    """Створює нового студента."""
    try:
        student = Student(name=name, group_id=group_id)
        session.add(student)
        session.commit()
        print(f"Створено студента: {student.name} (id={student.id})")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при створенні студента: {e}")


def list_students():
    """Виводить список всіх студентів."""
    for student in session.query(Student).all():
        print(f"{student.id}: {student.name}, група id={student.group_id}")


def update_student(id: int, name: str, group_id: int) -> None:
    """Оновлює ім'я студента за його ID."""
    try:
        student = session.query(Student).get(id)
        if student:
            student.name = name
            student.group_id = group_id
            session.commit()
            print(f"Оновлено студента з id={id}")
        else:
            print(f"Студента з id={id} не знайдено")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при оновленні студента: {e}")


def remove_student(id: int) -> None:
    """Видаляє студента за його ID."""
    try:
        student = session.query(Student).get(id)
        if student:
            session.delete(student)
            session.commit()
            print(f"Видалено студента з id={id}")
        else:
            print(f"Студента з id={id} не знайдено")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при видаленні студента: {e}")


def create_grade(student_id: int, subject_id: int, grade: int, date: str) -> None:
    """Створює нову оцінку."""
    try:
        grade_obj = Grade(
            student_id=student_id, subject_id=subject_id, grade=grade, date=date
        )
        session.add(grade_obj)
        session.commit()
        print(
            f"Додано оцінку: {grade} для студента {student_id} з предмета {subject_id} на дату {date}"
        )
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при створенні оцінки: {e}")


def list_grades():
    """Виводить список всіх оцінок."""
    for grade in session.query(Grade).all():
        print(
            f"{grade.id}: Студент {grade.student_id}, Предмет {grade.subject_id}, Оцінка {grade.grade}, Дата {grade.date}"
        )


def update_grade(id: int, grade_value: int, date: str) -> None:
    """Оновлює оцінку за її ID."""
    try:
        grade = session.query(Grade).get(id)
        if grade:
            grade.grade = grade_value
            grade.date = date
            session.commit()
            print(f"Оновлено оцінку з id={id}")
        else:
            print(f"Оцінку з id={id} не знайдено")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при оновленні оцінки: {e}")


def remove_grade(id: int) -> None:
    """Видаляє оцінку за її ID."""
    try:
        grade = session.query(Grade).get(id)
        if grade:
            session.delete(grade)
            session.commit()
            print(f"Видалено оцінку з id={id}")
        else:
            print(f"Оцінку з id={id} не знайдено")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Помилка при видаленні оцінки: {e}")


def main():
    parser = argparse.ArgumentParser(description="CLI для CRUD операцій")
    parser.add_argument(
        "-a", "--action", required=True, help="CRUD дія: create, list, update, remove"
    )
    parser.add_argument(
        "-m",
        "--model",
        required=True,
        help="Модель: Teacher, Group, Subject, Student, Grade",
    )
    parser.add_argument("--name", help="Ім'я (для Teacher, Group, Student, Subject)")
    parser.add_argument("--id", type=int, help="ID запису (для update/remove)")
    parser.add_argument("--teacher_id", type=int, help="ID викладача (для Subject)")
    parser.add_argument("--group_id", type=int, help="ID групи (для Student)")
    parser.add_argument("--student_id", type=int, help="ID студента (для Grade)")
    parser.add_argument("--subject_id", type=int, help="ID предмета (для Grade)")
    parser.add_argument("--grade", type=int, help="Оцінка (для Grade)")
    parser.add_argument("--date", help="Дата оцінки у форматі YYYY-MM-DD (для Grade)")

    args = parser.parse_args()

    if args.model == "Teacher":
        if args.action == "create" and args.name:
            create_teacher(args.name)
        elif args.action == "list":
            list_teachers()
        elif args.action == "update" and args.id and args.name:
            update_teacher(args.id, args.name)
        elif args.action == "remove" and args.id:
            remove_teacher(args.id)
        else:
            print("Недостатньо аргументів або невідома дія")
    elif args.model == "Group":
        if args.action == "create" and args.name:
            create_group(args.name)
        elif args.action == "list":
            list_groups()
        elif args.action == "update" and args.id and args.name:
            update_group(args.id, args.name)
        elif args.action == "remove" and args.id:
            remove_group(args.id)
        else:
            print("Недостатньо аргументів або невідома дія")
    elif args.model == "Subject":
        if args.action == "create" and args.name and args.teacher_id:
            create_subject(args.name, args.teacher_id)
        elif args.action == "list":
            list_subjects()
        elif args.action == "update" and args.id and args.name and args.teacher_id:
            update_subject(args.id, args.name, args.teacher_id)
        elif args.action == "remove" and args.id:
            remove_subject(args.id)
        else:
            print("Недостатньо аргументів або невідома дія")
    elif args.model == "Student":
        if args.action == "create" and args.name and args.group_id:
            create_student(args.name, args.group_id)
        elif args.action == "list":
            list_students()
        elif args.action == "update" and args.id and args.name and args.group_id:
            update_student(args.id, args.name, args.group_id)
        elif args.action == "remove" and args.id:
            remove_student(args.id)
        else:
            print("Недостатньо аргументів або невідома дія")
    elif args.model == "Grade":
        if (
            args.action == "create"
            and args.student_id
            and args.subject_id
            and args.grade
            and args.date
        ):
            create_grade(args.student_id, args.subject_id, args.grade, args.date)
        elif args.action == "list":
            list_grades()
        elif args.action == "update" and args.id and args.grade and args.date:
            update_grade(args.id, args.grade, args.date)
        elif args.action == "remove" and args.id:
            remove_grade(args.id)
        else:
            print("Недостатньо аргументів або невідома дія")
    else:
        print("Невідома модель")


if __name__ == "__main__":
    main()