strings = ["Mickey","Mack", "Marvin", "Mikke", "Merlin", "Mck"]

for word in sorted(strings, key=lambda word: "".join([c for c in word if c in "aeiou"])):
    print(word)