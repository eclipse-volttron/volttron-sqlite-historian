# -*- coding: utf-8 -*- {{{
# ===----------------------------------------------------------------------===
#
#                 Installable Component of Eclipse VOLTTRON
#
# ===----------------------------------------------------------------------===
#
# Copyright 2022 Battelle Memorial Institute
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# ===----------------------------------------------------------------------===
# }}}

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

