import numpy as np


class Workshop(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM workshops"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def allInLines(cls, items_per_line):
        workshops = np.array(cls.all())
        lines = np.ceil(workshops.size / items_per_line)
        return np.split(workshops, lines)

    @classmethod
    def allAssignedToSchollarYear(cls):
        sql = """
            SELECT * FROM school_year_workshop syw
            INNER JOIN workshops w ON syw.workshop_id = w.id
            INNER JOIN school_years sy ON syw.school_year_id = sy.id
        """

        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def removeWorkshopsOfSchollarYear(cls, school_year_id):
        sql = """ 
            DELETE FROM school_year_workshop
            WHERE school_year_id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (school_year_id))
        return cls.db.commit()

    @classmethod
    def assignWorkshopsTo(cls, workshops, school_year_id):
        cls.removeWorkshopsOfSchollarYear(school_year_id)
        sql = """
            INSERT INTO school_year_workshop
            (workshop_id, school_year_id)
            VALUES (%s, %s)
        """
        cursor = cls.db.cursor()
        cursor.executemany(
            sql, ([[workshop, school_year_id] for workshop in workshops])
        )
        return cls.db.commit()

    @classmethod
    def getFromSchoolYear(cls, school_year_id):
        sql = """
            SELECT * FROM workshops w
            INNER JOIN school_year_workshop syw ON w.id = syw.workshop_id
            WHERE syw.school_year_id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (school_year_id))
        return cursor.fetchall()

    @classmethod
    def getSchollarYears(cls, workshop_id):
        sql = """
            SELECT * FROM school_years sy
            INNER JOIN school_year_workshop sw ON sy.id = sw.school_year_id
            INNER JOIN workshops w ON sw.workshop_id = w.id
            WHERE w.id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id))
        return cursor.fetchall()

    @classmethod
    def getData(cls, workshop_id):
        sql = """
            SELECT * FROM workshops
            WHERE id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id))
        return cursor.fetchone()

    @classmethod
    def getAssignedTeachers(cls, workshop_id):
        sql = """
            SELECT * FROM teachers t
            INNER JOIN teacher_responsable_workshop tw ON  t.id = tw.teacher_id
            INNER JOIN school_year_workshop sw ON tw.workshop_id = sw.workshop_id
            WHERE tw.workshop_id = %s
            GROUP BY t.id
            ORDER BY sw.school_year_id
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id))
        return cursor.fetchall()

    @classmethod
    def getNotAssignedTeachers(cls, workshop_id):
        sql = """
            SELECT * FROM teachers t
            INNER JOIN teacher_responsable_workshop tw ON  t.id != tw.teacher_id
            WHERE tw.workshop_id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id))
        return cursor.fetchall()

    @classmethod
    def isAssigned(cls, workshop_id, schoolar_year_id, teacher_id):
        sql = """
            SELECT * FROM teacher_responsable_workshop
            WHERE teacher_id = %s
            AND school_year_id = %s
            AND workshop_id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (teacher_id, schoolar_year_id, workshop_id))
        return cursor.fetchall()

    @classmethod
    def getTeachersFrom(cls, workshop_id, school_year_id):
        sql = """
            SELECT t.id FROM teachers t
            INNER JOIN teacher_responsable_workshop tw ON t.id = tw.teacher_id
            WHERE tw.workshop_id = %s
            AND tw.school_year_id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id, school_year_id))
        return cursor.fetchall()

    @classmethod
    def removeTeachers(cls, workshop_id, schoolar_year_id):
        sql = """
            DELETE FROM teacher_responsable_workshop
            WHERE workshop_id = %s
            AND school_year_id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id, schoolar_year_id))
        return cls.db.commit()

    @classmethod
    def allInSchoolYear(cls, workshop_id, school_year_id):
        sql = """
            SELECT * FROM school_year_workshop
            WHERE workshop_id = %s
            AND school_year_id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id, school_year_id))
        return cursor.fetchall()

    @classmethod
    def isInSchoolYear(cls, workshop_id):
        sql = """
            SELECT * FROM school_year_workshop
            WHERE workshop_id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id))
        return cursor.fetchall()

    @classmethod
    def delete_students_for(cls, workshop_id, school_year_id):
        sql = """
            DELETE FROM student_workshop
            WHERE workshop_id = %s
            AND school_year_id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id, school_year_id))
        return cls.db.commit()

    @classmethod
    def assign_students_to(cls, workshop_id, school_year_id, students):
        sql = """
            INSERT INTO student_workshop
            (workshop_id, school_year_id, student_id)
            VALUES (%s, %s, %s)
        """

        cursor = cls.db.cursor()
        cursor.executemany(
            sql,
            ([[workshop_id, school_year_id, student_id] for student_id in students]),
        )
        return cls.db.commit()
