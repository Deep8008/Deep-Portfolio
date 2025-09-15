def body_mass_index(weight, height):
    
    '''
    This function calculates your BMI
    by dividing your weight by your hight squared
    and then tells you which category you fall into
    '''

    res = weight / height**2
    f_res = round(res, 2)
    if res <= 18.5:
        print(f"your Body Mass Index(BMI) is {f_res}, you have Underweight!")
    elif res <= 24.9:
        print(f"your Body Mass Index(BMI) is {f_res}, you have Healthy Weight!")
    else:
        print(f"your Body Mass Index(BMI) is {f_res}, you have Over Weight!")
        
print("please type your Weight:")
weight = int(input())

print("please type your Height:")
height = float(input())

body_mass_index(weight, height)
