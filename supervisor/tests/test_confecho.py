"""Test suite for supervisor.confecho"""

import unittest

from supervisor import confecho
from supervisor.compat import StringIO


class TopLevelFunctionTests(unittest.TestCase):
    def test_main_writes_data_out_that_looks_like_a_config_file(self):
        sio = StringIO()
        confecho.main(out=sio)

        output = sio.getvalue()
        self.assertTrue("[supervisord]" in output)
