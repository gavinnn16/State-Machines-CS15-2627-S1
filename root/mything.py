state = "coding"

while True:
    if state == "coding":
        print("You are coding!")
        while True:
            print("How are you feeling? (tired, hungry, happy)")
            feeling = input().lower()
            if feeling in ["tired", "hungry", "happy"]:
                if feeling == "tired":
                    state = "sleeping"
                elif feeling == "hungry":
                    state = "eating"
                else:
                    state = "coding"
                break

    elif state == "eating":
        print("You are eating!")
        while True:
            print("How are you feeling?")
            feeling = input().lower()
            if feeling in ["hungry", "full", "tired"]:
                if feeling == "hungry":
                    state = "eating"
                elif feeling == "full":
                    state = "coding"
                else:
                    state = "sleeping"
                break

    elif state == "sleeping":
        print("You are sleeping!")
        while True:
            print("How are you feeling?")
            feeling = input().lower()
            if feeling in ["hungry", "awake", "tired"]:
                if feeling == "hungry":
                    state = "eating"
                elif feeling == "awake":
                    state = "coding"
                else:
                    state = "sleeping"
                break