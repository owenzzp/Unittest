import unittest
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover('.', pattern='test*.py')

test_report = 'test_report.html'

with open(test_report, 'wb') as f:
    runner = HTMLTestRunner(f, title='测试报告', description='当前版本：V1.0')
    runner.run(suite)