# imports
from demo import Demo


class StringsDemo(Demo):

    # properties
    my_string1 = 'single quotation marks'
    my_string2 = "double quotation marks, needs no escape '\n'"
    my_string3 = """triple double quotation marks
    allows multi line"""

    # init
    def __int__(self, name):
        # call base init
        super().__int__(name)

    # methods
    def do_work(self):
        # call base method
        super().do_work()

        # print info
        print(' - Collection Data Type')

        # print string
        print('\n' + self.my_string1.__repr__() + ' is a ' + self.my_string1.__class__.__name__)
        print(self.my_string2.__repr__())
        print(self.my_string3)

        # sub strings
        my_string = 'hello world'
        print('\nslicing of ' + my_string.__repr__() + ' into sub-strings')
        print('my_string[0] = ' + my_string[0])
        print('my_string[0:5] = ' + my_string[0:5])
        print('my_string[::2] = ' + my_string[::2])
        print('my_string[::-1] = ' + my_string[::-1])
        my_list = my_string.split(' ')
        print('\nstring into list, my_string.split(\' \') = ' + my_list.__repr__())
        new_string = ''.join(my_list)
        print('list into string, \'\'.join(my_list) = ' + new_string.__repr__())
        print('JOINING is MORE EFFICIENT than LOOPING!!!')

        # adding string
        name_string = 'Tom'
        surname_string = 'Hardy'
        print('\nadding strings')
        print(name_string.__repr__() + ' + \' \' + ' + surname_string.__repr__())
        print('= ' + (name_string + ' ' + surname_string).__repr__())

        # if statement
        print('\nconditional statements')
        print('is \'H\' in ' + name_string.__repr__() + '?')
        if 'H' in name_string:
            print('Yes')
        else:
            print('No')
        print('is \'H\' in ' + surname_string.__repr__() + '?')
        if 'H' in surname_string:
            print('Yes')
        else:
            print('No')

        # string formatting
        print('\nold string formatting')
        name = 'Tom'
        age = 37
        formatted_string = '%s is %i' % (name, age)
        print('\'%s is %i\' % (name, age)')
        print('= ' + formatted_string.__repr__())

        print('\nnew string formatting (faster)')
        name = 'Alex'
        age = 29
        formatted_string = '{} is {}'.format(name, age)
        print('\'{} is {}\'.format(name, age)')
        print('= ' + formatted_string.__repr__())

        print('\nnewest string formatting (event faster)')
        name = 'Jim'
        age = 45
        formatted_string = f'{name} is {age}'
        print('f\'{name} is {age}\'')
        print('= ' + formatted_string.__repr__())