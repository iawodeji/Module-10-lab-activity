class Chapter1:
    def __init__(self):
        self.phone_found = False
        self.documents_found = False
        self.workers_interviewed = False

    def intro(self):
        print("Chapter 1: The Disappearance")
        print("The game begins with a news report about Carter Jones’ sudden disappearance.")
        print("His car was found abandoned near an incomplete building, and there are no leads.\n")
        print("Your editor calls you into his office and assigns you to the case.")
        print("You must visit the incomplete building where Carter’s car was found.\n")

    def investigate_car(self):
        if self.documents_found:
            print("You already found documents in the car.")
        else:
            print("You approach Carter’s car, which is still parked near the incomplete building.")
            print("The car door is slightly ajar, and you notice some documents scattered on the passenger seat.")
            print("You carefully examine the car for any clues...\n")
            self.documents_found = True
            return "You found some documents in the car."

    def talk_to_workers(self):
        if self.workers_interviewed:
            print("You already talked with the workers.")
        else:
            print("You decide to talk to the workers who were previously working on the building.")
            print("They seem hesitant at first, but one of them mentions seeing Carter arguing with someone near the car before he disappeared.\n")
            self.workers_interviewed = True
            return "A worker saw Carter arguing with someone."

    def find_phone(self):
        print("You search the debris around the building and eventually find a phone partially buried under some rubble.")
        print("The phone belongs to Carter, and you notice a cryptic message on the screen.")
        print("The last known GPS coordinates are also visible. This could be your first real lead!\n")
        return "Chapter 2: The Investigation Continues"

    def chapter1(self):
        self.intro()

        while not self.phone_found:
            print("Choose your action:")
            print("1. Investigate Carter’s car for any clues")
            print("2. Talk to the workers that were previously working on the building and nearby witnesses")
            print("3. Find Carter’s phone in the debris around the building (proceed to Chapter 2)")
            print("4. Stop Investigation and Exit")

            choice = input("Enter the number of your choice: ")

            if choice == "1":
                result = self.investigate_car()
                if result:
                    print(result)
            elif choice == "2":
                result = self.talk_to_workers()
                if result:
                    print(result)
            elif choice == "3":
                result = self.find_phone()
                print(result)
                self.phone_found = True  # Exit loop and proceed to Chapter 2
            elif choice == "4":
                print("Ending the investigation. Game over.")
                break
            else:
                print("Invalid choice. Please try again.")

        if self.phone_found:
            return "Proceeding to Chapter 2..."

# Example of running the chapter
if __name__ == "__main__":
    game_chapter1 = Chapter1()
    next_chapter = game_chapter1.chapter1()
    print(next_chapter)
