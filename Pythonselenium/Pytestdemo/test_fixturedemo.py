import pytest

from Pytestdemo.Baseloggerclass import Baseclass


# @pytest.fixture()
# def setup():
#     print("i will be executed first")
#     yield
#     print(" i will be executed last")
#
# def test_fixturedemo1(setup):
#     print("i will be executed second")




# @pytest.mark.usefixtures("dataload")
# class Testexample1:
#
#     def test_editprofile(self, dataload):
#         print(dataload[0])
#         print(dataload[2])

@pytest.mark.usefixtures("dataload")
class Testexample2(Baseclass):

    def test_editprofile(self, dataload):
        log = self.getlogger()
        log.info(dataload[0])
        log.info(dataload[2])
