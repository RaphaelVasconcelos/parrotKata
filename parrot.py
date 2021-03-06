from enum import Enum  # Enum is introduced in Python 3.4.

class Parrot:

    def __init__(self, number_of_coconuts, voltage, nailed):
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        raise ValueError("should be unreachable")

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    def _load_factor(self):
        return 9.0

    def _base_speed(self):
        return 12.0

class EuropeanParrot(Parrot):
    def speed(self):
        return self._base_speed()


class AfricanParrot(Parrot):
    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)


class NorwegianBlueParrot(Parrot):
    def speed(self):
        if self._nailed:
            return 0
        else:
            return self._compute_base_speed_for_voltage(self._voltage)
