class Assistance(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM assistance_student_workshop"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def create(cls, school_year_id, workshop_id, student_id, date):
        sql = """
            INSERT INTO assistance_student_workshop
            (school_year_id, workshop_id, student_id, date)
            values (%s, %s, %s, %s)
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (school_year_id, workshop_id, student_id, date))
        return cls.db.commit()

    @classmethod
    def removeAllFrom(cls, school_year_id, workshop_id, date):
        sql = """
            DELETE FROM assistance_student_workshop
            WHERE school_year_id = %s
            AND workshop_id = %s
            AND date = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (school_year_id, workshop_id, date))
        return cls.db.commit()

    @classmethod
    def createAll(cls, school_year_id, workshop_id, date, students):
        sql = """
            INSERT INTO assistance_student_workshop
            (school_year_id, workshop_id, student_id, date)
            VALUES (%s,%s,%s,%s)
        """

        cursor = cls.db.cursor()
        cursor.executemany(
            sql,
            ([[school_year_id, workshop_id, student, date] for student in students]),
        )
        return cls.db.commit()

    @classmethod
    def getAllFromDate(cls, school_year_id, workshop_id, date):
        sql = """
            SELECT * FROM assistance_student_workshop
            WHERE school_year_id = %s
            AND workshop_id = %s
            AND date = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (school_year_id, workshop_id, date))
        return cursor.fetchall()
