from src.mathOperation import add,sub,multiply,divide,modulous,pow

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(0,0)==0

def test_sub():
    assert sub(5,3) == 2
    assert sub(0,0) == 0
    assert sub(-1,-1) == 0

def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(-1,1) == -1
    assert multiply(0,5) == 0

def test_divide():
    assert divide(6,3) == 2
    assert divide(5,2) == 2.5
    assert divide(-4,2) == -2

def test_modulous():
    assert modulous(5,2) == 1
    assert modulous(9,3) == 0
    assert modulous(10,7) == 3

def test_pow():
    assert pow(2,3) == 8
    assert pow(5,0) == 1
    assert pow(3,2) == 9