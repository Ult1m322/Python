from student import Student
from performance import RealPerformance, DesiredPerformance
from student_data import StudentData
from database import Database

def main():
    db = Database("students.db")
    db.create_tables()

    student1 = Student("Кішко", "Олексій", "Павлович", "ІСД-32", "2005-10-9")
    real_perf1 = RealPerformance(["ОБДЗ", "python", "Радіотехнології"], [90, 90, 88])
    desired_perf1 = DesiredPerformance(["ОБДЗ", "python", "Радіотехнології"], [98, 95, 95])
    student_data1 = StudentData(student1, real_perf1, desired_perf1)

    student_data1.save_to_db(db)
    print(f"Студент доданий з ID: {student_data1.get_student_id()}")
    print(f"Середній бал: {real_perf1.average_grade():.2f}")

    student2 = Student("Котасов", "Олександр", "Петрович", "ІСД-32", "2006-09-26")
    real_perf2 = RealPerformance(["Вишмат", "python"], [85, 90])
    desired_perf2 = DesiredPerformance(["Вишмат", "python"], [90, 95])
    student_data2 = StudentData(student2, real_perf2, desired_perf2)

    student_data2.save_to_db(db)
    print(f"Студент доданий з ID: {student_data2.get_student_id()}")

    student1.set_group_number("ІСД-31")
    real_perf1.set_grades([92, 88, 90])
    student_data1.update_in_db(db)
    print(f"Дані студента {student_data1.get_student_id()} оновлено")

    loaded = StudentData.load_from_db(db, 1)
    print(f"Завантажено: {loaded.get_student().get_full_name()}")
    print(f"Група: {loaded.get_student().get_group_number()}")
    print(f"Середній бал: {loaded.get_real_performance().average_grade():.2f}")
    print(f"Бажаний бал: {loaded.get_desired_performance().average_grade():.2f}")

    student_data2.delete_from_db(db)
    print(f"Студент видалений")

    db.close()


if __name__ == "__main__":
    main()