class Student(object):

    db = None

    @classmethod
    def create(cls, data):
        sql = """
            INSERT INTO students (last_name, first_name, birth_date, location_id, level_id, home, gender_id, school_id, document_type_id, number, phone, town_down_id, place_of_birth, responsable)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(
            sql,
            (
                data["last_name"],
                data["first_name"],
                data["birth_date"],
                data["location"],
                data["level"],
                data["home"],
                data["gender"],
                data["school"],
                data["document_type"],
                data["number"],
                data["phone"],
                data["town_down"],
                data["place_of_birth"],
                data["responsable"],
            ),
        )
        cls.db.commit()
        return True

    @classmethod
    def find_by_dni(cls, number):
        sql = """
            SELECT * FROM students
            WHERE number = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (number))

        return cursor.fetchone()

    @classmethod
    def all(cls):
        sql = "SELECT * FROM students"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def filter(cls, dni, name, level, school):
        sql = """
            SELECT * FROM students
            WHERE number LIKE %s AND (first_name LIKE %s OR last_name LIKE %s) AND level_id LIKE %s AND school_id LIKE %s 
        """
        cursor = cls.db.cursor()
        cursor.execute(
            sql, (dni + "%", name + "%", name + "%", level + "%", school + "%")
        )

        return cursor.fetchall()

    @classmethod
    def delete_student(cls, id):
        sql = """
            DELETE from students
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        cls.db.commit()

    @classmethod
    def show_student(cls, id):
        sql = """
            SELECT * from students
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchone()

    @classmethod
    def update(cls, data, id):
        sql = """
            UPDATE students 
            SET last_name = %s, first_name = %s, birth_date = %s, location_id = %s, level_id = %s, home = %s, gender_id = %s, school_id = %s, document_type_id = %s, number = %s, phone = %s, town_down_id = %s, place_of_birth = %s, responsable = %s
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(
            sql,
            (
                data["last_name"],
                data["first_name"],
                data["birth_date"],
                data["location"],
                data["level"],
                data["home"],
                data["gender"],
                data["school"],
                data["document_type"],
                data["number"],
                data["phone"],
                data["town_down"],
                data["place_of_birth"],
                data["responsable"],
                id,
            ),
        )
        cls.db.commit()
        return True

    @classmethod
    def get_id_assigned_to(cls, workshop_id, school_year_id):
        sql = """
            SELECT id FROM students s
            INNER JOIN student_workshop sw ON s.id = sw.student_id
            WHERE sw.workshop_id = %s
            AND sw.school_year_id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id, school_year_id))
        return [student["id"] for student in cursor.fetchall()]

    @classmethod
    def data_get_assigned_to(cls, workshop_id, school_year_id):
        sql = """
            SELECT * FROM students s
            INNER JOIN student_workshop sw ON s.id = sw.student_id
            WHERE sw.workshop_id = %s
            AND sw.school_year_id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id, school_year_id))
        return cursor.fetchall()
