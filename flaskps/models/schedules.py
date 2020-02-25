class Schedules(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM schedules"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def allWithData(cls):
        sql = """
            SELECT * FROM schedules s
            INNER JOIN school_year_workshop syw ON s.school_year_workshop_id = syw.id
            INNER JOIN workshops w ON syw.workshop_id = w.id
            INNER JOIN school_years sy ON syw.school_year_id = sy.id
            INNER JOIN cores c ON s.core_id = c.id
            INNER JOIN days d ON s.day_id = d.id
            ORDER by syw.id, d.id
        """
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def resetSchedule(cls, workshop_id, core_id):
        sql = """
            DELETE FROM schedules
            WHERE school_year_workshop_id = %s
            AND core_id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id, core_id))
        return cls.db.commit()

    @classmethod
    def findAssigment(cls, workshop_id, core_id, day, start_time, finish_time):
        sql = """
            SELECT * FROM schedules
            WHERE school_year_workshop_id = %s
            AND core_id = %s
            AND day_id = %s
            AND (
                %s BETWEEN start_time AND finish_time
                OR %s BETWEEN start_time AND finish_time
            )
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id, core_id, day, start_time, finish_time))
        return cursor.fetchone()

    @classmethod
    def setAllDays(cls, workshop_id, core_id, day, start_time, finish_time):
        sql = """
            INSERT INTO schedules
            (school_year_workshop_id, core_id, day_id, start_time, finish_time)
            VALUES (%s, %s, %s, %s, %s)
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (workshop_id, core_id, day, start_time, finish_time))
        return cls.db.commit()

    @classmethod
    def allBySchoolarYear(cls, school_year):
        sql = """
            SELECT * FROM schedules s
            INNER JOIN school_year_workshop syw ON s.school_year_workshop_id = syw.id
            INNER JOIN workshops w ON syw.workshop_id = w.id
            INNER JOIN school_years sy ON syw.school_year_id = sy.id
            INNER JOIN cores c ON s.core_id = c.id
            INNER JOIN days d ON s.day_id = d.id
            WHERE syw.school_year_id = %s
            ORDER by syw.id, d.id
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (school_year))
        return cursor.fetchall()
