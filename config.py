class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'ondo'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'dakar_dem_dikk'
    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
