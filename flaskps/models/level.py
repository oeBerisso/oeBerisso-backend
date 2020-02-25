class Level(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM levels"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def find_level_name(cls, id):
        sql = """
    		SELECT name FROM levels
    		WHERE id = %s
    	"""
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchall()
