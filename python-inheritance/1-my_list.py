#!/usr/bin/python3
""" defina class MyList which inherits from list """


class MyList(list):
    """ class MyList """
    def print_sorted(self):
        print(sorted(self))
