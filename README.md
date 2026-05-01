# Book Analyzer (CS I Project)

A Python-based library management system and text analysis tool. This project allows users to maintain a digital library of book URLs (primarily from Project Gutenberg) and perform frequency analysis on the text to identify the most common significant words.

## Features

- **Library Management**: 
  - Add new books with normalized titles and URLs.
  - Remove books using case-insensitive title matching.
  - Update existing book URLs.
- **Text Analysis**: 
  - Fetches raw text directly from web URLs using the `requests` library.
  - Cleans text by removing punctuation and converting to lowercase.
  - Filters out "stop words" using a comprehensive list of thousands of common English words.
  - Excludes short words (less than 3 characters) to focus on meaningful content.
- **Visualization**: 
  - Generates a horizontal bar chart in the terminal using ASCII characters (`█`) to represent word frequencies.

## Requirements

- Python 3.x
- `requests` library
