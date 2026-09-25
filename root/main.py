state = "coding"

while True:
    if state == "coding":
        print("You are coding!")
        while True:
            feeling = input("How are you feeling? ").lower()
            if feeling == "tired" or feeling == "hungry" or feeling == "happy":
                if feeling == "tired":
                    state = "sleeping"
                elif feeling == "hungry":
                    state = "eating"
                else:
                    state = "coding"
                break
            else:
                print("Invalid feeling, try again.")

    elif state == "eating":
        print("You are eating!")
        while True:
            feeling = input("How are you feeling? ").lower()
            if feeling == "hungry" or feeling == "full" or feeling == "tired":
                if feeling == "hungry":
                    state = "eating"
                elif feeling == "full":
                    state = "coding"
                else:
                    state = "sleeping"
                break
            else:
                print("Invalid feeling, try again.")

    elif state == "sleeping":
        print("You are sleeping!")
        while True:
            feeling = input("How are you feeling? ").lower()
            if feeling == "hungry" or feeling == "awake" or feeling == "tired":
                if feeling == "hungry":
                    state = "eating"
                elif feeling == "awake":
                    state = "coding"
                else:
                    state = "sleeping"
                break
            else:
                print("Invalid feeling, try again.")