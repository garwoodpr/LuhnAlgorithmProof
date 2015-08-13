import unittest 
from unittest import TestCase
from doLuhn import aLuhn

class TestStringMethods(unittest.TestCase):

    def test_16_digit_proof_success(sixteenDigitLuhn):
        TestStringMethods().assertIs(aLuhn.doLuhn('2222222222222224'), True)

    def test_15_digit_proof_success(fifteenDigitLuhn):
        TestStringMethods().assertIs(aLuhn.doLuhn('111111111111119'), True)

    def test_14_digit_proof_success(fourteenDigitLuhn):
        TestStringMethods().assertIs(aLuhn.doLuhn('33333333333330'), True)

    def test_proof_too_long_fails(cardNumber):
        TestStringMethods().assertFalse(aLuhn.doLuhn('123456789123456789'))

    def test_16_digit_proof_fails(sixteenDigitDud):
        TestStringMethods().assertFalse(aLuhn.doLuhn('2222222222222222'))

    def test_15_digit_proof_fails(fifteenDigitDud):
        TestStringMethods().assertFalse(aLuhn.doLuhn('111111111111111'))

    def test_14_digit_proof_fails(fourteenDigitDud):
        TestStringMethods().assertFalse(aLuhn.doLuhn('33333333333333'))

    def test_14_digit_proof_fails(anyAlphaFails):
        TestStringMethods().assertFalse(aLuhn.doLuhn('3a333333333330'))

    def test_14_digit_proof_fails(anythinButDigitsFails):
        TestStringMethods().assertFalse(aLuhn.doLuhn('33.3333333330'))

    def test_proof_too_short_fails(cardNumber):
        TestStringMethods().assertFalse(aLuhn.doLuhn('123'))
