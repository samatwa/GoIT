from sqlalchemy import func, desc, create_engine
from sqlalchemy.orm import Session, sessionmaker
from models import Student, Grade, Subject, Teacher, Group
import os
from dotenv import load_dotenv


def select_1(session: Session):
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    return (
        session.query(
            Student.name, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .join(Grade)
        .group_by(Student.id, Student.name)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )


def select_2(session: Session, subject_id: int):
    """Знайти студента із найвищим середнім балом з певного предмета."""
    return (
        session.query(
            Student.name, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id, Student.name)
        .order_by(desc("avg_grade"))
        .first()
    )


def select_3(session: Session, subject_id: int):
    """Середній бал у групах з певного предмета."""
    return (
        session.query(
            Group.name, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .select_from(Group)
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id, Group.name)
        .all()
    )


def select_4(session: Session):
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    return session.query(
        func.round(func.avg(Grade.grade), 2).label("avg_grade")
    ).scalar()


def select_5(session: Session, teacher_id: int):
    """Знайти які курси читає певний викладач."""
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()


def select_6(session: Session, group_id: int):
    """Знайти список студентів у певній групі."""
    return session.query(Student.name).filter(Student.group_id == group_id).all()


def select_7(session: Session, group_id: int, subject_id: int):
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    return (
        session.query(Student.name, Grade.grade, Grade.date)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .order_by(Student.name, Grade.date)
        .all()
    )


def select_8(session: Session, teacher_id: int):
    """Середній бал, який ставить певний викладач зі своїх предметів."""
    return (
        session.query(
            Teacher.name, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .join(Subject, Subject.teacher_id == Teacher.id)
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Teacher.id == teacher_id)
        .group_by(Teacher.id, Teacher.name)  # Додав Teacher.id для кращої практики
        .first()
    )


def select_9(session: Session, student_id: int):
    """Знайти список курсів, які відвідує певний студент."""
    return (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )


def select_10(session: Session, student_id: int, teacher_id: int):
    """Список курсів, які певному студенту читає певний викладач."""
    return (
        session.query(Subject.name)
        .select_from(Subject)
        .join(Grade, Grade.subject_id == Subject.id)
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
        .distinct()
        .all()
    )


# Додаткові запити підвищеної складності
def select_extra_1(session: Session, teacher_id: int, student_id: int):
    """Середній бал, який певний викладач ставить певному студентові."""
    return (
        session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade"))
        .join(Subject)
        .filter(Subject.teacher_id == teacher_id, Grade.student_id == student_id)
        .scalar()
    )


def select_extra_2(session: Session, group_id: int, subject_id: int):
    """Оцінки студентів у певній групі з певного предмета на останньому занятті."""
    # Знаходимо останню дату для цієї групи та предмета
    subquery = (
        session.query(func.max(Grade.date))
        .join(Student)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .scalar()
    )

    # Отримуємо всі оцінки на цю дату
    return (
        session.query(Student.name, Grade.grade, Grade.date)
        .join(Grade)
        .filter(
            Student.group_id == group_id,
            Grade.subject_id == subject_id,
            Grade.date == subquery,
        )
        .order_by(Student.name)
        .all()
    )


def run_tests():
    """Функція для запуску всіх тестів."""
    # Підключення до бази даних
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        print("DATABASE_URL не знайдено в .env файлі")
        return

    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Отримуємо тестові дані
        subject = session.query(Subject).first()
        teacher = session.query(Teacher).first()
        group = session.query(Group).first()
        student_test = session.query(Student).first()

        # Тестування запитів
        print("1. Топ 5 студентів за середнім балом:")
        for student in select_1(session):
            print(f"   {student.name}: {student.avg_grade}")

        print(f"\n2. Студент з найвищим середнім балом з предмета '{subject.name}':")
        student = select_2(session, subject.id)
        if student:
            print(f"   {student.name}: {student.avg_grade}")
        else:
            print("   Немає даних")

        print(f"\n3. Середній бал у групах з предмета '{subject.name}':")
        for group_result in select_3(session, subject.id):
            print(f"   {group_result.name}: {group_result.avg_grade}")

        print("\n4. Середній бал на потоці:")
        avg_grade = select_4(session)
        print(f"   {avg_grade}")

        print(f"\n5. Предмети, які читає викладач '{teacher.name}':")
        for subject_result in select_5(session, teacher.id):
            print(f"   {subject_result.name}")

        print(f"\n6. Студенти в групі '{group.name}':")
        for student_result in select_6(session, group.id):
            print(f"   {student_result.name}")

        print(
            f"\n7. Оцінки студентів у групі '{group.name}' з предмета '{subject.name}':"
        )
        for grade in select_7(session, group.id, subject.id):
            print(f"   {grade.name}: {grade.grade} ({grade.date.date()})")

        print(f"\n8. Середній бал, який ставить викладач '{teacher.name}':")
        result = select_8(session, teacher.id)
        if result:
            print(f"   {result.name}: {result.avg_grade}")
        else:
            print("   Немає даних")

        print(f"\n9. Список курсів, які відвідує студент '{student_test.name}':")
        for subject_result in select_9(session, student_test.id):
            print(f"   {subject_result.name}")

        print(
            f"\n10. Список курсів, які студенту '{student_test.name}' читає викладач '{teacher.name}':"
        )
        for subject_result in select_10(session, student_test.id, teacher.id):
            print(f"   {subject_result.name}")

        print("\n" + "=" * 50)
        print("ДОДАТКОВІ ЗАПИТИ:")
        print("=" * 50)

        print(
            f"\n1. Середній бал, який викладач '{teacher.name}' ставить студенту '{student_test.name}':"
        )
        avg_grade = select_extra_1(session, teacher.id, student_test.id)
        if avg_grade:
            print(f"   {avg_grade}")
        else:
            print("   Немає даних")

        print(
            f"\n2. Оцінки студентів у групі '{group.name}' з предмета '{subject.name}' на останньому занятті:"
        )
        for grade in select_extra_2(session, group.id, subject.id):
            print(f"   {grade.name}: {grade.grade} ({grade.date.date()})")

        print("\nТестування завершено успішно!")

    except Exception as e:
        print(f"Помилка: {e}")
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    run_tests()
