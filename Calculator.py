
##Final Project Code In Place - Delta to Star Circuit Calculator - João Vitor Teixeira - GitHub: txxiss

def main():
    while True:
        print('MENU!')
        menu = getcalc()
        if menu == 1:
            estrela_para_triangulo()
        elif menu == 2:
            triangulo_para_estrela()
        elif menu == 3:
            calculate_power_current()
        else:
            continue
        request = input('Do you want to make a new transformation? (y/n) ').upper()
        if request in ['NO', 'N']:
            break

def getcalc():
    try:
        n = int(input('Welcome, If you want to exit press CTRL + C\nSelect a transformation :\n- 1 for Star-Delta Transformation\n- 2 for Delta-Star Transformation\n- 3 for Power and Current\nAnswer: '))
        if n not in [1, 2, 3]:
            raise Exception()
    except (ValueError, Exception):
        print('please Enter a Value 1, 2 or 3')
    else:
        return n

def estrela_para_triangulo():
        star = input('Enter resistance separated by "/" ').split('/')
        star[0] = int(star[0])
        star[1] = int(star[1])
        star[2] = int(star[2])
        if star[0] == 0:
            print('R1 need to be != 0')
        elif star[1] == 0:
            print('R2 need to be != 0')
        elif star[2] == 0:
            print('R3 need to be != 0')
        else:
            delta = ((star[0] * star[1])+(star[1] * star[2])+(star[2] * star[0]))
            Ra = int(delta/star[0])
            Rb = int(delta/star[1])
            Rc = int(delta/star[2])
            print(f'DELTA Ra = {Ra} Ω, Rb = {Rb} Ω, Rc = {Rc} Ω')

def triangulo_para_estrela():
        delta = input('Enter resistance separated by "/" ').split('/')
        delta[0] = int(delta[0])
        delta[1] = int(delta[1])
        delta[2] = int(delta[2])

        star = (delta[0] + delta[1] + delta[2])
        R1 = int((delta[0]*delta[1])/star)
        R2 = int((delta[1]*delta[2])/star)
        R3 = int((delta[0]*delta[2])/star)

        if delta[0] == 0:
            print('Ra need to be != 0')
        elif delta[1] == 0:
            print('Rb need to be != 0')
        elif delta[2] == 0:
            print('Rc need to be != 0')
        else:
            print(f'STAR R1 = {R1} Ω, R2 = {R2} Ω, R3 = {R3} Ω')

def calculate_power_current():
    V = float(input("Enter Voltage (V): "))
    R1 = float(input("Enter Resistance (Ω): "))
    if R1 <= 0:
        print('Resistence must be > 0')
    else:
        I = V / R1
        P = V * I
        print(f"Current (I) = {I} A")
        print(f"Power (P) = {P} W")

if __name__ == "__main__":
    main()
