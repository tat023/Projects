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
        self._terms_covered = set()

    def shuffle_cards(self):
        """Method uses random to shuffle the keys and values in the dictionary from the Term object into a
        randomized list"""
        larger_dict = self._term_ob.get_dictionary()
        all_terms = larger_dict.keys()
        all_defs = larger_dict.values()
        for words in all_terms:
            self._key_list.append(words)
        for definitions in all_defs:
            self._def_list.append(definitions)
        return self._key_list, self._def_list

    def start_studying(self):
        """Method displays a key and 4 values from dictionary from the Term object. If none of the values match the key
        the user will type 'None of the above' """
        while len(self._terms_covered) < len(self._key_list):
            index_num = random.randint(0, len(self._key_list) - 1)
            selected_term = self._key_list[index_num]
            if index_num in self._terms_covered:
                continue
            self._terms_covered.add(index_num)
            print(
                f'Please select the definition for {selected_term}. If none of these definitions match, type "None of '
                f'the above".')
            correct_choice = self._def_list[index_num]
            all_options = [correct_choice]
            for choices in range(0, 3):
                random_def = random.randint(0, len(self._def_list) - 1)
                mult_choice = self._def_list[random_def]
                all_options.append(mult_choice)
                random.shuffle(all_options)
            for definitions in all_options:
                print(definitions)
            user_input = input("Your answer: ")
            while user_input == "None of the above":
                all_options = [correct_choice]
                for choices in range(0, 3):
                    random_def = random.randint(0, len(self._def_list) - 1)
                    mult_choice = self._def_list[random_def]
                    all_options.append(mult_choice)
                    random.shuffle(all_options)
                for definitions in all_options:
                    print(definitions)
                user_input = input("Your answer: ")
            while user_input != correct_choice:
                user_try = input("Try again: ")
                if user_try == correct_choice:
                    print("That's right!")
                    break
            if user_input == correct_choice:
                print("That's right!")
