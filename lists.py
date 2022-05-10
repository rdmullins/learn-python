# Working with Lists

vowels = ["a", "e", "i", "o", "u"]

print(vowels)
print(vowels[0])
print(vowels[1])
print(vowels[2])
print(vowels[3])
print(vowels[4])

vowels.append("y")
print(vowels)

vowels.extend(["t", "p"])
print(vowels)

vowels.insert(2, "j")
print(vowels)

popped_letter = vowels.pop()
print(popped_letter)
print(vowels)

vowels.remove("t")
print(vowels)

vowels.sort()
print(vowels)

vowels.reverse()
print(vowels)

vowels.clear()
print("After clear.... ", vowels)
