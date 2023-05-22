# -*- coding: utf-8 -*-
"""
@author: user - Sanket Jadhav
"""
# Import libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Function to extract article title and text from a URL
def extract_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title_element = soup.find('title')
    if title_element:
        title = title_element.text.strip()
    else:
        title = 'No title found'
        
    article_text = ''
    article_element = soup.find('article')
    if article_element:
        for tag in article_element(['script', 'style', 'a']):
            tag.extract()
        article_text = article_element.get_text(separator='\n').strip()
    
    return title, article_text

# Text analysis on the extracted article text
def analyze_text(article_text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(article_text)
    positive_score = sentiment_scores['pos']
    negative_score = sentiment_scores['neg']
    polarity_score = sentiment_scores['compound']
    subjectivity_score = sentiment_scores['compound'] + 1
    
    sentences = nltk.sent_tokenize(article_text)
    num_sentences = len(sentences)
    
    total_words = 0
    avg_sentence_length = 0
    if num_sentences > 0:
        total_words = sum(len(nltk.word_tokenize(sentence)) for sentence in sentences)
        avg_sentence_length = total_words / num_sentences
    
    words = nltk.word_tokenize(article_text)
    num_complex_words = sum(1 for word in words if len(word) > 2 and word.isalpha() and len(nltk.word_tokenize(word)) >= 2)
    percentage_complex = 0
    if len(words) > 0:
        percentage_complex = (num_complex_words / len(words)) * 100
    
    fog_index = 0
    if avg_sentence_length > 0:
        fog_index = 0.4 * (avg_sentence_length + percentage_complex)
    
    avg_words_per_sentence = 0
    if num_sentences > 0:
        avg_words_per_sentence = len(words) / num_sentences
    
    complex_word_count = num_complex_words
    word_count = len(words)
    
    syllables_per_word = 0
    if word_count > 0:
        syllables_per_word = sum(len(word) for word in words) / word_count
    
    personal_pronouns = sum(1 for word, pos in nltk.pos_tag(words) if pos == 'PRP')
    
    avg_word_length = 0
    if word_count > 0:
        avg_word_length = sum(len(word) for word in words) / word_count
    
    return positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length, \
           percentage_complex, fog_index, avg_words_per_sentence, complex_word_count, word_count, \
           syllables_per_word, personal_pronouns, avg_word_length

# Read the input file
input_file = 'Input.xlsx'
df_input = pd.read_excel(r"D:\07-SANKET\INTERN\Input.xlsx")

# Store the output data
url_ids = []
titles = []
article_texts = []
positive_scores = []
negative_scores = []
polarity_scores = []
subjectivity_scores = []
avg_sentence_lengths = []
percentage_complex_words = []
fog_indices = []
avg_words_per_sentences = []
complex_word_counts = []
word_counts = []
syllables_per_words = []
personal_pronouns = []
avg_word_lengths = []

# Iterate over each row in the input DataFrame
for index, row in df_input.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    
    # Extract article title and text from the URL
    title, article_text = extract_article(url)
    
    # Perform text analysis on the extracted article text
    positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length, \
    percentage_complex, fog_index, avg_words_per_sentence, complex_word_count, word_count, \
    syllables_per_word, personal_pronoun, avg_word_length = analyze_text(article_text)
    
    # Append the results to the lists
    url_ids.append(url_id)
    titles.append(title)
    article_texts.append(article_text)
    positive_scores.append(positive_score)
    negative_scores.append(negative_score)
    polarity_scores.append(polarity_score)
    subjectivity_scores.append(subjectivity_score)
    avg_sentence_lengths.append(avg_sentence_length)
    percentage_complex_words.append(percentage_complex)
    fog_indices.append(fog_index)
    avg_words_per_sentences.append(avg_words_per_sentence)
    complex_word_counts.append(complex_word_count)
    word_counts.append(word_count)
    syllables_per_words.append(syllables_per_word)
    personal_pronouns.append(personal_pronoun)
    avg_word_lengths.append(avg_word_length)

# Create the output DataFrame
df_output = pd.DataFrame({
    'URL_ID': url_ids,
    'Title': titles,
    'Article Text': article_texts,
    'Positive Score': positive_scores,
    'Negative Score': negative_scores,
    'Polarity Score': polarity_scores,
    'Subjectivity Score': subjectivity_scores,
    'Avg Sentence Length': avg_sentence_lengths,
    'Percentage of Complex Words': percentage_complex_words,
    'FOG Index': fog_indices,
    'Avg Number of Words per Sentence': avg_words_per_sentences,
    'Complex Word Count': complex_word_counts,
    'Word Count': word_counts,
    'Syllables per Word': syllables_per_words,
    'Personal Pronouns': personal_pronouns,
    'Avg Word Length': avg_word_lengths
})

# Save the output to the output file
output_file = r'D:\07-SANKET\INTERN\Output.xlsx'
df_output.to_excel(output_file, index=False)
