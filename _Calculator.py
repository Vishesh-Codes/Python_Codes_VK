# ====================
# A simple calculator
# ====================
# print("Enter the first value", end=" = ")
# n1 = input()
# print("Enter the second value", end=" = ")
# n2 = input()
# print("Sum =",int(n1) + int(n2))
# print("Difference =",int(n1) - int(n2))
# print("Product =",int(n1) * int(n2))
# print("Quotient =",int(n1) / int(n2))
# print(type(int(n1) / int(n2)))



# =========================================
# A simple calculator - optimized version
# =========================================
# n1 = input("Enter the first value: ")
# n2 = input("Enter the second value: ")
# print("Sum =",int(n1) + int(n2))
# print("Difference =",int(n1) - int(n2))
# print("Product =",int(n1) * int(n2))
# print("Quotient =",int(n1) / int(n2))
# print(type(int(n1) / int(n2)))



# =========================================
# Advanced calculator made with Python
# =========================================
# print("\n\n"+"Welcome to the Python calculator".center(100, " "))
# print("I am the best calculator. You can trust me ☻\n\n".center(100, " "))

# a = int(input("first operand?  "))
# o = input("operator?  ").lower()
# b = int(input("second operand?  "))


# if o == "+" or o == "plus" or o.startswith("a"):
#     print(a, "+", b, "=", a + b)
# elif o == "-" or o == "minus" or o.startswith("s"):
#     print(a, "-", b, "=", a - b)
# elif o == "*" or o == "product" or o == "×" or o == "x" or o.startswith("m"):
#     print(a, "×", b, "=", a * b)
# elif o == "/" or o == "÷" or o.startswith("d"):
#     print(a, "÷", b, "=", a / b)
# else:
#     print(a, o, b, "=", "??\n Invalid_Operator_Error")



#==========================================
# Making Real Life Calculator
#==========================================
result = 0
while(result != ValueError):
    arg = input("type your problem: ")
    # if
    values = arg.partition("+")
    result = int(values[0]) + int(values[2])
    print(f"Ans: {result}")
else:
    print("Unexpected input detected")
    # break



# ==================================================
# name = input("enter your question: ")
# if name.index("+") != ValueError:
#     listo = name.partition("+")
#     result = int(listo[0]) + int(listo[2])
#     print(f"{listo[0]} + {listo[2]} = {result}")
# elif name.index("-") != ValueError:
#     listo = name.partition("-")
#     result = int(listo[0]) - int(listo[2])
#     print(f"{listo[0]} - {listo[2]} = {result}")
