# dictionary = {
#     'key': 'value',
#     'second_key': 'second_value',
#     'third_key': 'third_value',
#     123: 'one_two_three'}
# #prints second_value
# print(dictionary['second_key'])
# #prints one_two_three
# print(dictionary[123])

#Figured this one out without watching the lesson on it
name_dictionary = {}

def run_auction():
        name = input("What is your name?\n")
        bid = int(input("What is your bid?\n$"))
        other_people = input("Are there other people?\n")
        winner_name = ''
        if other_people.lower() == 'yes':
            name_dictionary[str(name)] = int(bid)
            run_auction()
        elif other_people.lower() == 'no':
            previous_bid = 0
            counter = 0
            bid_list = []
            name_dictionary[name] = int(bid)
            for key, value in name_dictionary.items():
                bid_list.append(value)
                if int(value) >= previous_bid:
                    counter += 1
                    previous_bid = value
                    winner_name = key
                elif int(value) <= previous_bid:
                     previous_bid != value

            print(f'{winner_name.capitalize()} You have won win the bid of {previous_bid}!')
            return 'Bids are over'

run_auction()