class HammingDistance:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
    def calculate_hamming_distance(self):
        if len(self.str1) != len(self.str2):
            return "string length must be the same"

        distance = sum(char1 != char2 for char1, char2 in zip(self.str1, self.str2))
        return distance
str1 = input("Enter string1: ")
str2 = input("Enter string2: ")
calculator = HammingDistance(str1, str2)
hamming_dist = calculator.calculate_hamming_distance()
print(f"The Hamming Distance is: {hamming_dist}")
