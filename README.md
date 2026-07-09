# CS50 – Credit Card Validator

## Description

This project revisits the _Credit_ exercise from CS50 by implementing the same credit card validator in Python instead of C. It verifies whether a credit card number is valid and identifies its type (AMEX, MASTERCARD, or VISA).

## How it works

The program:

- Prompts the user for a credit card number
- Validates the number using Luhn's algorithm
- Identifies the card issuer based on its length and starting digits
- Prints the card type or "INVALID"

## Usage

```
python credit.py
```

## Example

```
Number: 378282246310005
AMEX
```

## Concepts

- Python functions
- Input validation
- Regular expressions
- Conditional logic
