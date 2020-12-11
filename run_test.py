import unittest
import test_register
from HTMLTestRunner import HTMLTestRunner

# 第一步，创建一个测试套件
# suite = unittest.TestSuite()

# 第二步：将测试用例，加载到测试套件中
# 方式1，添加单条测试用例
# case = test_register.TestRegister("test_register_success")	# 创建一个用例对象，注意：通过用例类去创建测试用例对象的时候，需要传入用例的方法名（字符串类型）
# suite.addTest(case)	# 添加用例到测试套件中

# 方式2，添加多条测试用例
# case1 = test_register.TestRegister("test_register_success")
# case2 = test_register.TestRegister("test_username_isnull")
# suite.addTest([case1, case2])	# 添加用例到测试套件中

# 方式3，添加一个测试用例类
# loader = unittest.TestLoader()	# 创建一个加载对象
# suite.addTest(loader.loadTestsFromTestCase(test_register.TestRegister))

# 方式4，添加一个模块
# loader = unittest.TestLoader()	# 创建一个加载对象
# suite.addTest(loader.loadTestsFromModule(test_register))

# 方式5，指定测试用例的所在的目录路径，进行加载
# loader = unittest.TestLoader()
# suite.addTest(loader.discover(r"d:\learn\python"))
# 创建测试套件
suite = unittest.TestSuite()

# 通过模块加载测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_register))

# 创建测试运行程序启动器
runner = HTMLTestRunner(stream=open("report.html", "wb"),  # 打开一个报告文件，将句柄传给stream
                        # 报告中显示的测试人员
                        description="注册接口测试报告",        # 报告中显示的描述信息
                        title="自动化测试报告")                 # 报告的标题

# 使用启动器去执行测试套件里的用例
runner.run(suite)
