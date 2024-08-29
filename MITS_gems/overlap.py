def overlap_coefficient(str1,str2):
    """
        Calculate the Overlap Coefficient between two strings.

        The Overlap Coefficient is a measure of similarity between two sets,
        defined as the size of the intersection divided by the size of the
        smaller set of the two sets formed by the characters in the strings.

        Args:
            str1 (str): The first input string.
            str2 (str): The second input string.

        Returns:
            float: The Overlap Coefficient, a value between 0 and 1 indicating
            the proportion of overlap relative to the smaller set.

        Example:
            overlap_coefficient("hello", "helicopter")
            0.40
        """
    set1=set(str1)
    set2=set(str2)
    intersection=len(set1.intersection(set2))
    smaller_set_size=min(len(set1), len(set2))
    overlap=intersection / smaller_set_size
    return overlap
str1=input("enter string1:")
str2=input("enter string2:")
overlap_coef=overlap_coefficient(str1, str2)
print(f"The Overlap Coefficient is: {overlap_coef:.2f}")