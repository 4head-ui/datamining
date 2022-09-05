import pymysql

def connectx():
    try:
        connection = pymysql.connect(
            host = '127.0.0.1',
            port=3306,
            user='root',
            password='*******',
            database='*******',
            cursorclass=pymysql.cursors.DictCursor

        )
        try:
            with connection.cursor() as cursor:
                insert_query = "SELECT `xvalues` FROM information;"
                cursor.execute(insert_query)
                rows = cursor.fetchall()
                x = []
                for row in rows:
                    for r in row.values():
                        x.append(r)

        finally:
            return x

    except Exception as ex:
        pass


def connecty():
    try:
        connection = pymysql.connect(
            host = '127.0.0.1',
            port=3306,
            user='root',
            password='lesson1run',
            database='grafic',
            cursorclass=pymysql.cursors.DictCursor

        )
        try:
            with connection.cursor() as cursor:
                insert_query = "SELECT `yvalues` FROM information;"
                cursor.execute(insert_query)
                rows = cursor.fetchall()
                y = []
                for row in rows:
                    for r in row.values():
                        y.append(r)


        finally:
            return y




    except Exception as ex:
        pass


