import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot_mentors1.sqlite3')
    cursor = db.cursor()

    if db:
        print('База данных подключена!')

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(ID INTEGER PRIMARY KEY, name TEXT,"
               "direction TEXT, ega INTEGER, groupp TEXT,"
               "datas INTEGER)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES "
                       "(?, ?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_list_mentors(message):
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()


async def sql_command_find_id_mentors(user_id):
    return cursor.execute("SELECT * FROM mentors WHERE id = ?", (user_id,)).fetchall()


async def sql_command_find_name_mentors(user_id):
    return cursor.execute("SELECT * FROM mentors WHERE name = ?", (user_id,)).fetchall()


async def sql_command_find_direction_mentors(user_id):
    return cursor.execute("SELECT * FROM mentors WHERE direction = ?", (user_id,)).fetchall()


async def sql_command_find_age_mentors(user_id):
    return cursor.execute("SELECT * FROM mentors WHERE ega = ?", (user_id,)).fetchall()


async def sql_command_find_group_mentors(user_id):
    return cursor.execute("SELECT * FROM mentors WHERE groupp = ?", (user_id,)).fetchall()