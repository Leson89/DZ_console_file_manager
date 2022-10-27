import mock
import builtins
from main_manager.bank import finance
from main_manager.file_manager import actions


"""
Тестирование счет
"""
def test_billing():
    with mock.patch.object(builtins, 'input', lambda _: '19'):
        assert finance.billinng() == 19
def test_buy_sum():
    with mock.patch.object(builtins, 'input', lambda _: '50'):
        assert finance.buy_sum() == 50

"""
Тестирование файловый менеджер
"""
def test_new_file():
    with mock.patch.object(builtins, 'input', lambda _: '19.txt'):
        open('19.txt', 'w')