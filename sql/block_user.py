import sqlite3


def block_user(data):
    int(data)
    with sqlite3.connect('city25bot.db') as db:
        cursor = db.cursor()
        # cursor.execute("DROP TABLE IF EXISTS block_users")
        cursor.execute("""CREATE TABLE IF NOT EXISTS block_users(
        user_id INT)""")

        cursor.execute("SELECT * FROM block_users")
        users = [i[0] for i in cursor.fetchall()]
        if data not in users:
            cursor.execute('''INSERT INTO block_users (user_id) VALUES (?)''', (data,))
