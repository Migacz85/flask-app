def test_are_equal(actual,expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected,actual)

def test_not_equal(a,b):
    assert a != b, "Did not expect {0} but got {1}".format(a,b)

def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_item_is_in_list_of_list(session_user, user_list):
        test=False
        for user in user_list:
            if user[0] == session_user:
               test=True
        assert test , "{0} does not contain {1}".format(user_list, session_user)

def test_is_not_in(collection, item):
    assert not item in collection, "{0} does contain {1} and it should not".format(collection, item)

def test_is_between(start, end, x):
    assert x >= start and x <= end, "range is {0} - {1} testing value is {2}".format(start,end, x)

def test_are_equal_when_global_equal(actual,expected, equal):
    global question_number
    question_number=equal
    assert expected == actual, "Expected {0}, got {1}".format(expected,actual)

# collection = [1,2,4,5,2,4,5,6]
# test_is_in(collection, 2)
# test_is_not_in(collection,4)

# test_are_equal(1,2)
# test_is_between(1,10,11)
