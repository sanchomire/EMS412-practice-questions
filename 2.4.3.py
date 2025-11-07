def get_number():
    number = int(input("Enter integer: "))
    return number
def factorial(number):
    fac = 1
    mult = ''
    for i in range(number,0,-1):
        fac = fac*i
        if i == number:
            mult = mult + str(i)
        else: 
            mult = mult + ' x ' + str(i)
    return fac, mult
def main():
    number = get_number()
    fac, mult = factorial(number)
    print(f'Factorial of {number} = {mult} = {fac}')

main()