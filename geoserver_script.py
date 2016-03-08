from geoserver.catalog import Catalog


def connectCatalog(ip,user,password):
    ''' Return a catalog from geoserver REST API'''
    # example  Catalog("http://192.168.1.41:8080/geoserver/rest",'user', 'password')
    return cat = Catalog(ip,user,password)

def publish_feature_store(featureNameList,storeName,cat,epsg):
    '''Publish all layers from a postgis geoserver store'''
    ds = cat.get_store(store)
    for featureName in featureNameList:
        ft = cat.publish_featuretype(featureName, ds, epsg, srs=epsg)
        print ft.name
        cat.save(ft)
