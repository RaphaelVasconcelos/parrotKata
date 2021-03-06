from parrot import AfricanParrot, EuropeanParrot, NorwegianBlueParrot


def test_speedOfEuropeanParrot():
    parrot = EuropeanParrot(0, 0, False)
    assert parrot.speed() == 12.0


def test_speedOfAfricanParrot_With_One_Coconut():
    parrot = AfricanParrot(1, 0, False)
    assert parrot.speed() == 3.0


def test_speedOfAfricanParrot_With_Two_Coconuts():
    parrot = AfricanParrot(2, 0, False)
    assert parrot.speed() == 0.0


def test_speedOfAfricanParrot_With_No_Coconuts():
    parrot = AfricanParrot(0, 0, False)
    assert parrot.speed() == 12.0


def test_speedNorwegianBlueParrot_nailed():
    parrot = NorwegianBlueParrot(0, 1.5, True)
    assert parrot.speed() == 0.0


def test_speedNorwegianBlueParrot_not_nailed():
    parrot = NorwegianBlueParrot(0, 1.5, False)
    assert parrot.speed() == 18.0


def test_speedNorwegianBlueParrot_not_nailed_high_voltage():
    parrot = NorwegianBlueParrot(0, 4, False)
    assert parrot.speed() == 24.0
