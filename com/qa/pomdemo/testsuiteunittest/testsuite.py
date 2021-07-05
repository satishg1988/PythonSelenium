import unittest
import HtmlTestRunner
from com.qa.pomdemo.tests.loginTC import Logintest


class TestSuite:
    tc1 = unittest.TestLoader().loadTestsFromTestCase(Logintest)

    smoketest = unittest.TestSuite([tc1])
    unittest.TextTestRunner(verbosity=2).run(smoketest)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/PycharmProjects/PythonSelenium/reports'))
