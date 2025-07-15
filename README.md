# Data Extraction from URL with Text Analysis

## Overview

The **Data Extraction From URL** project is designed to extract article titles and text from specified URLs and perform sentiment analysis on the extracted text. The project utilizes web scraping techniques to gather data and natural language processing (NLP) to analyze the sentiment and complexity of the text. The results are then saved to an Excel file for further analysis.

## Features

- **Web Scraping**: Extract article titles and content from provided URLs using BeautifulSoup.
- **Sentiment Analysis**: Analyze the sentiment of the extracted text using NLTK's Sentiment Intensity Analyzer.
- **Text Complexity Metrics**: Calculate various metrics such as average sentence length, percentage of complex words, FOG index, and more.
- **Input/Output Handling**: Read input data from an Excel file and save the results to another Excel file.

## Technologies Used

- Python
- Pandas
- Requests
- BeautifulSoup
- NLTK
- OpenPyXL
