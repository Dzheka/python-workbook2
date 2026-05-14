import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host':     os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'calculator_db'),
    'user':     os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', ''),
}


class Database:
    def get_connection(self):
        return psycopg2.connect(**DB_CONFIG)


    def save_calculation(self, expression, result, operation):
        conn = self.get_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO calculations (expression, result, operation)
                VALUES (%s, %s, %s)
                """,
                (expression, result, operation)
            )
            conn.commit()
        conn.close()

    def get_all(self):
        conn = self.get_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "SELECT * FROM calculations ORDER BY created_at DESC"
            )
            rows = cur.fetchall()
        conn.close()
        return rows

    def clear_all(self):
        conn = self.get_connection()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM calculations")
            conn.commit()
        conn.close()


    def get_by_operation(self, operation):
        conn = self.get_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "SELECT * FROM calculations WHERE operation = %s ORDER BY created_at DESC",
                (operation,)
            )
            rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, keyword):
        conn = self.get_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "SELECT * FROM calculations WHERE expression ILIKE %s ORDER BY created_at DESC",
                (f"%{keyword}%",)
            )
            rows = cur.fetchall()
        conn.close()
        return rows


    def get_stats(self):
        conn = self.get_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cur:

            cur.execute("""
                SELECT
                    COUNT(*) AS total_calculations,
                    AVG(result) AS average_result,
                    MAX(result) AS largest_result,
                    MIN(result) AS smallest_result
                FROM calculations
            """)
            stats = cur.fetchone()

            cur.execute("""
                SELECT operation, COUNT(*) AS cnt
                FROM calculations
                GROUP BY operation
                ORDER BY cnt DESC
                LIMIT 1
            """)
            op = cur.fetchone()

            stats['most_used_operation'] = op['operation'] if op else None

        conn.close()
        return stats


    def delete_by_id(self, record_id):
        conn = self.get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM calculations WHERE id = %s RETURNING id",
                (record_id,)
            )
            deleted = cur.fetchone()
            conn.commit()
        conn.close()

        return deleted is not None


    def get_or_create_session(self, session_uuid):
        conn = self.get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id FROM sessions WHERE session_id = %s",
                (session_uuid,)
            )
            row = cur.fetchone()

            if row:
                session_id = row[0]
            else:
                cur.execute(
                    "INSERT INTO sessions (session_id) VALUES (%s) RETURNING id",
                    (session_uuid,)
                )
                session_id = cur.fetchone()[0]
                conn.commit()

        conn.close()
        return session_id

    def get_by_session(self, session_id):
        conn = self.get_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                SELECT * FROM calculations
                WHERE session_id = %s
                ORDER BY created_at DESC
                """,
                (session_id,)
            )
            rows = cur.fetchall()
        conn.close()
        return rows
