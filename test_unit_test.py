import unit_test
import pytest
import sys


# for skipping any test just run this decorator
@pytest.mark.skipif(sys.version_info > (3, 5), reason="I don't want to run the test now")  # decorator
def test_cal_add():
    total = unit_test.cal_add(5, 6)
    assert total == 11


def test_cal_mul():
    total = unit_test.cal_mul(4, 700)
    assert total == 2800
# to do unit testing go to command prompt and type "python -m pytest"
# and write the test python file starting as test
# for knowing details of the tests type python -m pytest -v
# file name and test name must have test_


# run the test by using name like run the test by using substring
# like run those tests which have multiply on their name


