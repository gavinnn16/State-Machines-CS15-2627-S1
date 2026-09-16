state = "coding"

while True:
    if state == "coding":
        print("\nYou are currently coding!")
        while True:
            print("How are you feeling? (tired, hungry, boredbo)")
            feeling = input().strip().lower()
            if feeling in ["tired", "hungry", "bored"]:
                if feeling == "tired":
                    state = "sleeping"
                elif feeling == "hungry":
                    state = "eating"
                elif feeling == "bored":
                    state = "gaming"
                break
            else:
                print("Invalid feeling, please try again.")

    elif state == "eating":
        print("\nYou are currently eating!")
        while True:
            print("How are you feeling? (full, tired, bored)")
            feeling = input().strip().lower()
            if feeling in ["full", "tired", "bored"]:
                if feeling == "full":
                    state = "coding"
                elif feeling == "tired":
                    state = "sleeping"
                elif feeling == "bored":
                    state = "gaming"
                break
            else:
                print("Invalid feeling, please try again.")

    elif state == "sleeping":
        print("\nYou are currently sleeping!")
        while True:
            print("How are you feeling? (hungry, awake, bored)")
            feeling = input().strip().lower()
            if feeling in ["hungry", "awake", "bored"]:
                if feeling == "hungry":
                    state = "eating"
                elif feeling == "awake":
                    state = "coding"
                elif feeling == "bored":
                    state = "gaming"
                break
            else:
                print("Invalid feeling, please try again.")

    elif state == "gaming":
        print("\nYou are currently gaming!")
        while True:
            print("How are you feeling? (tired, hungry, focused)")
            feeling = input().strip().lower()
            if feeling in ["tired", "hungry", "focused"]:
                if feeling == "tired":
                    state = "sleeping"
                elif feeling == "hungry":
                    state = "eating"
                elif feeling == "focused":
                    state = "coding"
                break
            else:
                print("Invalid feeling, please try again.")