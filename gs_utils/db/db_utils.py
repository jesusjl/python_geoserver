import psycopg2


def dbConnection(dbName,dbUser,dbHost,dbPass,dbPort):
    try:
        conn = psycopg2.connect(dbname=dbName, user=dbUser, host=dbHost, password=dbPass, port=dbPort)
        return conn
    except:
        print "Unable to connect to the database"

def listLayers(conn, dbscheme):
    arr = []
    cur = conn.cursor()
    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = (%s)
        AND table_type='BASE TABLE'""" , (dbscheme, ))
    rows = cur.fetchall()
    print "\nAppending the result in a list and return...\n"

    [arr.append(row[0]) for row in rows]

    return arr
