import pytest
# @pytest.mark.xfail
def test_firstprogram():
    msg = "Hello"
    assert msg == "Hi", "test failed beacuse strings do not match"

# @pytest.mark.smoke
# @pytest.mark.skip
def test_number():
    a = 4
    b = 6
    assert a + 2 == b, "test failed because sum didnt match"
