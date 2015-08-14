# Luhn Account Number Validator

### Tests 14-16 Digit Account Numbers for   
### Luhn Algorithm Compliance   

This module, written in python3, takes a 14, 15, or 16 digit account number   
(for example a credit/debit card number) and applies the Luhn Algorithm to   
the provided data. If the data passes the test the system returns 'True',    
else the system returns 'False'.   

An account number must be provided as a simple all-digits string without any   
type of separators, including white space, or the function will return 'False'.    
False values are also returned if the string contains any alpha characters,    
punctuation marks or non-digit characters of any kind. 


## Using the Luhn Algorithm Validator 

'<code>    
    import luhn from aLuhn   
    
    >>> cardNumber = '2222222222222224'   
    >>> trueOrFalse = aLuhn.doLuhn(cardNumber)   
    >>> trueOrFalse    
    True   
    
    >>> cardNumber = '2222222222222222'   
    >>> trueOrFalse = aLuhn.doLuhn(cardNumber)   
    >>> trueOrFalse      
    False   
</code>'   
