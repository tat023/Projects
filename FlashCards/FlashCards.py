import random


class Term:
    """Represents a list of terms. This list will be converted to a dictionary"""

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
        dictionary. Returns a statement if this is completed successfully, the key is typed incorrectly,
         or if the key does not exist"""
        if key in self._dict.keys():
            self._dict.pop(key)
            return print(f'{key} has been deleted')
        if key not in self._dict.keys():
            for term in self._dict:
                if key.lower() == term.lower():
                    return print(f'{key} has a typo, this is case sensitive')  # will create a better method
            return print(f'{key} is not a term')

    def print_dictionary(self):
        """Prints the dictionary and any updates that may have been made"""
        print(self._dict)

    def get_dictionary(self):
        """Returns the dictionary"""
        return self._dict


class Flashcard:
    """Represents an individual key value pair from the Term object"""

    def __init__(self, term_ob):
        self._term_ob = term_ob
        self._key_list = []
        self._def_list = []

    def shuffle_cards(self):
        """Method uses random to shuffle the keys and values in the dictionary from the Term object into a
        randomized list"""
        larger_dict = self._term_ob.get_dictionary()
        all_terms = larger_dict.keys()
        all_defs = larger_dict.values()
        for words in all_terms:
            self._key_list.append(words)
            random.shuffle(self._key_list)
        for definitions in all_defs:
            self._def_list.append(definitions)
            random.shuffle(self._def_list)
        return self._key_list, self._def_list

    def display_matches(self):
        """Method displays a key and 4 values from dictionary from the Term object. If none of the values match the key
        the user will type 'None of the above' """
        index_num = random.randint(0, len(self._key_list))
        selected_term = self._key_list[index_num]
        print(
            f'Please select the definition for {selected_term}. If none of these definitions match, type "None of '
            f'the above".')
        correct_choice = self._def_list[index_num]
        all_options = []
        all_options.append(correct_choice)
        for choices in range(0,3):
            random_def = random.randint(0, len(self._def_list))
            mult_choice = self._def_list[random_def]
            all_options.append(mult_choice)
        for defs in all_options:
            print(defs)
        user_input = input("Your answer: ")



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
    fourth_list = ['Pseudo random token generator', 'can be an app or device, many use TOTP', 'TOTP',
                   'Time based on time passwd algorithm, uses a secret key and time of day', 'HOTP',
                   'HMAC-based one time password algorithm, One-time psswd, never use it again, hash is diff everytime',
                   'Phone call', 'call gives you a random number, same disadvs as text (interception, forwarded',
                   'Static code', 'authentication that does not change, like pin or psswrds', 'Smart card',
                   'integrated circuit card, credit cards or access control cards, something you have']
    ob.add_terms(fourth_list)
    term = 'cat'
    ob.delete_term(term)
    card = Flashcard(ob)
    print(card)
    print(card.shuffle_cards())
    card.display_matches()


if __name__ == '__main__':
    main()
