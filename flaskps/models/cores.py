class Cores(object):

    db = None

    @classmethod
    def all(cls):
        sql = """
            SELECT * FROM cores
        """

        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
