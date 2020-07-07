import allure, pytest
class Test_allure:
    def setup(self):
        pass
    def teardown(self):
        pass

    @allure.testcase('http://www.baidu.com/test_001','test_001')
    def test_001(self):
        assert 1

    @allure.issue('http://www.163.com/test_002')
    def test_002(self):
        assert 0