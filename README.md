Books in Browsers: Enable Links in Archive.org Books
This project aims to enhance the accessibility and preservation of URLs in digitized books on Archive.org. It extracts URLs from OCR text, validates them, archives valid URLs in the Wayback Machine, and makes URLs clickable in a simplified Book Reader interface.

Features
URL Extraction:

Extracts URLs from OCR text using regex.

Handles imperfect URLs with extra spaces (e.g., "http:// example .com" → "http://example.com").

URL Validation:

Validates URLs using HTTP HEAD requests.

Logs valid and invalid URLs in urls.json.

Wayback Archiving:

Archives valid URLs using the Wayback Machine’s Save Page Now API.

Book Reader Prototype:

A simplified Book Reader interface with clickable URLs.

Highlights valid URLs and marks invalid URLs with a strikethrough.

Technologies Used
Programming Languages: Python, JavaScript

Frameworks: Flask (for the Book Reader prototype)

APIs: Wayback Machine Save Page Now API, Internet Archive OCR API

Tools: Regex, JSON, Git


How It Works
URL Extraction:

The script reads OCR text from sample_ocr.txt.

Uses regex to extract URLs and cleans them (removes extra spaces, ensures proper domain suffixes).

URL Validation:

Validates URLs using HTTP HEAD requests.

Logs valid and invalid URLs in urls.json.

Wayback Archiving:

Archives valid URLs using the Wayback Machine’s Save Page Now API.

Book Reader Prototype:

Displays the OCR text with clickable URLs.

Valid URLs are highlighted and clickable; invalid URLs are marked with a strikethrough.


Acknowledgments
Internet Archive for providing access to digitized books.

Wayback Machine for archiving URLs.





```mermaid
graph TD
    A[Start] --> B[Read OCR Text from sample_ocr.txt]
    B --> C[Extract URLs using Regex]
    C --> D[Clean URLs]
    D --> E[Save Extracted URLs to urls.json]
    E --> F[Validate URLs using HTTP HEAD Requests]
    F --> G{Is URL Valid?}
    G -->|Yes| H[Archive URL using Wayback Machine Save Page Now API]
    G -->|No| I[Mark URL as Invalid in urls.json]
    H --> J[Log Archived URL with Wayback Link in urls.json]
    I --> K[Log Invalid URL in urls.json]
    J --> L[Fetch OCR Text for Each Page using Internet Archive API]
    K --> L
    L --> M[Highlight URLs and Make Them Clickable in Book Reader]
    M --> N[Display Book Reader Interface with Clickable URLs]
    N --> O[End]




Contact
For questions or feedback, feel free to reach out:

Name: Rajdeep Jaiswal

Email: rajdeepjaiswal25nov@gmail.com

