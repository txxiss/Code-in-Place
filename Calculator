## FINAL PROJECT FOR CIP
## JOÃO VITOR TEIXEIRA 
## GITHUB: txxiss

def main():
    while True:
        print('MENU!')
        menu = getcalc()
        if menu == 1:
            estrela_para_triangulo()
        elif menu == 2:
            triangulo_para_estrela()
        else:
            continue
        request = input('Do you want make a new transformation y/n? ').upper()
        if request in ['NO','N']:
            break
def getcalc():
    try :        
        n = int(input('Welcome to Circuit :), If you want to exit press CTRL + C\nSelect calc :\n- 1 for Star-Delta Transformation\n- 2 for Delta-Star Transformation\nAnswer: '))
        if n not in [1,2]:
            raise Exception()
    except (ValueError,Exception):
        print('please Enter a Value 1 or 2')
        
    else : 
        return n
    
def estrela_para_triangulo():
    delta = input('Enter resistence separete by "/" ').strip()
    R1, R2, R3 = delta.split('/')
    R1 = int(R1)
    R2 = int(R1)
    R3 = int(R1)
    Rt1 = (R1 * R2) + (R2 * R3) + (R3 * R1)
    Ra = Rt1 / R1
    Rb = Rt1 / R2
    Rc = Rt1 / R3
    print(f'DELTA  Ra = {Ra}, Rb = {Rb}, Rc = {Rc}')

def triangulo_para_estrela():
    star = input('Enter resistence separete by "/" ').strip()
    Ra, Rb, Rc = star.split('/')
    Ra = int(Ra)
    Rb = int(Rb)
    Rc = int(Rc)
    Rt1 = Ra + Rb + Rc
    R1 = (Ra * Rb) / Rt1
    R2 = (Rb * Rc) / Rt1
    R3 = (Rc * Ra) / Rt1             
    print(f'STAR R1 = {R1}, R2 = {R2}, R3 = {R3}')

if __name__ == "__main__" :
    main()
