# imports
from demo import Demo


class SetsDemo(Demo):

    # properties
    my_set = {1, 2, 3, 4, 1, 2}

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
        print(' - Sets are mutable! values can be modified!')

        # print set
        print('\ndefinition: mySet = {1, 2, 3, 4, 1, 2}')
        print(self.my_set.__repr__() + ' is a ' + self.my_set.__class__.__name__ + '(no duplicates)')

        # alternate def
        self.my_set = set('hello')
        print('\nalternate definition: self.mySet = set(\'hello\')')
        print(self.my_set.__repr__() + ' is a ' + self.my_set.__class__.__name__ + '(no duplicates & unordered)')

        # mutable so items can be added
        self.my_set.add('c')
        print('\nadding items: self.mySet.add(\'c\')')
        print(self.my_set.__repr__())

        # remove items
        self.my_set.discard('c')
        print('\nremove items: self.mySet.discard(\'c\')')
        print(self.my_set.__repr__())

        # union, intersection & difference
        evens = {0, 2, 4, 6, 8}
        odds = {1, 3, 5, 7, 9}
        primes = {2, 3, 5, 7}
        print('\nevens: ' + evens.__repr__())
        print('odds: ' + odds.__repr__())
        print('primes: ' + primes.__repr__())
        print('\nunion between \'odds\' & \'evens\': ' + odds.union(evens).__repr__())
        print('intersection between \'odds\' & \'primes\': ' + odds.intersection(primes).__repr__())
        print('difference between \'odds\' & \'primes\': ' + odds.difference(primes).__repr__())
        print('symmetric difference between \'odds\' & \'primes\': ' + odds.symmetric_difference(primes).__repr__())

        # add sets to other sets
        evens.update(odds)
        evens.update(primes)
        print('\nadd evens, odds & primes')
        print(evens.__repr__() + ' + ' + odds.__repr__() + ' + ' + primes.__repr__())
        print('= ' + evens.__repr__())