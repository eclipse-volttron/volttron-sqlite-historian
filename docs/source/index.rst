SQLite Historian
================

This is a VOLTTRON historian agent that stores its data in a sqlite database. It depends on
`volttron-lib-sql-historian <https://pypi.org/project/volttron-lib-sql-historian/>`_ and extends the class
`SQLHistorian <https://github.com/eclipse-volttron/volttron-lib-sql-historian/blob/main/src/historian/sql/historian.py>`_

Configuration
-------------

The following is a minimal configuration file that uses a relative path to the database.

::

 {
    "connection": {
        "type": "sqlite",
        "params": {
            "database": "data/historian.sqlite"
        }
    }
}

All the above parameters are mandatory.

TODO- update SQLHistorian rst, link to that

