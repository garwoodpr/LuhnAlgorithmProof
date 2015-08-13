
# LuhnAlgorithmProof
# Python 3.4 Implementation of the Luhn Algorithm

Python3 system to validate (return True) or reject (return False) a Luhn Compliant Account Number.</br>
Checks 14, 15, or 16 digit card numbers to determine if the number is Luhn compliant.</br>
For details on the formula see: https://en.wikipedia.org/wiki/Luhn_algorithm</br>

Where cardNumber is intended to be an account number (received as a string)</br>
without white space, or separator marks: </br>

The following numbers act as a testable demonstration</br>
cardNumber = '111111111111119'  # Luhn Valid Number </br>
cardNumber = '111111111111111'  # Invalid Luhn Number </br>
cardNumber = '1111-111111-11119'  # Luhn Valid Number but invalid format </br>
cardNumber = '2222222222222224'  # Luhn Valid Number </br>
cardNumber = '2222222222222222'  # Invalid Luhn Number </br>
cardNumber = '2222-2222-2222-2224'  # Luhn Valid Number but invalid format </br>
cardNumber = '33333333333330'  # Luhn Valid Number </br>
cardNumber = '33333-33333-3330'  # Luhn Valid Number but invalid format </br>
cardNumber = '33333333333333'  # Invalid Luhn Number </br>

Luhn Algorithm Compliant Credit Card Types (Partial List)</br>
see: https://en.wikipedia.org/wiki/Bank_card_number (8/2015)</br>

Card Type, Account Digit Length </br>
American Express, 15</br>
Bankcard, 16</br>
Diners Club Carte Blanche, 14</br>
Diners Club International, 14</br>
Diners Club United States & Canada, 16</br>
Discover Card, 16</br>
InstaPayment, 16</br>
JCB, 16</br>
Dankort, 16</br>
MasterCard, 16</br>
Visa, 16</br>
UATP, 15</br>

HART Network (c) 2015 Clint Garwood
