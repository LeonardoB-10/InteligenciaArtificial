#Eliminar un objetivo mediante un disparo utilizando un agente
def fire_gun():
    goal_state = {'A':'0', 'B':'0', 'C:':'0'}
    cost = 0

    location_input = input("Ingrese la ubicacion del objetivo: ") #

    if location_input == 'A': #Para A
        status_input = input("Ingrese el estado de " + location_input + ": ")  # Estado de Ubicacion A
        status_input_complement1 = input("Ingrese el estado de B: ") # Estado de ubicacion B
        status_input_complement2 = input("Ingrese el estado de C: ") # Estado de ubicacion C
        print('Meta deseada: ' + str(goal_state)+' deben ser eliminados')  

        print("\nEl objetivo se coloca en la ubicación A") 
        if status_input == '1': 
            print("En la ubicación A está el Objetivo no eliminado") 
            goal_state['A'] = '0' 
            cost = cost + 1
            print("Eliminando Objetivo en la ubicación A") 
            print("Costo actual: " + str(cost))

            if status_input_complement1 == '1':
                print("\nEn la ubicación B está el Objetivo no eliminado") 
                print("Moviendo a la ubicación B") 
                cost = cost + 1
                print()
                goal_state['B'] = '0'
                cost = cost + 1
                print("Eliminando Objetivo en la ubicación B")
                print("Costo actual: " + str(cost))
            else:
                print("\nEn la ubicación B está el Objetivo eliminado")
                print("No se realizó ninguna acción")
                print("Costo actual: " + str(cost))
            
            if status_input_complement2 == '1':
                print("\nEn la ubicación C está el Objetivo no eliminado") 
                print("Moviendo a la ubicación C") 
                cost = cost + 1
                print()
                goal_state['C'] = '0'
                cost = cost + 1
                print("Eliminando Objetivo en la ubicación C")
                print("Costo actual: " + str(cost))

        elif status_input == '0': 
            print("\nEn la ubicación A está el Objetivo eliminado")
            if status_input_complement1 == '1':
                print("\nEn la ubicación B está el Objetivo no eliminado") 
                print("Moviendo a la ubicación B") 
                cost += 1 #increasing cost for moving righ
                print("Costo actual: " + str(cost))
                # suck the dirt and mark it as clean
                goal_state['B'] = '0'
                cost += 1
                print("Eliminando Objetivo en la ubicación B")
                print("Costo actual: " + str(cost))
            else:
                print("\nEn la ubicación B está el Objetivo eliminado")
                print("No se realizó ninguna acción")
                print("Costo actual: " + str(cost))

            if status_input_complement2 == '1':
                print("\nEn la ubicación C está el Objetivo no eliminado") 
                print("Moviendo a la ubicación C") 
                cost += 1 #increasing cost for moving righ
                print("Costo actual: " + str(cost))
                # suck the dirt and mark it as clean
                goal_state['C'] = '0'
                cost += 1
                print("Eliminando Objetivo en la ubicación C")
                print("Costo actual: " + str(cost))
            else:
                print("\nEn la ubicación C está el Objetivo eliminado")
                print("No se realizó ninguna acción")
                print("Costo actual: " + str(cost))

    elif location_input == 'B': #Para B
        status_input = input("Ingrese el estado de " + location_input + ": ")  # Estado de Ubicacion A
        status_input_complement1 = input("Ingrese el estado de A: ") # Estado de ubicacion B
        status_input_complement2 = input("Ingrese el estado de C: ") # Estado de ubicacion C
        print('Meta deseada: ' + str(goal_state)+' deben ser eliminados') 

        print("\nEl objetivo se coloca en la ubicación B")
        if status_input == '1':
            print("\nEn la ubicación B está el Objetivo no eliminado") 
            goal_state['B'] = '0'
            cost = cost + 1
            print("Eliminando Objetivo en la ubicación B")
            print("Costo actual: " + str(cost))

            if status_input_complement1 == '1':
                print("\nEn la ubicación A está el Objetivo no eliminado") 
                print("Moviendo a la ubicación A") 
                cost = cost + 1
                print()
                goal_state['A'] = '0'
                cost = cost + 1
                print("Eliminando Objetivo en la ubicación A")
                print("Costo actual: " + str(cost))
            else:
                print("\nEn la ubicación A está el Objetivo eliminado")
                print("No se realizó ninguna acción")
                print("Costo actual: " + str(cost))
            
            if status_input_complement2 == '1':
                print("\nEn la ubicación C está el Objetivo no eliminado") 
                print("Moviendo a la ubicación C") 
                cost = cost + 1
                print()
                goal_state['C'] = '0'
                cost = cost + 1
                print("Eliminando Objetivo en la ubicación C")
                print("Costo actual: " + str(cost))
            else:
                print("\nEn la ubicación C está el Objetivo eliminado")
                print("No se realizó ninguna acción")
                print("Costo actual: " + str(cost))
        
    else: #Para C
            status_input = input("Ingrese el estado de " + location_input + ": ")  # Estado de Ubicacion A
            status_input_complement1 = input("Ingrese el estado de A: ") # Estado de ubicacion B
            status_input_complement2 = input("Ingrese el estado de B: ") # Estado de ubicacion C
            print('Meta deseada: ' + str(goal_state)+' deben ser eliminados') 

            print("\nEl objetivo se coloca en la ubicación C")
            if status_input == '1':
                print("\nEn la ubicación C está el Objetivo no eliminado") 
                goal_state['C'] = '0'
                cost = cost + 1
                print("Eliminando Objetivo en la ubicación C")
                print("Costo actual: " + str(cost))

                if status_input_complement1 == '1':
                    print("\nEn la ubicación A está el Objetivo no eliminado") 
                    print("Moviendo a la ubicación A") 
                    cost = cost + 1
                    print()
                    goal_state['A'] = '0'
                    cost = cost + 1
                    print("Eliminando Objetivo en la ubicación A")
                    print("Costo actual: " + str(cost))
                else:
                    print("\nEn la ubicación A está el Objetivo eliminado")
                    print("No se realizó ninguna acción")
                    print("Costo actual: " + str(cost))
                
                if status_input_complement2 == '1':
                    print("\nEn la ubicación B está el Objetivo no eliminado") 
                    print("Moviendo a la ubicación B") 
                    cost = cost + 1
                    print()
                    goal_state['B'] = '0'
                    cost = cost + 1
                    print("Eliminando Objetivo en la ubicación B")
                    print("Costo actual: " + str(cost))
                else:
                    print("\nEn la ubicación B está el Objetivo eliminado")
                    print("No se realizó ninguna acción")
                    print("Costo actual: " + str(cost))

    # done cleaning
    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))

fire_gun()



