import math
def complex_number(comp_num):    
    # comp_num = input('Complex number: ')
    
    remove = str.maketrans({' ': ''})
    comp_simple = comp_num.translate(remove)
    comp_list = list(comp_simple.strip())
    
    if '-' in comp_list:
        position = comp_list.index('-')
        negative = True
    elif '+' in comp_list:
        position = comp_list.index('+')
        negative = False
    
    front = comp_list[:position]
    
    x = float(front[0])
    back = comp_list[(position+1):]
    if back[0] == 'i':
        back[0]=1
    
    if negative == True:
        y = -float(back[0])
    else:
        y = float(back[0])
    
    return x, y

# Input the complex number in the format (n) + (m)i, where n and m are the coefficients of the real and imaginary parts respectively
comp_num1, comp_num2 = '1 + 4i', '1-9i'

a,b = complex_number(comp_num1)
print(a,b)
c,d = complex_number(comp_num2)
print(c,d)
def multiply(a,b,c,d):
    real = a*c-b*d
    complex = a*d+c*b
    return real, complex
real, complex = multiply(a,b,c,d)
if complex > 0:
    print(f"The product is {real} + {complex}i")
elif complex < 0:
    complex = -complex
    print(f"The product is {real} - {complex}i")

