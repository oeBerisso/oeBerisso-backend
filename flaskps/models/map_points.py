class MapPoints(object):

    db = None

    @classmethod
    def all(cls):
        sql = """
            SELECT * FROM map_points
        """

        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
