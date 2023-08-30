import pytest



class LoginTestdata:
    testData = [{"username":"standard_user", "password": "secret_sauce"}]


@pytest.fixture(params=LoginTestdata.testData)
def getdata(self,request):
    return request.param