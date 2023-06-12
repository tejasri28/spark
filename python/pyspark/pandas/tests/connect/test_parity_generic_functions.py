#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import unittest

from pyspark.pandas.tests.test_generic_functions import GenericFunctionsTestsMixin
from pyspark.testing.connectutils import ReusedConnectTestCase
from pyspark.testing.pandasutils import PandasOnSparkTestUtils, TestUtils


class GenericFunctionsParityTests(
    GenericFunctionsTestsMixin, TestUtils, PandasOnSparkTestUtils, ReusedConnectTestCase
):
    @unittest.skip("TODO(SPARK-43631): Enable Series.interpolate with Spark Connect.")
    def test_interpolate(self):
        super().test_interpolate()

    @unittest.skip("TODO(SPARK-43645): Enable pyspark.pandas.spark.functions.std in Spark Connect.")
    def test_stat_functions(self):
        super().test_stat_functions()


if __name__ == "__main__":
    from pyspark.pandas.tests.connect.test_parity_generic_functions import *  # noqa: F401

    try:
        import xmlrunner  # type: ignore[import]

        testRunner = xmlrunner.XMLTestRunner(output="target/test-reports", verbosity=2)
    except ImportError:
        testRunner = None
    unittest.main(testRunner=testRunner, verbosity=2)
