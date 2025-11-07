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
    if negative == True:
        y = -float(back[0])
    else:
        y = float(back[0])
    modulus = (x**2+y**2)**0.5
    angle = (math.atan(y/x))
    return modulus, angle
comp_num = '-1 + 4i'
mod, theta = complex_number(comp_num)
theta_simple = str(theta/math.pi),'π'
print(f'Modulus = {mod}, Arctan = {theta} = {theta_simple}')