#INSTRUCTIONS
#Enter LOCATION A/B in captial letters
#Enter Status O/1 accordingly where 0 means CLEAN and 1 means DIRTY

def vacuum_world():
    # initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location_input = input("Enter Location of Vacuum: ") #Ingrese la habitacion a limpiar 
    status_input = input("Enter status of: " + location_input) #ingrese el estado de la habitacion
    status_input_complement = input("Enter status of other room: ")#ingrese el estado de la habitacion B
    print("Desired Goal:" + str(goal_state))

    if location_input == 'A':
        # Location A is Dirty.
        print("Vacuum is placed in Location A: ")
        if status_input == '1':
            print("Location A is Dirty.")#la habitacion A esta sucia
            # suck the dirt  and mark it as clean
            goal_state['A'] = '0'
            cost += 1## increasing cost for cleaning A
            print("Cleaning location A")
            print("Current Cost: " + str(cost))

            if status_input_complement == '1':
                # if B is Dirty
                print("Location B is Dirty.")
                print("Moving right to the Location B. ")
                cost += 1 #increasing cost for moving right
                print("Current cost: " + str(cost))
                # suck the dirt and mark it as clean
                goal_state['B'] = '0'
                cost += 1 #increasing cost for cleaning
                print("Cleaning location B")
                print("Current cost: " + str(cost))
            else:
                # suck and mark clean
                print("Location B is already clean.")
                print("No action. Current cost" + str(cost))
               
        if status_input == '0':
            print("Location A is already clean.")
            if status_input_complement == '1':# if B is Dirty
                print("Location B is Dirty.")
                print("Moving RIGHT to the Location B.")
                cost += 1 #increasing cost for moving right
                print("Current cost: " + str(cost))
                # suck the dirt and mark it as clean
                goal_state['B'] = '0'
                cost += 1   
                print("Cleaning location B. ")                    #cost for suck
                print("Updated cost: "+str(cost))
                
            else:
                print("No action " + str(cost))
                print(cost)
                # suck and mark clean
                print("Location B is already clean.")

    else:
        print("Vacuum is placed in location B")
        # Location B is Dirty.
        if status_input == '1':
            print("Location B is Dirty.")
            # suck the dirt  and mark it as clean
            goal_state['B'] = '0'
            cost += 1  # cost for suck
            print("COST for CLEANING " + str(cost))
            print("Location B has been Cleaned.")

            if status_input_complement == '1':
                # if A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1  # cost for moving right
                print("COST for moving LEFT" + str(cost))
                # suck the dirt and mark it as clean
                goal_state['A'] = '0'
                cost += 1  # cost for suck
                print("COST for SUCK " + str(cost))
                print("Location A has been Cleaned.")

        else:
            print(cost)
            # suck and mark clean
            print("Location B is already clean.")

            if status_input_complement == '1':  # if A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1  # cost for moving right
                print("COST for moving LEFT " + str(cost))
                # suck the dirt and mark it as clean
                goal_state['A'] = '0'
                cost += 1  # cost for suck
                print("Cost for SUCK " + str(cost))
                print("Location A has been Cleaned. ")
            else:
                print("No action " + str(cost))
                # suck and mark clean
                print("Location A is already clean.")

    # done cleaning
    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))


vacuum_world()