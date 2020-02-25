class Gender(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM genders"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def find_gender_name(cls, id):
        sql = """ 
    		SELECT name FROM genders
    		WHERE id = %s
    	"""
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchall()
