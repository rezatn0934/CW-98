import functools
from typing import Callable, Any
from dataclasses import dataclass


@dataclass
class AuthenticationDecorator:
    func: Callable[[Any], Any]

    def __call__(self, request):
        @functools.wraps(self.func)
        def wrapper():
            if 'token' in request['headers']:
                return self.func(request)
            else:
                raise ValueError('Your not Authenticated')
        return wrapper


request = {'headers': {'token': '123456'}}


@AuthenticationDecorator
def test(request):
    print('User is Authenticate')


test(request)()