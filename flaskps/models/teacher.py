class Teacher(object):

    db = None

    @classmethod
    def create(cls, data):
        sql = """
            INSERT INTO teachers (last_name, first_name, birth_date, location_id, home, gender_id, document_type_id, number, phone)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(
            sql,
            (
                data["last_name"],
                data["first_name"],
                data["birth_date"],
                data["location"],
                data["home"],
                data["gender"],
                data["document_type"],
                data["number"],
                data["phone"],
            ),
        )
        cls.db.commit()
        return True

    @classmethod
    def find_by_dni(cls, number):
        sql = """
            SELECT * FROM teachers
            WHERE number = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (number))

        return cursor.fetchone()

    @classmethod
    def all(cls):
        sql = "SELECT * FROM teachers"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def update(cls, data, id):
        sql = """
            UPDATE teachers 
            SET last_name = %s, first_name = %s, birth_date = %s, location_id = %s, home = %s, gender_id = %s, document_type_id = %s, number = %s, phone = %s
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
                data["home"],
                data["gender"],
                data["document_type"],
                data["number"],
                data["phone"],
                id,
            ),
        )
        cls.db.commit()
        return True

    @classmethod
    def filter(cls, dni, name):
        sql = """
            SELECT * FROM teachers
            WHERE number LIKE %s AND (first_name LIKE %s OR last_name LIKE %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (dni + "%", name + "%", name + "%"))

        return cursor.fetchall()

    @classmethod
    def delete_teacher(cls, id):
        sql = """
            DELETE from teachers
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        cls.db.commit()

    @classmethod
    def assign_workshop(cls, teachers_id, workshop_id, schoolar_year_id):
        sql = """
            INSERT into teacher_responsable_workshop
            (teacher_id, workshop_id, school_year_id)
            VALUES (%s, %s, %s)
        """

        cursor = cls.db.cursor()
        cursor.executemany(
            sql, ([[id, workshop_id, schoolar_year_id] for id in teachers_id])
        )
        return cls.db.commit()

    @classmethod
    def show_teacher(cls, id):
        sql = """
            SELECT * from teachers
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchone()
