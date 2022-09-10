from randomWordGenerator import getWord,clearDatabase
def start():
    """This function will start the Game"""

    print("Welcome to Word Game!!!!!")
    response = input("Enter [y/n] to Start/Exit the game.")
    Score = 0
    if response == "y" or response == "Y":
        gameWords = getWord()
        for i,j in gameWords.items():
            userResponse = input(f"Arrange the letters to form a valid word:\n{j}\n")
            if userResponse == i:
                Score+=1
                print("Correct")
            else:
                Score-=1
                print("Wrong")
        
        print(f"Your Net Score is {Score}")
            
    else:
        clearDatabase()
        print("Thank You for giving your time!!!\n\nSee you next time.")


if __name__ == "__main__":
    start()