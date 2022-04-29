# imports
from demo import Demo
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
from itertools import count, cycle, repeat
import operator


# function
def smaller_than_3(x):
    return x < 3


class ItertoolsDemo(Demo):

    # properties

    # init
    def __init__(self, name):
        # call base init
        super().__init__(name)

    # methods
    def do_work(self):
        # call base method
        super().do_work()

        # print info
        print(' - works with iterators only i.e. lists')

        print('\n-----------------------------------------------------------------------------------------------------')
        print('product:')
        print('-----------------------------------------------------------------------------------------------------')
        print(' - cartesian product')

        a = [1, 2]
        b = [3, 4]
        c = [5]
        print('\na = ' + a.__repr__())
        print('b = ' + b.__repr__())
        print('c = ' + c.__repr__())
        print('\nlist(product(a, b)')
        print(list(product(a, b)))
        print('\nlist(product(a, c)')
        print(list(product(a, c)))
        print('\nlist(product(a, c, repeat=2)')
        print(list(product(a, c, repeat=2)))

        print('\n-----------------------------------------------------------------------------------------------------')
        print('permutations:')
        print('-----------------------------------------------------------------------------------------------------')
        print(' - all possible orderings of an input')

        a = [1, 2, 3]
        perm = permutations(a)
        my_permutations = list(perm)
        print('\na = ' + a.__repr__())
        print('\nperm = permutations(a)')
        print(len(my_permutations).__repr__() + ' perms: ' + my_permutations.__repr__())

        perm = permutations(a, 2)
        my_permutations = list(perm)
        print('\nperm = permutations(a, 2) to specify the length of the permutations')
        print(len(my_permutations).__repr__() + ' perms: ' + my_permutations.__repr__())

        print('\n-----------------------------------------------------------------------------------------------------')
        print('combinations & combination_with_replacement:')
        print('-----------------------------------------------------------------------------------------------------')
        print(' - all possible combinations of an input')

        a = [1, 2, 3, 4]
        comb = combinations(a, 2)
        comb_wr = combinations_with_replacement(a, 2)
        my_comb = list(comb)
        my_comb_wr = list(comb_wr)
        print('\na = ' + a.__repr__())
        print('\ncomb = combinations(a, 2) to specify the length of the combos')
        print(len(my_comb).__repr__() + ' combos: ' + my_comb.__repr__())
        print('\ncomb_wr = combinations_with_replacement(a, 2) to specify the length of the combos')
        print(len(my_comb_wr).__repr__() + ' combos: ' + my_comb_wr.__repr__())

        print('\n-----------------------------------------------------------------------------------------------------')
        print('accumulate:')
        print('-----------------------------------------------------------------------------------------------------')
        print(' - all possible combinations of an input')

        b = [10, 20, 30]
        c = [0, 3, 6, 2, 1]
        acc = accumulate(b)
        print('\nb = ' + b.__repr__())
        print('c = ' + c.__repr__())
        print('\nacc = accumulate(b), calculates sums by default')
        print(list(acc))
        acc = accumulate(b, func=operator.sub)
        print('\nacc = accumulate(b, func=operator.sub) for subtraction')
        print(list(acc))
        acc = accumulate(c, func=max)
        print('\nacc = accumulate(c, func=max) for max value')
        print(list(acc))

        print('\n-----------------------------------------------------------------------------------------------------')
        print('groupby:')
        print('-----------------------------------------------------------------------------------------------------')
        print(' - returns keys and groups of an input')

        a = [1, 2, 3, 4]
        group_obj = groupby(a, key=smaller_than_3)
        print('\na = ' + a.__repr__())
        print('\ngroup_obj = groupby(a, key=smaller_than_3) where the key is a function')
        print('KEY, VALUE')
        for key, value in group_obj:
            print(str(key) + ', ' + list(value).__repr__())

        persons = [{'name': 'Tim', 'age': 25}, {'name': 'Lisa', 'age': 25},
                   {'name': 'Joe', 'age': 30}, {'name': 'Susy', 'age': 27}]
        group_obj = groupby(persons, key=lambda x: x['age'])
        print('\ngroup_obj = groupby(persons, key=lambda x: x[\'age\']) where key is a Lamda')
        print('KEY, VALUE')
        for key, value in group_obj:
            print(str(key) + ', ' + list(value).__repr__())

        print('\n-----------------------------------------------------------------------------------------------------')
        print('infinite iterators: count, cycle, repeat')
        print('-----------------------------------------------------------------------------------------------------')
        print(' - infinite loop applications')

        print('\ncount up from 5 infinitely until break is called')
        print('\'for i in count(5):\'')
        for i in count(5):
            print(i)
            if i == 10:
                break

        a = [1, 2, 3]
        print('\na = ' + a.__repr__())
        print('\ncycle through an iterable, until break is called')
        print('\'for i in cycle(a):\'')
        for i in cycle(a):
            print(i)
            if i == 3:
                break

        print('\ninfinite loop repeating the specified value for the specified number of iterations')
        print('\'for i in repeat(1, 4):\'')
        for i in repeat(1, 4):
            print(i)
