sec_terms = {'card': 'def'}
print(sec_terms)
print(sec_terms['card'])
dictionary = dict(term = 'CI', definition = 'continuous integration')
print(dictionary)
print(dictionary.keys())

my_list_keys = ['term', 'works']
my_list_values = ['the def', 'answer is yes']
big_list = ['this', 'is', 'working', 'h', 'another', 'wow', 'six']
start_dict = {}
#for iteration in range(0, len(big_list), 2):
 #   start_dict[big_list[iteration]] = big_list[iteration+1]
#print(start_dict)

for i in range(0, len(big_list), 3):
    print(i)
    print(big_list[i])




class Term:
    """Represents a list of terms.  This list will be converted to a dictionary"""
    def __init__(self, list):
        self._list = list
    def convert_list(self):
        """Returns a dictionary based on the list passed into the Term object"""
    def add_terms(self):
        """Returns nothing, only adds a term and a definition to the dictionary"""
    def delete_term(self):
        """Returns nothing, deletes a term and a definition from the dictionary"""
    def get_dictionary(self):
        """Returns to dictionary and any updates that may have been made"""

def main():
    list = [1, 2, 3]
    ob = Term(list)
    print(ob)
if __name__ == '__main__':
    main()

