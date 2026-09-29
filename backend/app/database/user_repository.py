from app.database.connection import get_connection


def create_user(name: str, email: str, password_hash: str):
    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO users (name, email, password_hash)
        VALUES (?, ?, ?)
        """,
        (name, email, password_hash),
    )

    connection.commit()

    user_id = cursor.lastrowid

    connection.close()

    return user_id


def get_user_by_email(email: str):
    connection = get_connection()

    user = connection.execute(
        """
        SELECT id, name, email, password_hash
        FROM users
        WHERE email = ?
        """,
        (email,),
    ).fetchone()

    connection.close()

    return user

def get_user_by_id(user_id: int):
    connection = get_connection()

    user = connection.execute(
        """
        SELECT id, name, email
        FROM users
        WHERE id = ?
        """,
        (user_id,),
    ).fetchone()

    connection.close()

    return user


def update_user_password(user_id: int, password_hash: str):
    connection = get_connection()

    connection.execute(
        """
        UPDATE users
        SET password_hash = ?
        WHERE id = ?
        """,
        (password_hash, user_id),
    )

    connection.commit()
    connection.close()    