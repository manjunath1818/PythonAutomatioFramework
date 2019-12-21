#CONSTANTS
import inspect
import sys

URL = "https://tvs-dev.operativeone.com/"
USERNAME = "supportops@devfox.com"
PASSWORD = "d3vfox!123"

def whoami():
    return inspect.stack([0][3])

def thisFunctionName():
    """Returns a string with the name of the function it's called from"""
    return sys._getframe(1).f_code.co_name