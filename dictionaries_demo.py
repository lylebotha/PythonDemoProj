# imports
from demo import Demo


class DictionariesDemo(Demo):

    # properties
    dict = dict(Abraham='tank', Alligator='helicopter', Typhoon='ship', Raptor='fighter jet')

    # init
    def __init__(self, name):
        # call base class init
        super().__init__(name)

    # methods
    def do_work(self):
        # call base class method
        super().do_work()

        # print info
        print(' - Collection Data Type')

        # print dictionary
        print('\n' + self.dict.__repr__() + ' is a ' + self.dict.__class__.__name__)

        # alternate way of defining a dict with parenthesis
        print('\ndefining a dict with parenthesis')
        dict2 = {'Jessica': 'girl', 'Andrew': 'boy', 'Rupert': 'boy'}
        print(dict2)

        # change value at key 1 to rusty tank and print
        print('\nchange value at key \'Typhoon\' to \'submarine\'')
        self.dict['Typhoon'] = 'submarine'
        print(self.dict)

        # delete items with del keyword and pop
        print('\ndelete item at key \'Abraham\' with del keyword, key 2 with pop() and last added with popitem()')
        del self.dict['Abraham']
        print(self.dict)
        print('\ndelete item at key \'Alligator\' with pop()')
        self.dict.pop('Alligator')
        print(self.dict)
        print('\ndelete item last added with popitem()')
        self.dict.popitem()
        print(self.dict)

        # add new key-value pairs and print
        print('\nadd new key-value pairs or items')
        self.dict['S-300'] = 'anti-aircraft missile'
        self.dict['Tomahawk'] = 'cruise-missile'
        print(self.dict)

        # for loops with dicts
        print('\nprint all items')
        print('KEY : VALUE')
        for key, value in self.dict.items():
            print(key + ' : ' + value)

        # copying with simple assignment
        print('\ncopying with simple assignment - note they point to the same memory')
        dict_cpy = self.dict
        print('original: ' + self.dict.__repr__())
        print('copy: ' + dict_cpy.__repr__())
        print('\nadding new \'Predator\' item to the copy changes both')
        dict_cpy['Predator'] = 'UAV'
        print('original: ' + self.dict.__repr__())
        print('copy: ' + dict_cpy.__repr__())

        # copying with copy() method
        print('\ncopying with copy method - gives deep clone')
        dict_cpy = self.dict.copy()
        print('original: ' + self.dict.__repr__())
        print('copy: ' + dict_cpy.__repr__())
        print('\npopping item from copy does not change the original dict')
        dict_cpy.pop('Predator')
        print('original: ' + self.dict.__repr__())
        print('copy: ' + dict_cpy.__repr__())

        # tuples can be used as keys
        print('\ntuples can be used as keys')
        tuple_key = ('Joe', 'Soap')
        new_dict = {tuple_key: 27}
        print(new_dict)
