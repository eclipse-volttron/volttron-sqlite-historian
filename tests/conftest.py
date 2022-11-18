import os
from pathlib import Path
import shutil
import sys
import tempfile

import pytest
from volttrontesting.fixtures.volttron_platform_fixtures import volttron_instance


# the following assumes that the testconf.py is in the tests directory.
volttron_src_path = Path(__file__).resolve().parent.parent.joinpath("src")

assert volttron_src_path.exists()

print(sys.path)
if str(volttron_src_path) not in sys.path:
    print(f"Adding source path {volttron_src_path}")
    sys.path.insert(0, str(volttron_src_path))

