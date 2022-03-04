from parrot import EuropeanParrot, Parrot, ParrotType


def test_speedOfEuropeanParrot():
    parrot = EuropeanParrot(0, 0, False)
    assert parrot.speed() == 12.0


def test_speedOfAfricanParrot_With_One_Coconut():
    parrot = Parrot(1, 0, False, ParrotType.AFRICAN)
    assert parrot.speed() == 3.0


def test_speedOfAfricanParrot_With_Two_Coconuts():
    parrot = Parrot(2, 0, False, ParrotType.AFRICAN)
    assert parrot.speed() == 0.0


def test_speedOfAfricanParrot_With_No_Coconuts():
    parrot = Parrot(0, 0, False, ParrotType.AFRICAN)
    assert parrot.speed() == 12.0


def test_speedNorwegianBlueParrot_nailed():
    parrot = Parrot(0, 1.5, True, ParrotType.NORWEGIAN_BLUE)
    assert parrot.speed() == 0.0


def test_speedNorwegianBlueParrot_not_nailed():
    parrot = Parrot(0, 1.5, False, ParrotType.NORWEGIAN_BLUE)
    assert parrot.speed() == 18.0


def test_speedNorwegianBlueParrot_not_nailed_high_voltage():
    parrot = Parrot(0, 4, False, ParrotType.NORWEGIAN_BLUE)
    assert parrot.speed() == 24.0
