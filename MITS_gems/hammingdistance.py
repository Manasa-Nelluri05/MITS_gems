def hamming_distance(str1, str2):
    """
        Calculate the Hamming distance between two strings of equal length.

        Args:
            str1 (str): The first string to compare.
            str2 (str): The second string to compare.

        Returns:
            int: The Hamming distance between str1 and str2 if they are of equal length.
            str: An error message if str1 and str2 are not of equal length.
        Example:
        hamming_distance("karolin", "kathrin")
        3

        hamming_distance("10100", "10011")
        3

        hamming_distance("hello", "world")
        'string length must be same'
"""
    if len(str1)!=len(str2):
        return "string length must be same"
    distance=sum(char1 != char2 for char1, char2 in zip(str1, str2))
    return distance
# Example usage:
str1=input("enter string1:")
str2=input("enter string2:")
hamming_dist=hamming_distance(str1, str2)
print(f"The Hamming Distance is:{hamming_dist}")