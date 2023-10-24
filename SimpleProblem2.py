#----------------------------------------------
# Write a function that will take a given string and reverse the order of the words.
#----------------------------------------------

# ========================= solution =========================
def revwords(str1):
    # printing the string passed to this function
    # print(str1)
    # made a list of words from that string and reversed
    str1 = str1.split(" ")[::-1]
    # again converted the list of words into whole string
    str1 = " ".join(str1)
    # printed the final result
    print(str1)
# taking input for string
revwords(input("type your string here --> "))

# ========================= let's see this also =========================

def revwordshigh(str1):
    # made a list of words from that string
    str1 = str1.split(" ")
    # initialized another list
    lst1 = []
    # reversed and appended each word from str1 into lst1
    for word in str1:
        lst1.append(word[::-1])
    # reversed the list
        lst1 = lst1[::-1]
    # again converted the list of words into whole string
    str1 = " ".join(lst1)
    # printed the final result i.e. reversed words of a string
    print(str1)
# taking input for string
revwordshigh(input("type your string here --> "))
