
# LuhnAlgorithmProof
# Python 3.4 Implementation of the Luhn Algorithm

Python3 system to validate (return True) or reject (return False) a Luhn Compliant Account Number.
Checks 14, 15, or 16 digit card numbers to determine if the number is Luhn compliant.
For details on the formula see: https://en.wikipedia.org/wiki/Luhn_algorithm

# where cardNumber is intended to be an account number (received as a string)
# without white space, or separator marks: 
# the following numbers act as a testable demonstration
# cardNumber = '111111111111119'  # Luhn Valid Number 
# cardNumber = '111111111111111'  # Invalid Luhn Number 
# cardNumber = '1111-111111-11119'  # Luhn Valid Number but invalid format 
# cardNumber = '2222222222222224'  # Luhn Valid Number 
# cardNumber = '2222222222222222'  # Invalid Luhn Number 
# cardNumber = '2222-2222-2222-2224'  # Luhn Valid Number but invalid format 
# cardNumber = '33333333333330'  # Luhn Valid Number 
# cardNumber = '33333-33333-3330'  # Luhn Valid Number but invalid format 
# cardNumber = '33333333333333'  # Invalid Luhn Number 

Luhn Algorithm Compliant Credit Card Types (Partial List)
see: https://en.wikipedia.org/wiki/Bank_card_number (8/2015)

Card Type, Account Digit Length 
American Express, 15
Bankcard, 16
Diners Club Carte Blanche, 14
Diners Club International, 14
Diners Club United States & Canada, 16
Discover Card, 16
InstaPayment, 16
JCB, 16
Dankort, 16
MasterCard, 16
Visa, 16
UATP, 15

