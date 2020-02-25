class SchoolYear(object):

    db = None

    @classmethod
    def all(cls):
        sql = """
            SELECT * FROM school_years
        """

        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def getData(cls, school_year_id):
        sql = """
            SELECT * FROM school_years
            WHERE id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (school_year_id))
        return cursor.fetchone()

    @classmethod
    def create(cls, semester, start_date, ending_date):
        sql = """
            INSERT INTO school_years
            (semester, start_date, ending_date)
            VALUES (%s, %s, %s)
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (semester, start_date, ending_date))
        cls.db.commit()

    @classmethod
    def validateInterval(cls, start, finish):
        sql = """
            SELECT count(*) FROM school_years sy
            WHERE %s BETWEEN sy.start_date AND sy.ending_date
            OR %s BETWEEN sy.start_date AND sy.ending_date 
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (start, finish))
        return bool(cursor.fetchone()["count(*)"])

    @classmethod
    def assignedToWorkshop(cls, workshop_id):
        sql = """
            SELECT * FROM school_years s
            INNER JOIN school_year_workshop sw ON s.id = sw.school_year_id
            WHERE sw.workshop_id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id))
        return cursor.fetchall()

    @classmethod
    def allWithWorkshop(cls):
        sql = """
            SELECT DISTINCT(s.id), s.start_date, s.ending_date, s.semester
            FROM school_years s
            INNER JOIN school_year_workshop sw ON s.id = sw.school_year_id
        """
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def search_date(cls):
        sql = """
            SELECT * FROM school_years sy
            WHERE NOW() BETWEEN sy.start_date AND sy.ending_date
        """

        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchone()
