class OverlapCoefficient:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
    def calculate_overlap_coefficient(self):
        set1 = set(self.str1)
        set2 = set(self.str2)
        intersection = len(set1.intersection(set2))
        smaller_set_size = min(len(set1), len(set2))
        overlap = intersection / smaller_set_size
        return overlap
str1 = input("Enter string1: ")
str2 = input("Enter string2: ")
calculator = OverlapCoefficient(str1, str2)
overlap_coef = calculator.calculate_overlap_coefficient()
print(f"The Overlap Coefficient is: {overlap_coef:.2f}")
