#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pytest
import allure

from python_calculator.calculator import Calculator


@allure.severity(allure.severity_level.TRIVIAL)
@allure.feature("计算器功能测试")
class TestCalc:
    @allure.story("登录成功")
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [100, 1, 101], [0.1, 0.1, 0.2], [-1, -1, -2],
        [1, 0, 1]
    ], ids=['int_case', 'bignum_case', 'float_case', 'minus_case', 'zero_case'])
    # def test_add(self, a, b, expect):
    #     result = self.calc.add(a, b)
    #     assert result == expect
    def test_float_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', [
        [1, 2, -1], [2, 1, 1], [-1, -2, 1], [-2, -1, -1], [1, -2, 3], [2, -1, 3], [-1, 2, -3], [-2, 1, -3],
        [0.3, 0.1, 0.2], [100, 99, 1]
    ], ids=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', [
        [1, 2, 0.5], [2, 1, 2], [-1, -2, 0.5], [-2, -1, 2], [1, -2, -0.5], [2, -1, -2], [-1, 2, -0.5], [-2, 1, -2],
        [0.3, 0.1, 3], [10, 0, True]
    ], ids=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    @allure.severity(allure.severity_level.NORMAL)
    def test_div(self, a, b, expect):
        # try:
        #     result = self.calc.div(a, b)
        #     assert result == expect
        # except ZeroDivisionError:
        #     print("除数为0")
        with pytest.raises(ZeroDivisionError):
            result = self.calc.div(a, b)
            assert result == expect
