class Days(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM days"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def allForSchedule(cls, school_year_workshop, core):
        sql = """
            SELECT * FROM days d
            INNER JOIN schedules s ON d.id = s.day_id
            WHERE s.school_year_workshop_id = %s
            AND s.core_id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (school_year_workshop, core))
        return cursor.fetchall()
