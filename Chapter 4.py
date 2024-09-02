class Chapter4:
    def __init__(self):
        self.puzzle_solved = False
        self.guards_sneaked_past = False
        self.documents_found = False

    def intro(self):
        print("Chapter 4: The Conspiracy Unveiled")
        print("The evidence points to a larger conspiracy involving powerful city officials and criminal organizations.\n")
        print("You break into a secure office building to find incriminating documents.\n")

    def sneak_past_guards(self):
        if self.guards_sneaked_past:
            print("You already sneaked past the guards.")
        else:
            print("You carefully navigate through the building, avoiding guards and surveillance cameras.")
            print("Your stealth skills are put to the test as you move silently through the corridors...\n")
            self.guards_sneaked_past = True
            return "You successfully sneaked past the guards."

    def find_documents(self):
        if self.documents_found:
            print("Crucial evidence has been gathered.")
        else:
            print("You search the office and find a set of documents that prove the conspiracy.")
            print("You take pictures of the documents for later use...\n")
            self.documents_found = True
            return "You gathered crucial evidence."

    def solve_puzzles(self):
        print("You encounter a series of security puzzles that you must solve to bypass the building's security system.")
        print("With patience and skill, you manage to deactivate the alarms and unlock the exit. You escape without getting caught!\n")
        self.puzzle_solved = True
        return "Chapter 5: The Final Confrontation"

    def return_to_club(self):
        print("You decide to leave the office building and return to the club to gather more evidence.")
        print("There might be more information you missed at the club...\n")
        return "Chapter 3: Into the Underworld"

    def play(self):
        self.intro()
        
        while not self.puzzle_solved:
            print("Choose your action:")
            print("1. Sneak past guards and surveillance cameras")
            print("2. Find and take pictures of documents proving the conspiracy")
            print("3. Solve puzzles to bypass the building’s security system and escape without getting caught (proceed to Chapter 5)")
            print("4. Return to the club to find more evidence (loops back to Chapter 3)")
            print("5. Stop Investigation and Exit")
            
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                result = self.sneak_past_guards()
                if result:
                    print(result)
            elif choice == "2":
                result = self.find_documents()
                if result:
                    print(result)
            elif choice == "3":
                result = self.solve_puzzles()
                print(result)
            elif choice == "4":
                result = self.return_to_club()
                print(result)
                return result  # Loop back to Chapter 3
            elif choice == "5":
                print("Ending the investigation. Game over.")
                break
            else:
                print("Invalid choice. Please try again.")
        
        if self.puzzle_solved:
            return "Proceeding to Chapter 5..."

# Example of running the chapter
if __name__ == "__main__":
    chapter4 = Chapter4()
    next_chapter = chapter4.play()
    print(next_chapter)
