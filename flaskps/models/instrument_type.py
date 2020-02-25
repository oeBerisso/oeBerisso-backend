class Instrument_type(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM instrument_types"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def find_instrument_type_name(cls, id):
        sql = """ 
    		SELECT name FROM instrument_types
    		WHERE id = %s
    	"""
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchall()
