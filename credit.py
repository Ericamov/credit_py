import re


def main():

    # Ask for a credit card number
    number_str = input("Number: ")

    # Check if number has 13 or 15 or 16 digits
    if not re.fullmatch(r"\d{13}|\d{15}|\d{16}", number_str):
        print("INVALID")
        return

    # Validate number using Luhn’s algorithm
    number_int = int(number_str)
    luhn_sum = sum_digits(number_int) + multiply_digits(number_int)

    if not is_valid_card(luhn_sum):
        print("INVALID")
        return

    # Extract number length and first two digits
    length = len(number_str)
    first_digits = int(number_str[:2])

    # Determine card type
    card_type = find_card_type(first_digits, length)
    print(card_type)


# Sum every other digits, starting with last one
def sum_digits(number):
    total = 0

    while number > 0:
        total += number % 10
        number //= 100

    return total


# Multiply every other digit by 2, starting with second to last
def multiply_digits(number):
    total = 0

    number //= 10
    while number > 0:
        digit = (number % 10) * 2

        if digit > 9:
            digit = (digit % 10) + (digit // 10)

        total += digit
        number //= 100

    return total


def is_valid_card(total):
    return total % 10 == 0


# check card len and starting digits
def find_card_type(first_digits, length):

    # Print AMEX (American Express) if it has 15 digits and starts with 34 or 37
    if length == 15 and first_digits in (34, 37):
        return "AMEX"
    # Print VISA if it has 13 or 16 digits and starts with 4
    if length in (13, 16) and first_digits // 10 == 4:
        return "VISA"
    # print MASTERCARD if it has 16 digits and starts with 51, 52, 53, 54 or 55
    if length == 16 and 51 <= first_digits <= 55:
        return "MASTERCARD"
    return "INVALID"


main()
