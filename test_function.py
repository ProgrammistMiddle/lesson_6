from lesson_5 import prime, denominator, max_denominator, \
    sum, find



def test_prime():
    assert prime(51) == 'no_prime'
def test_denominator():
    assert denominator(256) == [1, 2, 4, 8, 16, 32, 64, 128]
def test_max_denominator():
    assert max_denominator(256) == 128
def test_sum():
    assert sum(5)==15
def test_find():
    assert find(256) == [16, 32, 64, 128]
