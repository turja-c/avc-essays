
from asyncio.log import logger
import feedparser
import urllib.request
import time
import os.path
import html2text
import unidecode
import regex as re
from htmldate import find_date
import csv

rss = feedparser.parse("https://feeds.feedburner.com/avc")
h = html2text.HTML2Text()

print(h)