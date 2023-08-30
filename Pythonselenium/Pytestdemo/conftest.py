import pytest

@pytest.fixture()
def dataload():
    print("user profile is created")
    return ["rahul","shetty","rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","rahul"),("firefox","shetty"),"IA"])
def crossbrowser (request):
    return request.param
