class JaccardCoefficient:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
    def calculate_jaccard_coefficient(self):
        set1 = set(self.str1)
        set2 = set(self.str2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        jaccard = intersection / union
        return jaccard
str1 = input("Enter str1: ")
str2 = input("Enter str2: ")
calculator = JaccardCoefficient(str1, str2)
jaccard_index = calculator.calculate_jaccard_coefficient()
print(f"The Jaccard Coefficient is: {jaccard_index:.2f}")
