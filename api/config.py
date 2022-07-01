class BaseConfig:
    HOST = "0.0.0.0"
    PORT = 5100
    DEBUG = False


class Development(BaseConfig):
    PORT = 5100
    MONGODB_URL = "mongodb://admin:admin@cluster0-shard-00-00.kkv90.mongodb.net:27017,cluster0-shard-00-01.kkv90.mongodb.net:27017,cluster0-shard-00-02.kkv90.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-14i2ks-shard-0&authSource=admin&retryWrites=true&w=majority"
    DEBUG = True


class Testing(BaseConfig):
    MONGODB_URL = "mongodb://admin:admin@cluster0-shard-00-00.kkv90.mongodb.net:27017,cluster0-shard-00-01.kkv90.mongodb.net:27017,cluster0-shard-00-02.kkv90.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-14i2ks-shard-0&authSource=admin&retryWrites=true&w=majority"


class Prod(BaseConfig):
    MONGODB_URL = "mongodb://admin:admin@cluster0-shard-00-00.kkv90.mongodb.net:27017,cluster0-shard-00-01.kkv90.mongodb.net:27017,cluster0-shard-00-02.kkv90.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-14i2ks-shard-0&authSource=admin&retryWrites=true&w=majority"