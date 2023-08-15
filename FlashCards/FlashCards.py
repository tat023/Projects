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

    def delete_term(self, key):
        """Takes the parameter key, a string, and deletes that key value pair if the input matches a key in the
        dictionary. Returns a statement if this is completely successfully or if the key does not exist"""
        if key in self._dict.keys():
            self._dict.pop(key)
            return print(f"{key} has been deleted")
        if key not in self._dict.keys():
            return print(f"{key} is not a term")


    def get_dictionary(self):
        """Returns and prints the dictionary and any updates that may have been made"""
        print(self._dict)
        return self._dict


def main():
    first_list = ['Continuous integration (CI)', 'Code is constantly written and merged into a central repo frequently',
                  'Security checks CI', 'Documented sec baselines, large scale security analysis during testing',
                  'Continuous Delivery (CD)',
                  'the testing and release is automated for the application, manually deploy app',
                  'Continuous Deployment (CD)', 'Entire testing and deployment process is automated']
    ob = Term(first_list)
    ob.convert_list()
    second_list = ['Directory Services', 'Central database that stores all the usernames, psswds, computers, devices, '
                                         'ect. All authentication requests reference this directory', 'Federation',
                   'Uses credentials stored with a third party to authenticate with your org, must est trust']
    ob.add_terms(second_list)
    third_list = ['Attestation', 'Proves the hardware is really the user and is a sys you can trust. It is attesting'
                                 'it is trust worthy', 'Remote Attestation', 'Device provides an operational report'
                                                                             'to verification server, Encrypted',
                  'IMEI', 'International Mobile Equipment Identity, is a numeric identifier, usually unique', 'SMS',
                  'Short message service/text, authenticates using a text, easy to reassign phone number harder to'
                  'intercept', 'Push notification', 'Uses an authentication factor pushed to an app, sometimes push'
                                                    'is sent in the clear (bad)']
    ob.add_terms(third_list)
    ob.get_dictionary()
    word = 'cat'
    ob.delete_term(word)
    ob.get_dictionary()


if __name__ == '__main__':
    main()
