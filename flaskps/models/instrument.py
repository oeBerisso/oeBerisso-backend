class Instrument(object):

    db = None

    @classmethod
    def create(cls, data):
        sql = """
            INSERT INTO instruments (name, type_id, photo, alt)
            VALUES (%s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (data["name"], data["type"], data["photo"], data["alt"]))
        cls.db.commit()
        return True

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM instruments
            WHERE name = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (name))

        return cursor.fetchone()

    @classmethod
    def all(cls):
        sql = "SELECT * FROM instruments"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def update(cls, data, id):
        sql = """
            UPDATE instruments 
            SET name = %s, type_id = %s, alt = %s
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (data["name"], data["type"], data["alt"], id))
        cls.db.commit()
        return True

    @classmethod
    def update_with_photo(cls, data, id):
        sql = """
            UPDATE instruments 
            SET name = %s, type_id = %s, photo = %s, alt = %s
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(
            sql, (data["name"], data["type"], data["photo"], data["alt"], id)
        )
        cls.db.commit()
        return True

    @classmethod
    def filter(cls, name, type):
        sql = """
            SELECT * FROM instruments
            WHERE name LIKE %s AND type_id LIKE %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (name + "%", type + "%"))

        return cursor.fetchall()

    @classmethod
    def get_photo_name(cls, id):
        sql = """
            SELECT photo FROM instruments
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))

        return cursor.fetchone()["photo"]

    @classmethod
    def delete_instrument(cls, id):
        sql = """
            DELETE from instruments
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        cls.db.commit()

    @classmethod
    def show_instrument(cls, id):
        sql = """
            SELECT * from instruments
            WHERE id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        return cursor.fetchone()
