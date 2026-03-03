# Static Site Generator

A static site generator built from scratch in Python. This project takes raw content (like Markdown) and converts it into a structured tree of HTML nodes, which can then be rendered into static HTML files.

## Project Structure

- `src/` - Contains the Python source code for the static site generator.
  - `htmlnode.py`, `leafnode.py`, `parentnode.py` - Classes for representing and building HTML elements.
  - `textnode.py`, `inline_markdown.py` - Classes and functions for parsing inline text and Markdown into intermediate representations.
  - `main.py` - The entry point for the application.
  - `test_*.py` - Unit tests for the various components.
- `public/` - The destination folder for the generated static site (e.g., `index.html`, `styles.css`).
- `main.sh` - Shell script to run the generator.
- `test.sh` - Shell script to execute the test suite.

## Getting Started

To run the application, execute the main script:
```bash
./main.sh
```

To run the unit tests and ensure everything is working correctly, run:
```bash
./test.sh
```

## Features
- Custom HTML Node representation (`HtmlNode`, `LeafNode`, `ParentNode`) to build nested HTML structures.
- Parses and converts text and Markdown elements into HTML.
- Modular, test-driven design with an extensive test suite.
