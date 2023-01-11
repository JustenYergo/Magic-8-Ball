from responses import Responses as responses
import random

class Magic8(responses):

    def __init__(self, responses):
        responses.read(self)
        self._responses = responses.read(self)

    def shake(self):
        print('\n')
        print(random.choice(list((self._responses).items())))


