import colorama
import emoji
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def imprimir_coste(coste_acumulador,estado_campo):
    print(f'\n{Fore.YELLOW}Estado del objetivo')
    print(f'{Fore.YELLOW}{estado_campo}')
    print(f'{Fore.YELLOW}Medida de desempeño: {coste_acumulador} \U0001F4C8 \U0001F4C9')

def imprimir_bosque(estado_edificacion,coste_acumulador,estado_mercado,estado_campo):
    if estado_edificacion == '1':
        print(f"{Fore.RED}En la Edificación hay un incendio  \U0001F6A8.")
        coste_acumulador += 1#costo por buscar el incendio
        estado_campo['edificacion'] = '0'
        print(f'{Fore.BLUE}Incendio apagado de la Edificación \U0001F692 \U0001F681.')
        coste_acumulador += 1#costo por apagar el incendio
        print(f'{Fore.BLUE}Costo actual: {coste_acumulador}\U0001F4C8 \U0001F4C9')

    if estado_mercado  == '1':
        print(f"{Fore.RED}En el mercado hay un incendio  \U0001F6A8.")
        coste_acumulador += 1#costo por buscar el incendio
        estado_campo['mercado'] = '0'
        coste_acumulador += 1#costo por apagar el incendio
        print(f'{Fore.BLUE}Incendio apagado del Mercado \U0001F692 \U0001F681.')
        print(f'{Fore.BLUE}Costo actual: {coste_acumulador}\U0001F4C8 \U0001F4C9')
    else:
        print(f'En la Edificación y en el Mercado son responsables con el incendio: ')
    imprimir_coste(coste_acumulador,estado_campo)

def imprimir_edificacion(estado_bosque,coste_acumulador,estado_mercado,estado_campo):
    if estado_bosque == '1':
        print(f"{Fore.RED}En el Bosque hay un incendio  \U0001F6A8.")
        coste_acumulador += 1#costo por buscar el incendio
        estado_campo['bosque'] = '0'
        print(f"{Fore.GREEN}Incendio apagado en el Bosque \U0001F692 \U0001F681.")
        coste_acumulador += 1#costo por apagar el incendio
        print(f'{Fore.BLUE}Costo actual: {coste_acumulador}\U0001F4C8 \U0001F4C9')

    if estado_mercado  == '1':
        print(f"{Fore.RED}En el Mercado hay un incendio  \U0001F6A8.")
        coste_acumulador += 1#costo por buscar el incendio
        estado_campo['mercado'] = '0'
        print(f'{Fore.BLUE}Incendio apagado del Mercado \U0001F692 \U0001F681.')
        coste_acumulador += 1#costo por apagar el incendio
        print(f'{Fore.BLUE}Costo actual: {coste_acumulador}\U0001F4C8 \U0001F4C9')
    else:
        print(f'En la Edificación y en el Mercado son responsables con el incendio: ')
    imprimir_coste(coste_acumulador,estado_campo)

def imprimir_mercado(estado_bosque,coste_acumulador,estado_edificacion,estado_campo):
    if estado_bosque == '1':
        print(f"{Fore.RED}En la Bosque hay un incendio  \U0001F6A8.")
        coste_acumulador += 1#costo por buscar el incendio
        estado_campo['bosque'] = '0'
        print(f"{Fore.GREEN}Incendio apagado en el Bosque \U0001F692 \U0001F681.")
        coste_acumulador += 1#costo por apagar el incendio
        print(f'{Fore.BLUE}Costo actual: {coste_acumulador}\U0001F4C8 \U0001F4C9')

    if estado_edificacion  == '1':
        print(f"{Fore.RED}En la Edificación hay un incendio  \U0001F6A8.")
        coste_acumulador += 1#costo por buscar el incendio
        estado_campo['edificacion'] = '0'
        print(f"{Fore.GREEN}Incendio apagado en la E \U0001F692 \U0001F681.")
        coste_acumulador += 1#costo por apagar el incendio
        print(f'{Fore.BLUE}Costo actual: {coste_acumulador}\U0001F4C8 \U0001F4C9')
    else:
        print(f'En la Edificación y en el Mercado son responsables con el incendio: ')
    imprimir_coste(coste_acumulador,estado_campo)

