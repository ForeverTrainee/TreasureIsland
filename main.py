def main():
    print(
        """
              _               _   
             | |             | |  
          ___| |__   ___  ___| |_ 
         / __| '_ \ / _ \/ __| __|
        | (__| | | |  __/\__ \ |_ 
         \___|_| |_|\___||___/\__|                          
    """
    )


class InvalidDecision(Exception):
    pass


def get_answer_first():
   while True:
    try:
        user_input = input("Left or Right? ")
        if user_input != "Left" and user_input != "Right":
            raise InvalidDecision("Wrong Input")
        else:
            return user_input
    except ValueError:
        print("Value is not a string")
        pass
    except InvalidDecision:
        print("Please enter asked value")
        pass




def get_answer_second():
    while True:
        try:
            user_input = input("Swim or Wait? ")
            if user_input != "Swim" and user_input != "Wait":
                raise InvalidDecision("Wrong Input")
            else:
                return user_input
        except ValueError:
            print("Value is not a string")
            pass
        except InvalidDecision:
            print("Please enter asked value")
            pass

def get_answer_third():
    while True:
        try:
            user_input = input("Which Door? Red, Blue or Yellow? ")
            if user_input != "Red" and user_input != "Blue" and user_input != "Yellow":
                raise InvalidDecision("Wrong Input")
            return user_input
        except ValueError:
            print("Value is not a string")
            pass
        except InvalidDecision:
            print("Please enter asked value")
            pass
def treasure_island():
    print("Welcome to Treasure Island. Your mission is to find treasure.")

    user_input = get_answer_first()

    if user_input == "Right":
        print("Game Over")
    elif user_input == "Left":
        user_input = get_answer_second()

    if user_input == "Swim":
        print("Game Over")
    elif user_input == "Wait":
        user_input = get_answer_third()

    if user_input == "Red":
        print("Game Over")
    elif user_input == "Blue":
        print("Game Over")
    elif user_input == "Yellow":
        print("You Win!")



treasure_island()

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
