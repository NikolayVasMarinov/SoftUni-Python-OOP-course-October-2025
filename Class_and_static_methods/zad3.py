from math import floor

roman_to_int = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float) -> str | "Integer":
        if type(float_value) != float:
            return "value is not a float"

        return cls(int(floor(float_value)))

    @classmethod
    def from_roman(cls, value: str):
        nums = list(value)
        int_value = 0

        for i, char in enumerate(nums[:len(nums) - 1]):
            if roman_to_int[char] < roman_to_int[nums[i + 1]]:
                int_value -= roman_to_int[char]

            else:
                int_value += roman_to_int[char]

        int_value += roman_to_int[nums[-1]]
        return cls(int_value)

    @classmethod
    def from_string(cls, value: str):
        if type(value) != str:
            return "wrong type"

        return cls(int(value))