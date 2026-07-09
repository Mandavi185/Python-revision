#Question 9.
# Count the frequency of each character in a string using a dictionary

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

print(frequency)