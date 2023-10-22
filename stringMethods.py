#==========================================
# string and its methods
#==========================================
a = "this is A string"
b = "abcdabcdabcd this is A string abcdabcdabcd"
# print(a)
# print(a.capitalize())
# print(a.upper())
# print(a.casefold())
# print(a.swapcase())
# print(a.title())
# print(a.lower())
# print(a.count('s'))
# print(a.find('63'))
# print(a.index('63'))
# print(a.center(100, '-'))
# print(a.zfill(100))
# print(a.replace(' ', '_'))
# print(a.split(' '))
# print(a.rsplit('i', maxsplit=0))
# print(a.rpartition(' '))
# print(a.partition(' '))
# print(b.strip('abcd'))
# print(b.rstrip('abcd'))
# print(b.lstrip('abcd'))
# print(" ".join(a))
# print(a.startswith('this'))
# print(a.endswith('ing'))
# print(a.isalnum())
# print(a[:4].isalpha())
# print(a[4].isspace())
# print(a.isascii())
# print(a.isdecimal())
# print(a.isdigit())
# print(a.isidentifier())
# print(a.isnumeric())
# print(a.islower())
# print(a.isupper())
# print(a.istitle())
# print(a.isprintable())
# print(a.ljust(50, '_'))
# print(a.rjust(50, '_'))
# print(a.removeprefix('t'))
# print(a.removesuffix("ing"))

# ==================================================
str1 = "There are 10 distinct symbols in decimal number system."
# print(str1)
# print(len(str1))
# print(str1[0], str1[5], str1[52])
# print(str1[:])
# print(str1[10:])
# print(str1[:15])
# print(str1[45:46])
# print(str1[-20:-4])
# print(str1[::])
# print(str1[::2])
# print(str1[::5])
# print(str1[25::2])
# print(str1[::-1])
# print(str1[::-2])
# print(str1[:25:2])
# print(str1[:25:-2])
# print(str1[-12:-5])
# print(str1[-12:-5:2])
# print(str1[-12:5:-2])

# ==================================================

str2 = "ABCDEFGHIJ"
# print(str2)
# print(str2[::2])
# print(str2[::-1])
# print(str2[::-2])
# print(str2[2:-2:])
# print(str2[-2:2:-1])
# print(str2[-2:2:-2])

# ==================================================
# # manually written
# # str.removeprefix()  as removefirst(str, prefix)
# # str.removesuffix()  as removelast(str, suffix)

# def removefirst(str, prefix):
#     if str.startswith(prefix):
#         return str[len(prefix):]
#     else: return str

# def removelast(str, suffix):
#     if str.endswith(suffix):
#         return str[:-len(suffix)]
#     else: return str

# string = "hello, I am VK."
# print(removefirst(string, "he"))
# print(removelast(string, "."))
