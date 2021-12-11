# COMP1531 Lab 02
#
# Dan Nguyen (z5206032)
# 25/2/2020

def calculate_bmi(w, h):
    return float(w) / (float(h) * float(h))

def print_bmi():
    while True:
        w = input('What is your weight in kg? ')
        h = input('What is your height in m? ')

        try:
            print('Your BMI is %.1f\n' % calculate_bmi(w, h))

        except ValueError:
            print('\nError: Invalid BMI input...\n')

        except Exception:
            if float(h) <= 0 or float(w) <= 0:
                print('\n Error: Nonpositive BMI input...\n')

        else:
            break

if __name__ == '__main__':
    print_bmi()