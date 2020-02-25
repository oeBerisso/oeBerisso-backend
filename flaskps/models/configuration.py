class Configuration(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM configuration"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return {i["field"]: i for i in cursor.fetchall()}

    @classmethod
    def get(cls, conf):
        sql = """
            SELECT value FROM configuration where field = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (conf))
        return cursor.fetchone()["value"]

    @classmethod
    def update(cls, field, value):
        sql = """ 
            INSERT INTO 
            configuration (field, value)
            VALUES(%s, %s)
            ON DUPLICATE KEY
                UPDATE value=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (field, value, value))
        return cls.db.commit()

    @classmethod
    def updateAll(cls, fields):
        for conf in list(fields.keys()):
            res = cls.update(conf, fields[conf])
        return res

    @classmethod
    def service_unavailable(cls):
        status = cls.get("maintenance")
        return int(status)
