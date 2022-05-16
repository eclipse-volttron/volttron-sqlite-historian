import gevent
import pytest
from volttron.historian.base_test import HistorianTestInterface
import sqlite3
from pathlib import Path

class SQLiteIntegrationTest(HistorianTestInterface):
    @pytest.fixture
    def historian(self, volttron_instance):
        sqlite_platform = {
            "connection": {
                "type": "sqlite",
                "params": {
                    "database": volttron_instance.volttron_home + 'test.sqlite'
                }
            }
        }
        table_names = {
            "table_prefix": "",
            "data_table": "data",
            "topics_table": "topics",
            "meta_table": "meta"}
        historian_version = ">=4.0.0"
        connection, time_precision = self.setup_sqlite(sqlite_platform["connection"]["params"], table_names, historian_version)
        agent_path = Path(__file__).parents[4]
        historian_uuid = volttron_instance.install_agent(
            vip_identity='platform.historian',
            agent_dir=agent_path,
            config_file=sqlite_platform,
            start=True)
        print("agent id: ", historian_uuid)
        gevent.sleep(1)
        yield "platform.historian", 6
        if volttron_instance.is_running() and volttron_instance.is_agent_running(historian_uuid):
            volttron_instance.stop_agent(historian_uuid)
        volttron_instance.remove_agent(historian_uuid)
        #cleanup_function = globals()["cleanup_" + connection_type]
        # import inspect
        # inspect.getargspec(cleanup_function)[0]
        # cleanup_function(db_connection, None, drop_tables=True)
        gevent.sleep(1)

    def setup_sqlite(self, connection_params, table_names, historian_version):
        print("setup sqlite")
        database_path = connection_params['database']
        print("connecting to sqlite path " + database_path)
        db_connection = sqlite3.connect(database_path)
        print("successfully connected to sqlite")

        # clean_db_rows up any rows from older runs if exists
        cursor = db_connection.cursor()
        for table in table_names.values():
            if table:
                cursor.execute(f"DROP TABLE IF EXISTS {table}")
        db_connection.commit()

        if historian_version == "<4.0.0":
            # test for backward compatibility
            # explicitly create tables based on old schema - i.e separate topics and meta table - so that historian
            # does not create tables with new schema on startup
            print("Setting up for version <4.0.0")
            cursor = db_connection.cursor()
            cursor.execute(
                '''CREATE TABLE ''' + table_names['topics_table'] +
                ''' (topic_id INTEGER PRIMARY KEY,
                     topic_name TEXT NOT NULL,
                     UNIQUE(topic_name))'''
            )
            cursor.execute(
                '''CREATE TABLE ''' + table_names['meta_table'] +
                '''(topic_id INTEGER PRIMARY KEY,
                    metadata TEXT NOT NULL)'''
            )
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS ''' + table_names['data_table'] +
                ''' (ts timestamp NOT NULL,
                     topic_id INTEGER NOT NULL,
                     value_string TEXT NOT NULL,
                     UNIQUE(topic_id, ts))'''
            )
            cursor.execute(
                '''CREATE INDEX IF NOT EXISTS data_idx 
                ON ''' + table_names['data_table'] + ''' (ts ASC)'''
            )
        db_connection.commit()
        return db_connection, 6
