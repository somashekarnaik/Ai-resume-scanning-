import sqlite3


DATABASE_NAME = "resume_scanner.db"


def get_connection():

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    connection.row_factory = (
        sqlite3.Row
    )

    return connection


def create_tables():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY
                AUTOINCREMENT,

            name TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL

        )
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resumes (

            id INTEGER PRIMARY KEY
                AUTOINCREMENT,

            user_id INTEGER,

            filename TEXT,

            extracted_text TEXT,

            score REAL

        )
    """)


    connection.commit()

    connection.close()


def create_user(
    name,
    email,
    password
):

    connection = get_connection()

    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users
            (name, email, password)
            VALUES (?, ?, ?)
            """,
            (
                name,
                email,
                password
            )
        )

        connection.commit()

        user_id = cursor.lastrowid

        return user_id

    except sqlite3.IntegrityError:

        return None

    finally:

        connection.close()


def get_user(
    email,
    password
):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email = ?
        AND password = ?
        """,
        (
            email,
            password
        )
    )


    user = cursor.fetchone()

    connection.close()

    return user


def save_resume(
    user_id,
    filename,
    text,
    score
):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO resumes
        (
            user_id,
            filename,
            extracted_text,
            score
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            user_id,
            filename,
            text,
            score
        )
    )


    connection.commit()

    connection.close()