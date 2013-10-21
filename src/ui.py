#! usr/bin/env/python

class ConsoleUI(object):
    """Reads from stdin or writes to stdout. """
    def __init__(self):
        pass

    def get_input(self, prompt):
        """ Returns string """
        response = raw_input(prompt)
        return response

    def display_data(self, data):
        """ Prints data """
        print data