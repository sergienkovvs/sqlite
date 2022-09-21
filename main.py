import sqlite3

try:
    sqlite_connection = sqlite3.connect('chinook.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_select_query = "SELECT UnitPrice, Quantity FROM invoice_items"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    res = 0
    for row in record:
        UnitPrice = row[0]
        Quantity = row[1]
        res += UnitPrice * Quantity
    print(res)


    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