def calculo_agente():
    #1==Encendido || 0==apagado
    estado_campo = {'bosque':'0','edificacion':'0','mercado':'0'}#Creamos un diccionario con su (key, value)
    coste_acumulador = 0 #variable acumuladore
    print('\U0001F681 \U0001F681 \U0001F681 \U0001F681 \U0001F681 \U0001F681 \U0001F681 \U0001F681 \U0001F681')
    print(f'{Fore.RED}-----Menú de Opciones-----')
    print(f'{Fore.BLUE}[1] Bosque \U0001F331')
    print(f'{Fore.BLUE}[2] Edificación \U0001F306')
    print(f'{Fore.BLUE}[3] Mercado \U0001F3D8 \n')
    ubicaion_objetivo = ''
    while ubicaion_objetivo != '1' and ubicaion_objetivo != '2' and ubicaion_objetivo != '3':
        ubicaion_objetivo = input(f"{Fore.GREEN}Ingrese la ubicacion del objetivo: ")
    print(f'{Fore.YELLOW}Meta esperada: {estado_campo}')   
    estado_bosque = ''
    estado_edificacion = ''
    estado_mercado = ''
    
    if ubicaion_objetivo == '1':
        print(f'\n{Fore.GREEN}[0] No hay incendio \U0001F331.')
        print(f'{Fore.RED}[1] Hay incendio {emoji.emojize(":fire:")}.\n')
        while estado_bosque != '0' and estado_bosque != '1':
            estado_bosque = input(f'{Fore.GREEN}Ingrese el estado actual del bosque: ')
        while estado_edificacion != '0' and estado_edificacion != '1':
            estado_edificacion = input(f'{Fore.GREEN}Ingrese el estado actual de la Edificación: ')
        while estado_mercado != '0' and estado_mercado != '1':
            estado_mercado = input(f'{Fore.GREEN}Ingrese el estado actual del mercado: ')

        if estado_bosque == '1':
            print(f"{Fore.RED}En el Bosque hay un incendio \U0001F6A8.")
            estado_campo['bosque'] = '0'#Apagando el incendio, cuidando el medio hambiente
            coste_acumulador += 1
            print(f'{Fore.BLUE}Incendio apagado del Bosque \U0001F692 \U0001F681.')
            print(f'{Fore.BLUE}Costo actual: {coste_acumulador}\U0001F4C8 \U0001F4C9')

            imprimir_bosque(estado_edificacion,coste_acumulador,estado_mercado,estado_campo)

        elif estado_bosque == '0':
            imprimir_bosque(estado_edificacion,coste_acumulador,estado_mercado,estado_campo)

    elif ubicaion_objetivo == '2':
        print(f'{Fore.GREEN}[0] No hay incendio \U0001F331.')
        print(f'{Fore.BLUE}[1] Hay incendio {emoji.emojize(":fire:")}.\n')
        while estado_bosque != '0' and estado_bosque != '1':
            estado_bosque = input('Ingrese el estado actual del bosque: ')
        while estado_edificacion != '0' and estado_edificacion != '1':
            estado_edificacion = input('Ingrese el estado actual de la Edificación: ')
        while estado_mercado != '0' and estado_mercado != '1':
            estado_mercado = input('Ingrese el estado actual del mercado: ')

        if estado_edificacion == '1':
            print(f"{Fore.RED}En la Edificación hay un incendio  \U0001F6A8.")
            estado_campo['edificacion'] = '0'#Apagando el incendio, cuidando el medio hambiente
            coste_acumulador += 1
            print(f"{Fore.GREEN}Incendio apagado en la Edificación \U0001F692 \U0001F681.")
            print(f'{Fore.BLUE}Costo actual: {coste_acumulador}\U0001F4C8 \U0001F4C9')

            imprimir_edificacion(estado_bosque,coste_acumulador,estado_mercado,estado_campo)
        elif estado_edificacion == '0':
            imprimir_edificacion(estado_bosque,coste_acumulador,estado_mercado,estado_campo)
    
    elif ubicaion_objetivo == '3':
        print(f'{Fore.GREEN}[0] No hay incendio \U0001F331.')
        print(f'{Fore.BLUE}[1] Hay incendio {emoji.emojize(":fire:")}.\n')

        while estado_bosque != '0' and estado_bosque != '1':
            estado_bosque = input('Ingrese el estado actual del bosque: ')
        while estado_edificacion != '0' and estado_edificacion != '1':
            estado_edificacion = input('Ingrese el estado actual de la Edificación: ')
        while estado_mercado != '0' and estado_mercado != '1':
            estado_mercado = input('Ingrese el estado actual del mercado: ')

        if estado_mercado == '1':
            print(f"{Fore.RED}En el Mercado hay un incendio  \U0001F6A8.")
            estado_campo['mercado'] = '0'#Apagando el incendio, cuidando el medio hambiente
            coste_acumulador += 1
            print(f'{Fore.BLUE}Incendio apagado del Mercado \U0001F692 \U0001F681.')
            print(f'{Fore.BLUE}Costo actual: {coste_acumulador}\U0001F4C8 \U0001F4C9')
            imprimir_edificacion(estado_bosque,coste_acumulador,estado_mercado,estado_campo)

        elif estado_mercado == '0':
            imprimir_edificacion(estado_bosque,coste_acumulador,estado_mercado,estado_campo)
                
calculo_agente()