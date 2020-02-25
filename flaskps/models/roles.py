class Roles(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM roles"
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def getFromUsername(cls, username):
        sql = """
            SELECT r.id FROM roles r
            INNER JOIN user_has_role ur ON r.id = ur.role_id
            INNER JOIN users u ON ur.user_id = u.id
            WHERE u.username = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (username))

        return [i["id"] for i in cursor.fetchall()]

    @classmethod
    def getUserPermissions(cls, username):
        sql = """
            SELECT name FROM permissions p
            INNER JOIN role_has_permission rhp ON p.id = rhp.permission_id
            INNER JOIN user_has_role uhr ON rhp.role_id = uhr.role_id
            INNER JOIN users u ON uhr.user_id = u.id
            WHERE u.username = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (username))

        return [i["name"] for i in cursor.fetchall()]
