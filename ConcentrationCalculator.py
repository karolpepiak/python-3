#Concentration calculator - env (Python 3.11 (64-bit)) by Karol Pepiak
from queue import Empty
import os

def clear():
    os.system('cls')

def find_percentage_concentration(solvent_mass, substance_mass):
    solution_mass = solvent_mass + substance_mass
    percentage_concentration = (substance_mass / solution_mass) * 100
    return percentage_concentration

def find_molar_concentration(substance_mass, molar_mass, volume):
    n = substance_mass/molar_mass
    molar_concentration = n/volume
    return molar_concentration

app_running = True
user_choise = 0
temp_input_string = str(Empty)
temp_bool = True
history_array = []

print("This application was created to calculate concentrations of chemical substances.")

while app_running is True:

    os.system('cls')
    print("Choose what You want to do:")
    print("[1] Calculate percentage concentration")
    print("[2] Calculate molar concentration")
    print("[3] Show history")

    while temp_bool is True:
        try:
            user_choise = int(input())
            if user_choise != 1 and user_choise != 2 and user_choise !=3:
                print("Type number from 1 to 3")
            else:
                clear()
                temp_bool = False
        except:
            print("Wrong input format!")

    temp_bool = True

    if user_choise == 1:
        
        print("Enter substance mass [g]:")
        while temp_bool is True:
            try:
                substance_mass = float(input())
                temp_bool = False
                clear()
            except:
                print("Wrong input format!")
                substance_mass = 0

        temp_bool = True

        print("Enter solvent mass [g]:")
        while temp_bool is True:
            try:
                solvent_mass = float(input())
                temp_bool = False
                clear()
            except:
                print("Wrong input format!")
                solvent_mass = 0

        temp_bool = True

        result = find_percentage_concentration(solvent_mass, substance_mass)
        msg = "The percentage concentration of " + str(substance_mass) + "g of substance dissolved in " + str(solvent_mass) + "g of solvent is: " + str(result) + "%."
        history_array.append(msg)
        print(msg)

    elif user_choise == 2:
        
        print("Enter substance mass [g]:")
        while temp_bool is True:
            try:
                substance_mass = float(input())
                temp_bool = False
                clear()
            except:
                print("Wrong input format!")
                substance_mass = 0

        temp_bool = True

        print("Enter molar mass of the substance [g/mol]:")
        while temp_bool is True:
            try:
                molar_mass = float(input())
                temp_bool = False
                clear()
            except:
                print("Wrong input format!")
                #molar mass for water
                molar_mass = 18.01528

        temp_bool = True

        print("Enter solvent volume [dm3]:")
        while temp_bool is True:
            try:
                volume = float(input())
                temp_bool = False
                clear()
            except:
                print("Wrong input format!")
                volume = 0

        temp_bool = True

        result = find_molar_concentration(substance_mass, molar_mass, volume)
        msg = "The molar concentration of " + str(substance_mass) + "g of substance with molar mass equal to " + str(molar_mass) + "g/mol dissolved in " + str(volume) + "dm3 of solvent is: " + str(result) + "mol/dm3."
        history_array.append(msg)
        print(msg)
    
    elif user_choise == 3:
        clear()
        for i in range(len(history_array)):
            element = history_array[i]
            print("[" + str(i) + "] " + str(element))


    print("Do You want to calculate another concentration?")
    print("[Y] Yes")
    print("[N] No")
    
    while temp_bool is True:
        try:
            temp_input_string = str(input())
            if temp_input_string != "N" and temp_input_string != "n" and temp_input_string != "Y" and temp_input_string != "y":
                print("Type N or Y")
                temp_bool = True
            else:
                if temp_input_string == "N" or temp_input_string == "n":
                    print("Thank You for using this application.")
                    app_running = False
                else:
                    app_running = True
                temp_bool = False
        except:
            print("Wrong input format!")
            temp_input_string = str(Empty)

    temp_bool = True
