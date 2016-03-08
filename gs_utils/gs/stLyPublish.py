from geoserver.catalog import Catalog


def connectCatalog(ip,user,password):
    ''' Return a catalog from geoserver REST API'''
    # example  Catalog("http://192.168.1.41:8080/geoserver/rest",'user', 'password')
    cat = Catalog(ip,user,password)
    return cat

def getDatastore(cat,storeName):
    ''' Return a datastore   from geoserver REST API'''
    # example  Catalog("http://192.168.1.41:8080/geoserver/rest",'user', 'password')
    st = cat.get_store('bluehabitats')
    return st


def publish_feature_store(layersList,storeName,cat,epsg):
    '''Publish all layers from a postgis geoserver store'''
    for layer in layersList:
        ft = cat.publish_featuretype(layer, storeName, epsg, srs=epsg)
        print ft.name
        cat.save(ft)
