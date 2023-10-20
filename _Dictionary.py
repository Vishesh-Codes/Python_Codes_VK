# ====================
# A simple Dictionary
# ====================
book = {"mutable" : "can be change",
        "immutable" : "can not be change",
        "implicit" : "suggested though not directly expressed",
        "explicit" : "stated clearly and in detail, leaving no room for confusion or doubt"}
# print("Ask me a word ☺")
# query = input()               # optimized code is written below
query = input("Ask me a word ☺ : ")
query0 = query.lower()
print(query.capitalize() + " = " + book[query0])
