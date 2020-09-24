#!/usr/bin/env python
# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import nltk
from newspaper import Article  


nltk.download('punkt')

def parse_url(link, file = None, file_name = None):

    article = Article(link)
    article.download()
    article.parse()
    article.nlp()
    source = article.source_url
    date = article.publish_date.strftime('%Y-%m-%d:%H:%M:%S')
    summary = article.summary
    Url= link
    content = article.text
    title = article.title
    
    # Remove new line characters
    summary = summary.replace('\n', ' ')
    content = content.replace('\n', ' ')
    title = title.replace('\n', ' ')
    
    return [date,source,summary,Url,content,title]






