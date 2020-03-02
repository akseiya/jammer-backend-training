import yaml

MONGO_HOST      = "mongo"
MONGO_PORT      =  27017
MONGO_DBNAME    = "eve"
with open('app/eve_schema.yml') as f:
    DOMAIN = yaml.safe_load(f)
