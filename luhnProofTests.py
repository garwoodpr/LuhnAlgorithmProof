import luhnProofFunction

tooShort = '123'
def test_proof_too_short_fails(tooShort):
    assert doLuhn(tooShort) == False

tooLong = '123456789123456789'
def test_proof_too_long_fails(tooLong):
    assert doLuhn(tooLong) == False

sixteenDigitLuhn = '2222222222222224'
def test_16_digit_proof_success(sixteenDigitLuhn):
    assert doLuhn(sixteenDigitLuhn) == True

sixteenDigitDud = '2222222222222222'
def test_16_digit_proof_fails(sixteenDigitDud):
    assert doLuhn(sixteenDigitDud) == False

fifteenDigitLuhn = '111111111111119'
def test_15_digit_proof_success(fifteenDigitLuhn):
    assert doLuhn(fifteenDigitLuhn) == True

fifteenDigitDud = '111111111111111'
def test_15_digit_proof_fails(fifteenDigitDud):
    assert doLuhn(fifteenDigitDud) == False

fourteenDigitLuhn = '33333333333330'
def test_14_digit_proof_success(fourteenDigitLuhn):
    assert doLuhn(fourteenDigitLuhn) == True

fourteenDigitDud = '33333333333330'
def test_14_digit_proof_fails(fourteenDigitDud):
    assert doLuhn(fourteenDigitDud) == False

anyAlphaFails = '3a333333333330'
def test_14_digit_proof_fails(anyAlphaFails):
    assert doLuhn(anyAlphaFails) == False

anythinButDigitsFails = '33.3333333330'
def test_14_digit_proof_fails(anythinButDigitsFails):
    assert doLuhn(anythinButDigitsFails) == False
