'''
for i in range(101):
    print(i)
    j = i / 5
    if j.is_integer() == True:
        print(i,"is a multiple of 5")
'''

for i in range(101):
    print(i)
    j = i % 5
    if j == 0:
        print(i,"is a multiple of 5")
    
