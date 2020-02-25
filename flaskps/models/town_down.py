class TownDown(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM town_down"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def find_town_down_name(cls, id):
        sql = """ 
    		SELECT name FROM town_down
    		WHERE id = %s
    	"""
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchall()
