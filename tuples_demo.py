# imports
from demo import Demo


class TuplesDemo(Demo):

    # properties
    my_tuple = ("Max", 28, "Boston")

    # init
    def __int__(self, name):
        # call base class init
        super().__init__(name)

    # methods
    def do_work(self):
        # call base class method
        super().do_work()

        # print info
        print(' - Collection Data Type')
        print(' - Tuples are immutable! values cannot be modified! Therefore more memory efficient than Lists')

        # print my tuple
        x = self.my_tuple.__repr__()
        y = self.my_tuple.__class__.__name__
        print('\n' + x + ' is a ' + y)

        # access tuple elements in a for loop with enumerate
        print('\nprint each element')
        for idx, i in enumerate(self.my_tuple):
            print(idx.__repr__() + ': ' + i.__repr__())

        # check for specific item
        print('\ncheck for \'Max\' in the tuple with \'if statement\'')
        if 'Max' in self.my_tuple:
            print('Yes it exists')