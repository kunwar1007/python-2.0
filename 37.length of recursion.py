#Method 1 : Length of the String using Recursion
def length(str):
    if str == "":
        return 0
    return 1 + length(str[1:])


str = "PrepInsta"
print("length of", str, "is", length(str))