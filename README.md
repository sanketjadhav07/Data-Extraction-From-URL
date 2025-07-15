# Data Extraction from URL with Text Analysis

## Overview

The **Data Extraction from URL with Text Analysis** project is a Python-based tool designed to extract article content from specified URLs and perform in-depth text analysis. This tool is particularly useful for researchers, data analysts, and developers interested in sentiment analysis, readability metrics, and content summarization.

The project leverages popular libraries such as `BeautifulSoup` for web scraping and `NLTK` for natural language processing, providing a comprehensive solution for analyzing textual data from online sources.

## Features

- **Web Scraping**: Efficiently extracts article titles and content from a list of URLs.
- **Sentiment Analysis**: Utilizes NLTK's VADER sentiment analysis tool to evaluate the emotional tone of the text.
- **Text Complexity Metrics**: Calculates various readability and complexity metrics, including:
  - FOG Index
  - Average Sentence Length
  - Percentage of Complex Words
  - Word Count and Syllables per Word
- **Excel Integration**: Reads input from and writes output to Excel files, making it easy to manage data.
- **Error Handling**: Robust handling of HTTP requests to manage inaccessible URLs gracefully.

## Libraries

Pandas

requests

beautifulsoup4

nltk

openpyxl
