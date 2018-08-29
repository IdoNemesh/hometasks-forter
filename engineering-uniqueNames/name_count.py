import csv
from collections import defaultdict
import Levenshtein

# Min score
min_score = 0.25
dict = {}


def leven_score(s1, s2):
    # Compute and return the distance of two strings by the Levenshtein algorithm
    return 1.0 / (1.0 + Levenshtein.distance(s1, s2))


def flip(name):
    # Flip a name
    if name == '':
        return ''
    if len(name.split()) == 1:
        return name
    name = name.split()
    name.reverse()
    return ' '.join(name)


def count_unique_names(bill_first_name, bill_last_name, ship_first_name, ship_last_name, bill_name_on_card):
    # Returns the number of unique names in a transaction

    # Max unique names
    unique_names = 3

    # Lower casing all names and removing whitespaces
    bill_first_name = bill_first_name.lower().strip()
    bill_last_name = bill_last_name.lower().strip()
    ship_first_name = ship_first_name.lower().strip()
    ship_last_name = ship_last_name.lower().strip()
    bill_name_on_card = bill_name_on_card.lower().strip()

    bill_middle_name = ''
    ship_middle_name = ''
    card_middle_name = ''

    # Bill middle name
    if len(bill_first_name.split()) > 1:
        bill_middle_name = bill_first_name.split()[1]
        bill_first_name = bill_first_name.split()[0]

    # Bill name
    bill_name = bill_first_name + ' ' + bill_last_name

    # Ship middle name
    if len(ship_first_name.split()) > 1:
        ship_middle_name = ship_first_name.split()[1]
        ship_first_name = ship_first_name.split()[0]

    # Ship name
    ship_name = ship_first_name + ' ' + ship_last_name

    # Card name
    card_name = bill_name_on_card

    # Card middle name
    if len(card_name.split()) > 2:
        card_middle_name = ' '.join(card_name.split()[1:-1])
        card_name = card_name.split()
        card_name = card_name[0] + ' ' + card_name[-1]

    # Compare bill-name and ship-name
    if compare(bill_name, bill_middle_name, ship_name, ship_middle_name, skip=True) >= min_score:
        # The flag is for skipping the flip check when comparing bill name and ship name
        unique_names -= 1
        if compare(bill_name, bill_middle_name, card_name, card_middle_name) >= min_score:
            unique_names -= 1

        # Compare bill-name to card-name and ship-name to card-name
    elif compare(bill_name, bill_middle_name, card_name, card_middle_name) >= min_score \
            or compare(ship_name, ship_middle_name, card_name, card_middle_name) >= min_score:
        unique_names -= 1
    return unique_names


def get_nicknames(name):
    # Given an original name, returns it
    # Given a nickname, returns the original name
    for original_name in dict:
        if name == original_name:
            return name
        if name in dict[original_name]:
            return original_name
    return name


def compare(first_full_name, first_middle_name, second_full_name, second_middle_name, skip=False):
    # Returns a score between (0-1) based on the similarity of the names

    # If one middle name is missing, omit both of them
    if first_middle_name is '' or second_middle_name is '':
        first_middle_name = ''
        second_middle_name = ''

    # If middle names are not the same
    if first_middle_name != second_middle_name and leven_score(first_middle_name, second_middle_name) < min_score:
        return 0.0

    # Exact match
    if first_full_name == second_full_name or ((not skip) and first_full_name == flip(second_full_name)):
        return 1.0

    # Find first name intersection (including nicknames)
    first_nicknames = get_nicknames(first_full_name.split()[0])
    second_nicknames = get_nicknames(second_full_name.split()[0])

    # The first and the last name might be reversed, so another intersection should be made
    third_nicknames = ''
    if not skip:
        third_nicknames = get_nicknames(second_full_name.split()[-1])

    names_intersection = 0
    if first_nicknames == second_nicknames or first_nicknames == third_nicknames:
        names_intersection = 1

    # Compare last name only if first names are the same
    if first_full_name.split()[0] == second_full_name.split()[0] or names_intersection > 0:
        return leven_score(first_full_name.split()[-1], second_full_name.split()[-1])
    return leven_score(first_full_name, second_full_name)


# Main
nicknames_dict = defaultdict(list)
# Loading the csv file to a dictionary
with open('nickname.csv.txt', 'r') as file:
    reader = csv.reader(file)
    for key, value in reader:
        key = key.strip().lower()
        value = value.strip().lower()
        nicknames_dict[key].append(value)

dict = nicknames_dict
# Tests
print count_unique_names("Deborah", "Egli", "Deborah", "Egli", "Deborah Egli")  # 1
print count_unique_names("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli")  # 1
print count_unique_names("Deborah", "Egni", "Deborah", "Egli", "Deborah Egli")  # 1
print count_unique_names("Deborah S", "Egli", "Deborah", "Egli", "Egli Deborah")  # 1
print count_unique_names("Michele", "Egli", "Deborah", "Egli", "Michele Egli")  # 2
