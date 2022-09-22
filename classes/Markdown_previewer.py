from customtkinter import *
import random
from helpers import create_error
from markdown import markdown
from bs4 import BeautifulSoup
from html.parser import HTMLParser


class MarkdownPreviewer():
    def __init__(self, canvas):
        self.canvas = canvas

        self.markdown_text_label = CTkLabel(text='Votre Markdown')
        self.canvas.create_window(200, 30, window=self.markdown_text_label)

        self.markdown_text = CTkEntry(width=300, height=100, bg_color='gray12')
        self.canvas.create_window(200, 110, window=self.markdown_text)

    def valid(self):
        value = self.markdown_text.get()

        html_text = markdown(value)
        #soup = BeautifulSoup(html_text)
        #text = soup.get_text('\n')
        #print(text)

        f = HTMLFilter()
        f.feed(html_text)
        print(f.text)

        #return text


class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data