"""
Word Count Data Processing Tool
Christian Doss
An OOP-based program that displays a menu of 4 predefined text files, lets the user choose one, then reads and analyzes that file. The program will count the frequency of every word in the selected file and print an alphabetical report. 
10/8/26
"""

import string
from pathlib import Path



class WordAnalyzer:
    def __init__(self,filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        if not self.__filepath.exists():
            print(f"Error: The file '{self.__filepath}' could not be found.")
            return False

        try:

            text = self.__filepath.read_text(encoding='utf-8')
            text = text.lower()
            clean_text = text.translate(str.maketrans('', '', string.punctuation))
            words = clean_text.split()

            for word in words:
                if word in self.__frequencies:
                    self.__frequencies[word] += 1
                else:
                    self.__frequencies[word] = 1               
            return True
        
        except FileNotFoundError:
            print(f"Error: Could not locate or open {self.__filepath}.")
            return False

    def print_report(self):
        sorted_words = sorted(self.__frequencies.keys())
        
        for word in sorted_words:
            print(f"{word} :: {self.__frequencies[word]}")


def main():
    txt_dict = {
        "1": {"name": "Monte Cristo (Chapter 1)", "path": Path("monte_cristo.txt")},
        "2": {"name": "Princess Mars (Chapter 1)", "path": Path("princess_mars.txt")},
        "3": {"name": "Tarzan (Chapter 1)", "path": Path("Tarzan.txt")},
        "4": {"name": "Treasure Island (Chapter 1)", "path": Path("treasure_island.txt")}
    }

    while True:
        print("Word Analyzer")
        print("\nPlease select a file to analyze:\n")

        for key, file_info in txt_dict.items():
            print(f"{key}. {file_info['name']}")
        print("5. Exit")
        selection = input("\nEnter your choice (1-5): ").strip()

        if selection == "5":
            print("Goodbye!")
            break

        elif selection in txt_dict:
            selection_selected = txt_dict[selection]
            file_path = str(selection_selected['path'])
            print(f"\nProcessing '{selection_selected['path']}'...")
            analyzer = WordAnalyzer(file_path)
            if analyzer.process_file():
                analyzer.print_report()
            input("\nPress Enter to return to the main menu.")

        else:
            print("Invalid Input. Please select from choices 1-5")
            input("\nPress Enter to return to the main menu.")

if __name__ == "__main__":
    main()