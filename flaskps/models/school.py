class School(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM schools"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def find_school_name(cls, id):
        sql = """ 
    		SELECT name FROM schools
    		WHERE id = %s
    	"""
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchall()
