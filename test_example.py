import pytest
import random

# Тесты для встроенных функций len(), sum(), sorted()
@pytest.mark.functionality
def test_len():
    assert len([1, 2, 3]) == 3
    assert len('Aryna') == 5
    assert len('') == 0

@pytest.mark.functionality
def test_sum():
    assert sum([1, 2, 3]) == 6
    assert sum([-1, 1]) == 0
    assert sum([]) == 0  

@pytest.mark.functionality
def test_sorted():
    assert sorted([3, 1, 2]) == [1, 2, 3]
    assert sorted(['b', 'a', 'c']) == ['a', 'b', 'c']
    assert sorted([0]) == [0]

# Фикстура, которая возвращает случайный список из 10 чисел
@pytest.fixture
def random_list():
    return [random.randint(1, 2000) for _ in range(10)]

def test_random_list_len(random_list):
    assert len(random_list) == 10

def test_random_list_sorted(random_list):
    sorted_list = sorted(random_list)
    assert sorted_list == sorted(random_list)

# Проверка на четность и нечетность
@pytest.mark.even
def test_all_even(random_list):
    for num in random_list:
        assert num % 2 == 0, f"{num} is not even"

@pytest.mark.odd
def test_has_one_odd(random_list):
    one_odd_numbers = [num for num in random_list if num % 2 != 0]
    assert len(one_odd_numbers) > 0, "There is no odd number"

