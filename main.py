# imports
from demo import Demo
from lists_demo import ListsDemo
from dictionaries_demo import DictionariesDemo
from tuples_demo import TuplesDemo
from sets_demo import SetsDemo
from strings_demo import StringsDemo
from collections_demo import CollectionsDemo
from itertools_demo import ItertoolsDemo

# properties
my_demos = [Demo]


# methods
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # add demos to demo list
    my_demos.append(ListsDemo('Lists: ordered, mutable, allows duplicate elements'))
    my_demos.append(TuplesDemo('Tuples: ordered, immutable, allows duplicate elements'))
    my_demos.append(DictionariesDemo('Dictionaries: key-value pairs, unordered, mutable'))
    my_demos.append(SetsDemo('Sets: unordered, mutable, no duplicates'))
    my_demos.append(StringsDemo('Strings: ordered, immutable, text representation'))
    my_demos.append(CollectionsDemo('Collections: Counter, namedTuple, OrderedDict, defaultdict, deque'))
    my_demos.append(ItertoolsDemo('itertools: product, permutations, combinations, accumulate, groupby, infinite iterators'))

    # do work for each demo class
    for demo in my_demos:
        if isinstance(demo, ListsDemo):
            ListsDemo.do_work(demo)
        elif isinstance(demo, TuplesDemo):
            TuplesDemo.do_work(demo)
        elif isinstance(demo, DictionariesDemo):
            DictionariesDemo.do_work(demo)
        elif isinstance(demo, SetsDemo):
            SetsDemo.do_work(demo)
        elif isinstance(demo, StringsDemo):
            StringsDemo.do_work(demo)
        elif isinstance(demo, CollectionsDemo):
            CollectionsDemo.do_work(demo)
        elif isinstance(demo, ItertoolsDemo):
            ItertoolsDemo.do_work(demo)



