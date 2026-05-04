"""
Concepts We Are Practicing:
- Functions
- Loops and Menu-Driven Programs
- Lists and Data Filtering
- Dictionaries
- Counter (from collections)

Modules and Libraries:
- API Requests (requests)
- Text Processing (re - regular expressions)
"""

"""
Author: Alejandro Martinez
GitHub Link: https://github.com/AlejandroMartinez-05/CS-Final-Project
Project: Book Analyzer (CS I Project)
Extra credit:   I saved the book titles in lowercase to keep the naming consistent.
                I implemeted a new feature:  if choice == '6', user can now give books a 1-5 star rating, which the system saves and tracks automatically.
"""

import requests
import re
from collections import Counter


# -----------------------------
# INITIAL DATA
# -----------------------------

my_library = {
    "moby dick": "https://www.gutenberg.org/files/2701/2701-0.txt"
}

my_book_rating = {}

# TODO 3: Read stop words from a file instead; this file "EN-Stopwords" contains thousands stop words(2 points)
with open("EN-Stopwords.txt", "r") as f:
    STOP_WORDS = f.readlines()
    STOP_WORDS = [i.strip() for i in STOP_WORDS] #strpped newline character for every line

# -----------------------------
# FETCH BOOK
# -----------------------------
def fetch_book(url):
    """Download text from a URL."""
    # TODO 4: Handle exceptions (network errors, invalid URLs, etc.) (1 point)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error occured when fetching book: {e}")
    return response.text

# -----------------------------
# CLEAN TEXT
# -----------------------------
def clean_text(raw_text):
    """Lowercase text and remove punctuation."""
    text = raw_text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()

# -----------------------------
# ANALYZE TEXT
# -----------------------------
def analyze_text(words):
    """Remove stop words and count frequencies."""
    filtered_words = [] 
    for w in words: 
        if w not in STOP_WORDS and len(w) > 2:   #checking len(w)> 2 to remove tiny words((is, to, at))
            filtered_words.append(w)

    # print(f"STOP_WORDS: {STOP_WORDS}")
    # print(Counter(filtered_words).most_common(10))
    return Counter(filtered_words).most_common(10)



# -----------------------------
# VISUALIZATION (BAR CHART)
# -----------------------------
# TODO 5: Implement the following function (2 points)
# hints: use print() statements to create a horizontal bar chart using the "█" or "*" character.
def plot_results(stats, title):
    """Create a bar chart of word frequencies."""
    print(title)
    print(stats)
    for word, count in stats:
        print(f"{word.title()} appeard in {count} times")
        c = count // 100
        for i in range(c):
            print("█", end='')
        print(f"({count})")
    #pass

# -----------------------------
# MENU SYSTEM
# -----------------------------
def main():
    while True:
        print("\n--- LIBRARY MANAGER ---")
        print(f"Current Books: {list(my_library.keys())}")
        print("1. Add New Book")
        print("2. Remove Book")
        print("3. Update Book URL")
        print("4. Analyze a Book")
        print("5. Exit")
        print("6. Rate a Book")

        choice = input("\nSelect (1-6): ")

        if choice == '1':
            # Add new books to the dictionary (use this website: https://www.gutenberg.org/browse/scores/top)
            # TODO 1.1: Normalize input by removing extra spaces and ignoring case.
                # (e.g., " The Hobbit " (with space) and "the hobbit" should be treated as the same book.) (1 point)
            name = input("Enter Book Title: ")
            # Frankenstein
            url = input("Enter Gutenberg .txt URL: ")
            # https://www.gutenberg.org/ebooks/84.txt.utf-8

            copy_name = name.strip().lower()

            # TODO 1.2: Validate that the Book title or URL is not empty (1 point)
            if len(name) == 0:
                print("It can't be empty.") #if empty just print a message that "It can't be empty"
            if len(url) == 0:
                print("It can't be empty.")  #if empty just print a message that "It can't be empty"

            # TODO 1.3: Prevent duplicate book names (1 point)
            if copy_name not in my_library:
                my_library[copy_name] = url
                print(f"'{name}' added.")
            else:
                print(f"{name} already exists in your library.")

        elif choice == '2':
            # Remove books from the dictionary
            #TODO 2.1: Handle missing books—check if the title exists before trying to delete it.(1 point)
            #TODO 2.2: Make the removal case-insensitive so "The Hobbit" matches "the hobbit".(1 point)
            # Hint: Use .strip().lower() to normalize the user's input!
            name = input("Enter title to remove: ")
            new_name = name.strip().lower()
            
            if new_name in my_library:
                my_library.pop(new_name)
            else:
                print(f"{name} doesn't exist in Library.")
            

        elif choice == '3':
            # UPDATE OPERATION
            name_input = input("Enter the book title to update: ").strip().lower()
            target_key = None  # Start with None in case we don't find it

            for k in my_library:
                if k.lower() == name_input:
                    target_key = k
                    break  # We found it, so stop looking

            if target_key:
                print(f"Current URL: {my_library[target_key]}")
                new_url = input("Enter new URL: ").strip()
                if new_url == "":
                    print("Invalid URL. Update cancelled.")
                else:
                    my_library[target_key] = new_url
                    print(f"'{target_key}' updated successfully.")
            else:
                print("Book not found.")

        elif choice == '4':
            name_input = input("Which book to analyze? ").strip().lower()
            
            target_key = None
            for k in my_library:
                if k.lower() == name_input:
                    target_key = k
                    break

            if target_key:
                url = my_library[target_key]
                print(f"Fetching and analyzing '{target_key}'...")
                raw_text = fetch_book(url)

                if raw_text:
                    words = clean_text(raw_text)
                    stats = analyze_text(words)
                    plot_results(stats, target_key)
            else:
                print("Error: Book not found.")

        elif choice == '5':
            print("Goodbye!")
            break

        elif choice == '6':
            name_input = input("Which book to rate? ").strip().lower()
            #norm_book = name_input.strip().lower()
            
            if name_input not in my_book_rating:
                if name_input in my_library:
                    rate = input("What is your rate on this book from 1-5? ")
                    if rate.isdigit():
                        my_book_rating[name_input] = rate
                        print('*' * int(rate))
                    else:
                        print("Please enter a valid number.")
                else:
                    print("This book does not exist!")
            else:
                print("This book has already been rated!")

               
if __name__ == "__main__":
    main()
