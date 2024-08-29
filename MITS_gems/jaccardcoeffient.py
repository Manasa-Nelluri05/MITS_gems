def jaccard_coefficient(str1, str2):
    """
        Calculate the Jaccard Coefficient between two strings.

        The Jaccard Coefficient is a measure of similarity between two sets,
        defined as the size of the intersection divided by the size of the union
        of the sets formed by the characters in the strings.

        Args:
            str1 (str): The first input string.
            str2 (str): The second input string.

        Returns:
            float: The Jaccard Coefficient, a value between 0 and 1 indicating the
            similarity between the two strings.

        Example:
             jaccard coefficient("hello", "hola")
            0.4
        """
    set1=set(str1)
    set2=set(str2)
    intersection=len(set1.intersection(set2))
    union=len(set1.union(set2))
    jaccard=intersection / union
    return jaccard
str1=input("enter str1:")
str2=input("enter str2:")
jaccard_index=jaccard_coefficient(str1,str2)
print(f"The Jaccard Coefficient is:{jaccard_index:.2f}")