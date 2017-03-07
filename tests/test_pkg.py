from pkg.mod import adder

def test_add2():
    assert 2+2 == 4

def test_adder():
    assert adder(1,2) == 3
