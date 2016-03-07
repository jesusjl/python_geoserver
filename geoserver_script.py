from geoserver.catalog import Catalog
import psycopg2


def dbConecction(dbname,dbuser,host,dbpass ):

    try:
        conn = psycopg2.connect("dbname=dbname user=dbuser host=host password='dbpass'")
        return conn
    except:
        print "Unable to connect to the database"

def listLayers(conn, dbscheme):
    cur = conn.cursor()
    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema= %s
        AND table_type='BASE TABLE'""" % dbscheme)
    rows = cur.fetchall()
    print "\nShow me the databases:\n"
    for row in rows:
        print "   ", row[0]
    return rows

def connectCatalog(ip,user,password):
    ''' Return a catalog from geoserver REST API'''
    # example  Catalog("http://192.168.1.41:8080/geoserver/rest",'user', 'password')
    return cat = Catalog(ip,user,password)

def publish_feature_store(featureName,storeName,cat,epsg):
    '''Publish all layers from a postgis geoserver store'''
    ds = cat.get_store(store)
    ds = cat.get_stores(store)
    ft = cat.publish_featuretype(featureName, ds, epsg, srs=epsg)
    print ft.name
    cat.save(ft)


def publish_all_features()
    for row in rows:
         publish_feature_store(row,storeName,cat,epsg)

def __init__(self):
    return self.name
