
print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

direction = input("left or right? \n").lower()

if direction != "left":
    print('You fell into a hole.')
    print('GAME OVER.')

elif direction == "left":
    Swim = input("swim or wait? \n").lower()
    
    if ( Swim != "wait" ):
        print('You were attached by a shark.')
        print('GAME OVER.')

    else:
        Door = input('Which door? blue / yellow / red? \n').lower()

        if (Door == "blue"):
            print('You were eaten by beasts')
            print('GAME OVER.')

        elif (Door == "yellow"):
            print('YOU WIN')
            art = """
              _______    _______     __________ _____________
            - ______ \ - ______ \ / _____   //.  .  ._______/
            / /     / // /     / //_/     / // ___   /
            / /     / // /     / /       .-'//_/|_/,-'
            / /     / // /     / /     .-'.-'
            / /     / // /     / /     / /
            / /     / // /     / /    / /
            / /_____/ // /_____/ /   / /
            \________- \________-   /_/
            """
            
            print(art)

        elif (Door == "red"):
            print('You were burned by fire')
            print('GAME OVER.')

        else:
            print('GAME OVER')
