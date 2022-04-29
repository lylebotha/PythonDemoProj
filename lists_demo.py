# imports
from demo import Demo


class ListsDemo(Demo):

    # properties
    mixed_list = []
    int_list = []
    new_int_list = []
    str_list = []
    new_str_list = []

    # init
    def __init__(self, name):
        # call base class init
        super().__init__(name)

        # init mixed list
        self.mixed_list = [3, 5, 2, 'BMW', 'Audi', 'Mercedes-Benz', 4, 1]

    # methods
    def do_work(self):
        # call base class method
        super().do_work()

        # print info
        print(' - Collection Data Type')
        print(' - Lists are mutable! values can be modified!')

        # print mixed list
        print('\nMixed List:\n' + self.mixed_list.__repr__())

        # separate lists into 2 lists by type using casting and exception handling
        for item in self.mixed_list:
            try:
                int(item)
                self.int_list.append(item)
            except ValueError:
                self.str_list.append(item)

        # sort and print new separated lists
        self.int_list.sort()
        self.str_list.sort()
        print('\nInteger List:\n' + self.int_list.__repr__())
        print('\nString List:\n' + self.str_list.__repr__())

        # append popped items onto new string list (achieves a reverse())
        print('\nPop & Append(Reverse):')
        length = len(self.str_list)
        for i in range(length):
            self.new_str_list.append(self.str_list.pop())
            print(self.str_list.__repr__() + ' ---> ' + self.new_str_list.__repr__())

        # splitting
        txt = self.new_str_list[0:1].__repr__() + ' + ' + self.new_str_list[1:2].__repr__() + ' + ' + self.new_str_list[2:3].__repr__();
        print(txt)

        # duplicating with logic
        print('\nDuplicating: element-wise logic')
        print(self.int_list.__repr__() + '\nmultiply each element by 2')
        self.new_int_list = [item*2 for item in self.int_list]
        print(self.new_int_list.__repr__())
