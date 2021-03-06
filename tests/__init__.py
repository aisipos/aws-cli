# Copyright 2012-2013 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import sys
from botocore.hooks import HierarchicalEmitter
from botocore.session import Session
import awscli.clidriver
from awscli.plugin import load_plugins
from awscli.clidriver import CLIDriver
from awscli import EnvironmentVariables


# The unittest module got a significant overhaul
# in 2.7, so if we're in 2.6 we can use the backported
# version unittest2.
if sys.version_info[:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest


class BaseCLIDriverTest(unittest.TestCase):
    """Base unittest that use clidriver.

    This will load all the default plugins as well so it
    will simulate the behavior the user will see.
    """
    def setUp(self):
        emitter = HierarchicalEmitter()
        session = Session(EnvironmentVariables, emitter)
        load_plugins({}, event_hooks=emitter)
        driver = CLIDriver(session=session)
        self.session = session
        self.driver = driver
