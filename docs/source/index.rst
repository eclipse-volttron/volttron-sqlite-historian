SQLite Historian
================

This is a VOLTTRON historian agent that stores its data in a sqlite database. It depends on
`volttron-lib-sql-historian <https://pypi.org/project/volttron-lib-sql-historian/>`_ and extends the class
`SQLHistorian <https://github.com/eclipse-volttron/volttron-lib-sql-historian/blob/main/src/historian/sql/historian.py#:~:text=class%20SQLHistorian>`_

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

Optional Configuration
----------------------

In addition to the above configuration, SQLite Historian can be configured using all the available configurations
exposed by the SQLHistorian and BaseHistorian. Please refer to
:ref:`SQL Historian Configurations <SQL-Historian-Configurations>` and
:ref:`Base Historian Configurations <Base-Historian-Configurations>`


