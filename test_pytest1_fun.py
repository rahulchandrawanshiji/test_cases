import pytest1
import pytest
'''
@pytest.mark.skip(reason="do not run string and test ")
def test_add():
    assert pytest1.add(7,4) == 11
    assert pytest1.add(7) == 9
    assert pytest1.add(7,7) == 14
    assert pytest1.add(6,4) == 10

#@pytest.mark.number
def test_product():
    assert pytest1.product(5,2) == 10
    assert pytest1.product(6,2) == 12
    assert pytest1.product(5,5) == 25
    assert pytest1.product(5,6) == 30

#@pytest.mark.string
def test_add_string():
    result = pytest1.add("hello","world")
    assert result == "helloworld"
    assert type(result) is str
    assert "heldo" not in result

#@pytest.mark.string
def test_product_string():
    assert pytest1.product("hello",3) == "hellohellohello"
    result = pytest1.product("hello")
    assert result == "hellohello"
    assert type(result) is str
    assert "hello" in result '''


'''@pytest.mark.parametrize("num1,num2,result",
                         [
                           (7,3,10),
                           ("hello","world","helloworld")

                        ]
                         )
def test_add(num1,num2,result):
    assert pytest1.add(num1,num2) == result
'''

from pytest1 import studentDB
db = None

def setup_module(module):
    print("======================setup============")
    global db
    db = studentDB()
    db.connect('data.json')

def teardown_module(module):
    print("=================tear down ===========")
    db.close()

def test_scott_data():
    scott_data = db.get_data('scott')
    assert scott_data['id'] == 1

    mark_data = db.get_data('mark')
    assert mark_data['id'] == 2

def test_mark_data():
    ''' db = studentDB()
    db.connect('data.json')'''
    mark_data = db.get_data('mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'mark'
    assert mark_data['result'] == 'fail'


