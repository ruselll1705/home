while True:

    print("Type 'quit' to exit")

    phrase = input("Your message: ")

    if phrase == "quit":

        break

    elif phrase == "Hello" or phrase == "Hi":

        print("Hi! How‘s it going?")

    elif phrase == "What is your name?":

        print("I don't have name :(")
    elif phrase=="я устал":
        print('«Ты больше не хочешь со мной говорить?')
        phrase = input("Your message: ")
        if phrase=="нет":
            print("Ну, поговори еще со мной!")
    else:

        print("I don't understand you")