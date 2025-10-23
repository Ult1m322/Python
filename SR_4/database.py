import sqlite3


class Database:

    def __init__(self, db_name="students.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                surname TEXT,
                name TEXT,
                patronymic TEXT,
                group_number TEXT,
                birth_date TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS real_performance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                subject TEXT,
                grade REAL,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS desired_performance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                subject TEXT,
                desired_grade REAL,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        ''')

        self.connection.commit()

    def insert_student(self, student):
        self.cursor.execute('''
            INSERT INTO students (surname, name, patronymic, group_number, birth_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (student.get_surname(), student.get_name(), student.get_patronymic(),
              student.get_group_number(), student.get_birth_date()))
        self.connection.commit()
        return self.cursor.lastrowid

    def update_student(self, student_id, student):
        self.cursor.execute('''
            UPDATE students
            SET surname=?, name=?, patronymic=?, group_number=?, birth_date=?
            WHERE id=?
        ''', (student.get_surname(), student.get_name(), student.get_patronymic(),
              student.get_group_number(), student.get_birth_date(), student_id))
        self.connection.commit()

    def delete_student(self, student_id):
        self.cursor.execute('DELETE FROM real_performance WHERE student_id=?', (student_id,))
        self.cursor.execute('DELETE FROM desired_performance WHERE student_id=?', (student_id,))
        self.cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
        self.connection.commit()

    def insert_performance(self, student_id, subjects, grades, table_name):
        self.cursor.execute(f'DELETE FROM {table_name} WHERE student_id=?', (student_id,))

        grade_column = 'grade' if table_name == 'real_performance' else 'desired_grade'

        for subject, grade in zip(subjects, grades):
            self.cursor.execute(f'''
                INSERT INTO {table_name} (student_id, subject, {grade_column})
                VALUES (?, ?, ?)
            ''', (student_id, subject, grade))

        self.connection.commit()

    def get_student(self, student_id):
        self.cursor.execute('SELECT * FROM students WHERE id=?', (student_id,))
        return self.cursor.fetchone()

    def get_performance(self, student_id, table_name):
        grade_column = 'grade' if table_name == 'real_performance' else 'desired_grade'
        self.cursor.execute(f'SELECT subject, {grade_column} FROM {table_name} WHERE student_id=?',
                            (student_id,))
        rows = self.cursor.fetchall()
        subjects = [row[0] for row in rows]
        grades = [row[1] for row in rows]
        return subjects, grades

    def close(self):
        self.connection.close()