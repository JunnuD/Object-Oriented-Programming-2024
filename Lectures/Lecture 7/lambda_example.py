strings = ["Mickey","Mack", "Marvin", "Mikke", "Merlin", "Mck"]

for word in sorted(strings, key=lambda word: "".join([c for c in word if c in "aeiou"])):
    print(word)

    """
    List comprehension
    [<expression> for <item> in <series>]

    lambda expression
    lambda <parameters>: <expression>
    """ 


print()
print("Old Fashioned way")

new_list = []
for word in strings:
    for c in word:
        if c in "aeiou  ":
            find = True
    if find:
        new_list.append(word)
    find = False

sorted_list = sorted(new_list)

for word in sorted_list:
    print(word)