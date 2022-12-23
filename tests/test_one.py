import math
"""
функций filter, map, sorted, а также для функций из библиотеки math: pi, sqrt, pow, hypot.
"""
numbers = [1,2,3,4,5,6,7,8,9,10]
"""
Тест filter на четные числа
"""

def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False


def test_filter_odd_num():
    out_filter = list(filter(filter_odd_num,numbers))
    assert out_filter == [2,4,6,8,10]

"""
Тест map на четные числа
"""
def degree(numbers):
    return numbers ** 2

def test_degree_result():
    result = list(map(degree,numbers))
    assert result == [1,4,9,16,25,36,49,64,81,100]
"""
Тест sorted на четные числа
"""

def function_sort(num):
    return num % 2

def test_sort():
    assert sorted(numbers, key=function_sort) == [2,4,6,8,10,1,3,5,7,9]

"""
Тест pi на четные числа
"""
def test_math_pi():
    assert math.pi == 3.141592653589793

"""
Тест sqrt на четные числа
"""
def test_sqrt():
    assert math.sqrt(4) == 2
    assert math.sqrt(25) == 5
"""
Тест pow на четные числа
"""

def test_math_pow():
    assert math.pow(4, 2) == 16
    assert math.pow(10,4) == 10000
    assert math.pow(5, 3) == 125
"""
Тест hypot на четные числа
"""

def test_math_hypot():
    assert  math.hypot(5,15) == 15.811388300841898
    assert math.hypot(20, 40) == 44.721359549995796