import os

def connection_string():
    DATABASE_URL = os.getenv('DATABASE_URL')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PW = os.getenv('DATABASE_PW')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_PORT = os.getenv('DATABASE_PORT')

    return(f'postgresql://{DATABASE_USER}{DATABASE_PW}:@{DATABASE_URL}:{DATABASE_PORT}/{DATABASE_NAME}')