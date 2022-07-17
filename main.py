# Normal Dict: Key ---> Value
# Reversed Dict: Value ----> Key
# Stanford Code in Place 2021 Data Science Lecture Question, and it's solution


def main():
    print("Hello World")
    ages = {
        'Mehran': 51,
        'Gary': 70,
        'Chris': 33,
        'Freya': 1,
        'Adele': 33,
        'Lionel': 33,
        'Rihanna': 33,
        'Stephen': 33
    }

    reversed_dict = reverse(ages)
    print("Reversed:")

    for key in reversed_dict:
        print(key, '-->', reversed_dict[key])


def reverse(original):
    reversed_dict = {}

    for old_key in original:
        old_value = original[old_key]
        # reversed_dict[old_value] = old_key
        # case: if this is the first time we have ever seen old_value then we should make a new list
        if old_value not in reversed_dict:
            reversed_dict[old_value] = []
        else:
            # get the list that is already associated with old_value and add to it !
            value_list = reversed_dict[old_value]
            value_list.append(old_key)

    return reversed_dict


if __name__ == '__main__':
    main()

# reversed = {
#     51: [Mehran'],
#     70: ['Gary'],
#     33: ['Chris', 'Adele', 'Lionel', 'Rihanna', 'Stephen'],
#     1 : ['Freya']
# }
