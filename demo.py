# servers as a base class for the rest

class Demo:

    # variables
    name = 'not set'

    # constructor
    def __init__(self, name):
        self.name = name

    # methods
    def do_work(self):
        # print intro
        print('=======================================================================================================')
        print(self.name)
        print('=======================================================================================================')

