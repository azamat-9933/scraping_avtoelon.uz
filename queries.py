import sqlite3


def insert_data_avto(model, company_name, price, description, region, date, link):
    database = sqlite3.connect("avto.db")
    cursor = database.cursor()
    cursor.execute("""
                INSERT INTO avto(avto_model, avto_company, avto_price, avto_description, avto_region, avto_data, avto_link)
                VALUES (?,?,?,?,?,?,?);
            """, (model, company_name, price, description, region, date, link))

    database.commit()
    database.close()
