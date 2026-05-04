# Book Analyzer — CS I Project

Author: Alejandro Martinez  
GitHub: https://github.com/AlejandroMartinez-05/CS-Final-Project

A menu‑driven Python program that manages a personal library of books, downloads text from Project Gutenberg, processes the text, and displays the most frequent words. The program also supports book ratings and basic input validation.

## Features

### Library Management
- Add, remove, and update books  
- Case‑insensitive matching  
- Duplicate prevention  
- Titles normalized to lowercase  

### Text Analysis
- Fetch book text using `requests`  
- Clean and tokenize text  
- Remove stop words loaded from `EN-Stopwords.txt`  
- Count word frequencies using `collections.Counter`  
- Display top 10 most common words  

### Visualization
- ASCII bar chart showing word frequency  

### Extra Credit
- Lowercase storage for book titles  
- Rating system (1–5 stars) stored in memory  

## Concepts Practiced
- Functions  
- Loops and menu‑driven programs  
- Lists and filtering  
- Dictionaries  
- Regular expressions  
- API requests  
- Counters and frequency analysis

## Requirements

- Python 3.x
- `requests` library
