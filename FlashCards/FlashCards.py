class Term:
    """Represents a list of terms.  This list will be converted to a dictionary"""
    def __init__(self, list):
        self._list = list
        self._dict = {}
    def convert_list(self):
        """Returns a dictionary based on the list passed into the Term object"""
        for i in range(0, len(self._list), 2):
            self._dict[self._list[i]] = self._list[i + 1]
        return self._dict
    def add_terms(self, list):
        """Returns nothing, only adds a list of terms and definitions to the dictionary"""
        for i in range(0, len(list), 2):
            self._dict[list[i]] = list[i + 1]
        return self._dict
    def delete_term(self):
        """Returns nothing, deletes a list of terms and definitions from the dictionary"""
    def get_dictionary(self):
        """Returns and prints the dictionary and any updates that may have been made"""
        print(self._dict)
        return self._dict


def main():
    first_list = ['Continuous integration (CI)', 'Code is constantly written and merged into a central repo frequently',
            'Security checks CI', 'Documented sec baselines, large scale security analysis during testing',
            'Continuous Delivery (CD)', 'the testing and release is automated for the application, manually deploy app',
            'Continuous Deployment (CD)', 'Entire testing and deployment process is automated']
    ob = Term(first_list)
    ob.convert_list()
    ob.get_dictionary()
    second_list = ['Directory Services', 'Central database that stores all the usernames, psswds, computers, devices, '
                                         'ect. All authentication requests reference this directory', 'Federation',
                   'Uses credentials stored with a third party to authenticate with your org']
    ob.add_terms(second_list)
    ob.get_dictionary()
if __name__ == '__main__':
    main()
