# Для создания БД, для организации БД, создания таблиц
import sqlite3

# Подключится к БД, создать БД
database_avto = sqlite3.connect("avto.db")

# Объявить менеджера ---
cursor = database_avto.cursor()


def create_table_avto():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS avto(
            avto_id INTEGER PRIMARY KEY AUTOINCREMENT,
            avto_model VARCHAR(20),
            avto_company VARCHAR(20),
            avto_price TEXT,
            avto_description TEXT,
            avto_region TEXT,
            avto_data TEXT,
            avto_link TEXT
        )
    """)

# create_table_avto()

# commit --- Сохранить изменения в БД
database_avto.commit()
# close --- Отключится от БД
database_avto.close()