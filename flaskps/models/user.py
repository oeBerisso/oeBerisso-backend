from datetime import datetime


class User(object):

    db = None

    @classmethod
    def all(cls):
        sql = "SELECT * FROM users"
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def roles_for_user(cls, id):
        sql = """
            SELECT r.id AS roleid, r.name as rolename
            FROM users AS u LEFT JOIN user_has_role AS ur ON u.id = ur.user_id
            LEFT JOIN roles AS r ON r.id = ur.role_id
            WHERE u.id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))

        return cursor.fetchall()

    @classmethod
    def create(cls, data):
        sql = """
            INSERT INTO users (email, username, password, first_name, last_name)
            VALUES (%s, %s, SHA1(%s), %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(
            sql,
            (
                data["email"],
                data["username"],
                data["password"],
                data["first_name"],
                data["last_name"],
            ),
        )
        cls.db.commit()
        return True

    @classmethod
    def create_from_google(cls, email, password, username, first_name, last_name):
        sql = """
            INSERT INTO users (email, username, password, first_name, last_name, is_social)
            VALUES (%s, %s, sha1(%s), %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(
            sql,
            (
                email,
                username,
                password,
                first_name,
                last_name,
                1,
            ),
        )
        cls.db.commit()
        return True

    @classmethod
    def update(cls, username, name, last_name, email):
        sql = """
            UPDATE users
            SET first_name = %s, last_name = %s, email = %s
            WHERE username = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (name, last_name, email, username))
        cls.db.commit()
        return True

    @classmethod
    def update_password(cls, username, password):
        sql = """
            UPDATE users
            SET password = SHA1(%s)
            WHERE username = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (password, username))
        cls.db.commit()
        return True

    @classmethod
    def filter(cls, username, name, email, active):
        sql = """
            SELECT * FROM users AS u
            WHERE u.email LIKE %s AND u.username LIKE %s AND (u.first_name LIKE %s OR u.last_name LIKE %s) AND u.active LIKE %s
        """
        cursor = cls.db.cursor()
        cursor.execute(
            sql, (email + "%", username + "%", name + "%", name + "%", active + "%")
        )

        return cursor.fetchall()

    @classmethod
    def change_active(cls, active, user_id):
        sql = """
            UPDATE users
            SET active = %s, updated_at = %s
            WHERE id = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (active, datetime.now(), user_id))
        cls.db.commit()

    @classmethod
    def find_by_username_and_pass(cls, username, password):
        sql = """
            SELECT * FROM users AS u
            WHERE u.username = %s AND u.password = SHA1(%s)
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (username, password))

        return cursor.fetchone()

    @classmethod
    def find_by_username(cls, username):
        sql = """
            SELECT * FROM users AS u
            where u.username = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (username))

        return cursor.fetchone()

    @classmethod
    def find_by_email(cls, email):
        sql = """
            SELECT * FROM users AS u
            where u.email = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email))

        return cursor.fetchone()

    @classmethod
    def find_by_username_or_email(cls, username, email):
        sql = """
            SELECT * FROM users AS u
            where u.username = %s OR u.email = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (username, email))

        return cursor.fetchone()

    @classmethod
    def get_roles_from_username(cls, username):
        sql = """
            SELECT name FROM roles r
            INNER JOIN user_has_role ur ON r.id = ur.role_id
            INNER JOIN users u ON ur.user_id = u.id
            WHERE u.username = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (username))

        return cursor.fetchall()

    @classmethod
    def delete_roles(cls, id):
        sql = """
            DELETE from user_has_role
            WHERE user_id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id))
        cls.db.commit()

    @classmethod
    def modify_roles(cls, id, roles):
        sql = """
            INSERT INTO user_has_role (user_id, role_id)
            VALUES (%s, %s)
        """
        cursor = cls.db.cursor()
        for rol in roles:
            cursor.execute(sql, (id, rol[0]))
            cls.db.commit()

    @classmethod
    def is_active(cls, username):
        sql = """
            SELECT active FROM users WHERE username = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (username))

        return int(cursor.fetchone()["active"])
