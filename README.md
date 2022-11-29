[![Run Pytests](https://github.com/eclipse-volttron/volttron-sqlite-historian/actions/workflows/run-test.yml/badge.svg)](https://github.com/eclipse-volttron/volttron-sqlite-historian/actions/workflows/run-test.yml)
[![pypi version](https://img.shields.io/pypi/v/volttron-sqlite-historian.svg)](https://pypi.org/project/volttron-sqlite-historian/)

VOLTTRON historian agent that stores data into a SQLite database


## Requirements

 - Python >= 3.8

## Installation

1. Create and activate a virtual environment.

   ```shell
    python -m venv env
    source env/bin/activate
    ```

2. Installing volttron-sqlite-historian requires a running volttron instance.

    ```shell
    pip install volttron
    
    # Start platform with output going to volttron.log
    volttron -vv -l volttron.log &
    ```

3. Create a agent configuration file 
   SQLite historian supports two parameters
    
    - connection -  This is a mandatory parameter with type indicating the type of sql historian (i.e. sqlite) and params 
                    containing the path the database file.
    
    - tables_def - Optional parameter to provide custom table names for topics, data, and metadata.
    
    The configuration can be in a json or yaml formatted file.

    Yaml Format:

    ```yaml
    connection:
      # type should be sqlite
      type: sqlite
      params:
        # Relative to the agents data directory
        database: "data/historian.sqlite"
    
      tables_def:
        # prefix for data, topics, and (in version < 4.0.0 metadata tables)
        # default is ""
        table_prefix: ""
        # table name for time series data. default "data"
        data_table: data
        # table name for list of topics. default "topics"
        topics_table: topics
    ```
    
4. Install and start the volttron-sqlite-historian.

    ```shell
    vctl install volttron-sqlite-historian --agent-config <path to configuration> --start
    ```

5. View the status of the installed agent

    ```shell
    vctl status
    ```

## Development

Please see the following for contributing guidelines [contributing](https://github.com/eclipse-volttron/volttron-core/blob/develop/CONTRIBUTING.md).

Please see the following helpful guide about [developing modular VOLTTRON agents](https://github.com/eclipse-volttron/volttron-core/blob/develop/DEVELOPING_ON_MODULAR.md)

# Disclaimer Notice

This material was prepared as an account of work sponsored by an agency of the
United States Government.  Neither the United States Government nor the United
States Department of Energy, nor Battelle, nor any of their employees, nor any
jurisdiction or organization that has cooperated in the development of these
materials, makes any warranty, express or implied, or assumes any legal
liability or responsibility for the accuracy, completeness, or usefulness or any
information, apparatus, product, software, or process disclosed, or represents
that its use would not infringe privately owned rights.

Reference herein to any specific commercial product, process, or service by
trade name, trademark, manufacturer, or otherwise does not necessarily
constitute or imply its endorsement, recommendation, or favoring by the United
States Government or any agency thereof, or Battelle Memorial Institute. The
views and opinions of authors expressed herein do not necessarily state or
reflect those of the United States Government or any agency thereof.
