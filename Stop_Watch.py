#I wanted to test my ability in coding, with just one school year of learning Raptor, so i programed a working stop wach and a count downer in the terminal with Python. You can exit any time. It has a very good desine when it comes to a disyplaing time.(I did this as a 16yo)



#check if all variables are reset after program goes again
import time
import math

#function for showing time on screen
def time_function(oficial_time):
    hours = oficial_time // 3600
    remaining_after_hour = oficial_time % 3600
    minutes = remaining_after_hour // 60
    seconds = remaining_after_hour % 60

    # Code will sort out if somethink is 0 it wont dispay it
    if hours == 0 and minutes == 0 and seconds == 0:
        print("\nTime:",(math.floor((end - start)*10))/10,"sec")

    elif hours == 0 and minutes == 0 and seconds > 0:
        print("\nTime:",seconds,"sec")

    elif hours == 0 and minutes > 0 and seconds == 0:
        print("\nTime:",minutes,"min")

    elif hours == 0 and minutes > 0 and seconds > 0:
        print("\nTime:",minutes,"min",seconds,"sec")

    elif hours > 0 and minutes == 0 and seconds == 0:
        print("\nTime:",hours,"h")

    elif hours > 0 and minutes == 0 and seconds > 0:
        print("\nTime:",hours,"h",seconds,"sec")

    elif hours > 0 and minutes > 0 and seconds == 0:
        print("\nTime:",hours,"h",minutes,"min")

    else:
        print("\nTime:",hours,"h",minutes,"min",seconds,"sec")

# Loop that will end when user types exit when he is done with the program
while True:

    #MODE CHOSING
    # User must select wich mode he will use
    print("\n\n\nYou have two modes;\n\nMode one: Stopwatch\nMode two:Timer\n")
    mode_select = input("Type ~1~ for MODE 1 or ~2~ for MODE 2\n")

    # The loop will check if the user typed -1- or -2- and if not, the loop wont end until thay type -start-
    while True:
        if mode_select not in ("1","2"):
            # Program will shout down if the user types -exit-
            if mode_select.lower() == "exit":
                print("Program closing...")
                time.sleep(1)
                print("Program closed.")
                exit()

            print("\nError: You didnt insert a correct number\n")
            mode_select = input("Type ~1~ for MODE 1 or ~2~ for MODE 2\n")
        else:
            break

    #MODE 1
    if mode_select == "1":

        # Basic instructions
        print("\nWhen you will type ~start~ the timer will began and when you type ~end~ the time will end. How much time was in between will be shown on the screen\nYou can exit the program anytime by typing ~exit~\n\n")

        # User must type -start- for it to start
        time_start = input("Type ~start~ to start it:\n")

        # The loop will check if the user typed -start- and if not, the loop wont end until thay type -start-
        while True:
            if time_start.lower() != "start":
                    # Program will shout down if the user types -exit-
                if time_start.lower() == "exit":
                    print("Program closing...")
                    time.sleep(1)
                    print("Program closed.")
                    exit()

                print("Error: You didnt insert a correct word")
                time_start = input("Type here to start it:\n")
            else:
                break

        # Time will start and when you insert -end- the time will end
        start = time.time()
        print("\nTime started\n")

        # User must type -end- so the progrem stops
        time_end = input("Type ~end~ to stop it:\n")

        # The loop will check if the user typed -end- and if not, the loop wont end until thay type -end-
        while True:
            if time_end.lower() != "end":
                    # Program will shout down if the user types -exit-
                if time_end.lower() == "exit":
                    print("Program closing...")
                    time.sleep(1)
                    print("Program closed.")
                    exit()

                print("Error: You didnt insert a correct word")
                time_end = input("Type here to stop it:\n")
            else:
                end = time.time()
                break

        # Code will calculate the time betwen the start and the end
        oficial_time = math.floor((end - start))

        #function for showing time on screen
        time_function(oficial_time)
  
            # Code will ask if the user wants to exit or continue on the manu
        while True:
            exit_check_for_user = input("\n\nYou finished! If you want to close the program type -exit- or if you whoud like to go to the mode menu type -menu-.\n")

            if exit_check_for_user.lower() != "menu":
                    # Program will shout down if the user types -exit-
                if exit_check_for_user.lower() == "exit":
                    print("Program closing...")
                    time.sleep(1)
                    print("Program closed.")
                    exit()

                print("Error: You didnt insert a correct word")
            else:
                break

    #MODE 2            
    else:
        #Basic instructions
        print("\nWhat ever number you will type, the time will start count downing from that specific number [The number must be full number]. You can exit the program by typing -exit-.\nWARING: once you start the timer you can exit just by closing the program\n\n")

        #user will type the number

        while True:
            timer_count = input("Type the number in seconds:\n")

            #code will see if the user typed a full number and if yes the loop will end
            if timer_count.isdigit():
                break

            
                #loop will continue unless the user types a full number
            else:
                # Program will shout down if the user types -exit-
                if timer_count.lower() == "exit":
                    print("Program closing...")
                    time.sleep(1)
                    print("Program closed.")
                    exit()

                print("Error: You didnt insert a correct number")

        time.sleep(1)
        print("Time has started:")

        #number will go fronm string to int
        timer_count = int(timer_count)

        while timer_count > 0:

            #function for showing time on screen
            time_function(timer_count)
        
            timer_count = timer_count - 1
            time.sleep(1)

        print("Time is up!!!")

            # Code will ask if the user wants to exit or continue on the manu
        while True:
            exit_check_for_user = input("\n\nYou finished! If you want to close the program type -exit- or if you whoud like to go to the mode menu type -menu-.\n")

            if exit_check_for_user.lower() != "menu":
                    # Program will shout down if the user types -exit-
                if exit_check_for_user.lower() == "exit":
                    print("Program closing...")
                    time.sleep(1)
                    print("Program closed.")
                    exit()

                print("\nError: You didnt insert a correct word")
            else:
                break
