import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text
from sqlalchemy import create_engine

class AWS_DB_Connector:
    def __init__(self):
        self.HOST = "sonia-postgresql-database.cja0w4gsmrar.us-east-1.rds.amazonaws.com"
        self.PORT = 5432
        self.USERNAME = "soniakataria"
        self.PASSWORD = "soniakataria154"
        self.DATABASE = "pinterest_datapipelines_postgresql_db"

    def connect_to_db(self):
        engine = create_engine(f"postgresql+psycopg2://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}")
        # connection = engine.connect()
        # return connection
        return engine

    def execute_create_table_query(self,query_to_be_executed = "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';"):
        engine = self.connect_to_db()
        with engine.connect() as connection:
            query_result = connection.execute(text(query_to_be_executed))
            connection.commit()
            return query_result

    def execute_select_query(self,query_to_be_executed = "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';" ):
        engine = self.connect_to_db()
        with engine.connect() as connection:
            query_result = connection.execute(text(query_to_be_executed))
            return query_result