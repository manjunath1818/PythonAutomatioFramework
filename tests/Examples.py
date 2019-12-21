import pytest


@pytest.mark.usefixtures("test_setup")
class Example:
    def add(self,x,y):
        return x+y

    def sub(self,x,y):
        return x-y