#Question 10.
#print odd numbers from 1 to 50.
# method 1.
'''
for i in range(1, 51, 2):
    print(i)
'''

# method 2.
for i in range(1, 51):
    if i % 2 != 0:
        print(i)    