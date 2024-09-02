class Chapter3:
    def __init__(self):
        self.eavesdrop_successful = False
        self.information_gathered = False
        self.evidence_captured = False

    def intro(self):
        print("Chapter 3: Into the Underworld")
        print("The address leads you to a shady part of the city known for its underground clubs and illegal activities.\n")
        print("You enter a dimly lit club where Carter was reportedly seen with a known criminal.\n")

    def follow_criminal(self):
        if self.information_gathered:
            print("You have already gathered information from the meeting.")
        else:
            print("You decide to follow the criminal to a secret meeting in the back alley.")
            print("You see a group of people discussing something in hushed tones. It seems important...\n")
            self.information_gathered = True
            return "You gathered information from the meeting."

    def take_photos(self):
        if self.evidence_captured:
            print("You have captured good enough evidence.")
        else:
            print("You take out your camera and carefully snap photos of the meeting for evidence.")
            print("The photos could be useful later as proof of the criminal activities...\n")
            self.evidence_captured = True
            return "You captured photographic evidence."

    def eavesdrop(self):
        print("You position yourself near the group and listen closely to their conversation.")
        print("You overhear a discussion about a secure office building where important documents are kept.")
        print("This information could be vital for your investigation. You decide to proceed to the next chapter.\n")
        self.eavesdrop_successful = True
        return "Chapter 4: The Secure Office Building"

    def go_back(self):
        print("You decide that more information is needed before proceeding further.")
        print("You leave the club and head back to the restaurant to interview more people.\n")
        return "Chapter 2: The Investigation Continues"

    def chapter3(self):
        self.intro()

        while not self.eavesdrop_successful:
            print("Choose your action:")
            print("1. Follow the criminal to a secret meeting in the back alley")
            print("2. Take photos of the meeting for evidence")
            print("3. Eavesdrop on conversations to gather information about a secure office building (proceed to Chapter 4)")
            print("4. Go back to the restaurant to interview more people (loops back to Chapter 2)")
            print("5. Stop Investigation and Exit")
            
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                result = self.follow_criminal()
                if result:
                    print(result)
            elif choice == "2":
                result = self.take_photos()
                if result:
                    print(result)
            elif choice == "3":
                result = self.eavesdrop()
                print(result)
            elif choice == "4":
                result = self.go_back()
                print(result)
                return result  # Loop back to Chapter 2
            elif choice == "5":
                print("Ending the investigation. Game over.")
                break
            else:
                print("Invalid choice. Please try again.")
        
        if self.eavesdrop_successful:
            return "Proceeding to Chapter 4..."

# Example of running the chapter
if __name__ == "__main__":
    chapter3_instance = Chapter3()
    next_chapter = chapter3_instance.chapter3()
    print(next_chapter)
