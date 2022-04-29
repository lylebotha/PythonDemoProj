# imports
from demo import Demo
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque


class CollectionsDemo(Demo):

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
        print(' - import from collections module')

        # Counter
        print('\n-----------------------------------------------------------------------------------------------------')
        print('Counter')
        print('-----------------------------------------------------------------------------------------------------')
        print(' - key-value pairs')
        print(' - param must be ITERABLE!')
        my_counter = Counter('abbcccddddeeeee')
        print('\nCounter(\'abbcccddddeeeee\')')
        print('= ' + my_counter.__repr__())
        print('\nmy_counter.keys() gives Dict of keys')
        print(my_counter.keys())
        print('\nmy_counter.values() gives Dict of values')
        print(my_counter.values())
        print('\nmost_common(2) gives list of Tuples')
        print(my_counter.most_common(2))
        print('\nelements() gives iterable')
        print(list(my_counter.elements()))

        # namedTuple
        print('\n-----------------------------------------------------------------------------------------------------')
        print('namedTuple')
        print('-----------------------------------------------------------------------------------------------------')
        print(' - allows creation of struct/class like objects')

        Point = namedtuple('Point', 'x,y')
        pt = Point(1, 2)
        print('\nPoint = namedTuple(\'Point\', \'x,y\')')
        print('pt = Point(1, 2)')
        print(pt)

        # OrderedDict
        print('\n-----------------------------------------------------------------------------------------------------')
        print('OrderedDict')
        print('-----------------------------------------------------------------------------------------------------')
        print(' - just like a regular dictionary except remembers order of pair insertion')
        print(' - Not as useful as of Python 3.7 as regular dictionaries can do the same')

        ordered_dict = OrderedDict()
        ordered_dict['a'] = 1
        ordered_dict['b'] = 2
        ordered_dict['c'] = 3
        ordered_dict['d'] = 4
        print('\n' + ordered_dict.__repr__())

        # defaultDict
        print('\n-----------------------------------------------------------------------------------------------------')
        print('defaultDict')
        print('-----------------------------------------------------------------------------------------------------')
        print(' - returns default value for unassigned keys instead of throwing KeyError')

        default_dict = defaultdict(int)
        default_dict['a'] = 3
        default_dict['b'] = 5
        print('\n' + default_dict.__repr__())
        print('default_dict[\'c\'] = ' + default_dict['c'].__repr__() + ' (default int value is 0)')

        default_dict = defaultdict(list)
        default_dict['a'] = [1, 3, 5]
        default_dict['b'] = [2, 4, 6]
        print('\n' + default_dict.__repr__())
        print('default_dict[\'c\'] = ' + default_dict['c'].__repr__() + ' (default list value is [])')

        # deque
        print('\n-----------------------------------------------------------------------------------------------------')
        print('deque')
        print('-----------------------------------------------------------------------------------------------------')
        print(' - double ended queue, can add & remove elements from both ends')
        print(' - very efficient')

        my_deque = deque()
        my_deque.append(1)
        my_deque.append(2)
        my_deque.append(3)
        print('\n' + my_deque.__repr__())
        my_deque.appendleft(4)
        print('\nmy_deque.appendleft(4)')
        print(my_deque)
        my_deque.append(5)
        print('\nmy_deque.append(5)')
        print(my_deque)
        my_deque.pop()
        print('\nmy_deque.pop()')
        print(my_deque)
        my_deque.popleft()
        print('\nmy_deque.popleft()')
        print(my_deque)
        my_deque.extend([5, 6, 7])
        print('\nmy_deque.extend([5, 6, 7])')
        print(my_deque)
        my_deque.extendleft([11, 12, 13])
        print('\nmy_deque.extendleft([11, 12, 13])')
        print(my_deque)
        my_deque.rotate(1)
        print('\nmy_deque.rotate(1)')
        print(my_deque)
        my_deque.rotate(-2)
        print('\nmy_deque.rotate(-2)')
        print(my_deque)

