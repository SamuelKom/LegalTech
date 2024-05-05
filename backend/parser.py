from typing import List
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
import numpy
import spacy
import random
from copy import deepcopy

from backend.structure import ParseInfo

class Parser:
    def __init__(self) -> None:
        #nltk.download('popular')
        #nltk.download('punkt')
        #nltk.download('averaged_perceptron_tagger')
        #nltk.download('maxent_ne_chunker')
        #nltk.download('words')
        #self.nlp = spacy.load("en_core_web_sm")
        self.nlp = spacy.load("de_core_news_sm")

    def split_sources(self, msg: str) -> List[str]:
        raise NotImplementedError
    
    def __get_delimiter(self, book: str, delimiters: List[str]) -> str:
        res = {}
        for keys in book:
            res[keys] = res.get(keys, 0) + 1
        delimiter_counts = {delimiter: res.get(delimiter, 0) for delimiter in delimiters}
        delimiter_char = max(delimiter_counts, key=delimiter_counts.get)
        print("delimiter: " + delimiter_char)
        return delimiter_char
    
    def __get_volume(self, book: str, delimiter: str) -> List:
        key_words = ["Auflage", "Volume"]
        for part in book.split(delimiter):
            for key in key_words:
                if key in part:
                    volume = re.findall(r'\d+', part)
                    if(len(volume) > 1):
                        raise ValueError("only one volume number possible")
                    return [int(volume[0]), True]
        return [1, False]
    
    def __get_authors(self, book) -> List[str]:
        #tokens = nltk.word_tokenize(book)
        #tagged = nltk.pos_tag(tokens)
        #entities = nltk.chunk.ne_chunk(tagged)
        #print(entities)
        #tokens = word_tokenize(book)
        #tagged = pos_tag(tokens)
        #named_entities = ne_chunk(tagged)
        #names = []
        #for entity in named_entities:
        #    if hasattr(entity, 'label') and entity.label() == 'PERSON':
        #        names.append(' '.join([token for token, tag in entity]))
        #print(names)
        #for word in book.split(" "):
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        w = url_pattern.sub('', book)
        w = re.sub("[^A-Za-z0-9 ]+", "", w)#.split()
        #random.shuffle(w)
        #w = ' '.join(w)

        doc = self.nlp(w)
        lst = []
        for ent in doc.ents:
            #print(ent.text, ent.label_)
            if(ent.label_ == "PER"):
                for i in ent.text.split():
                    if i not in lst:
                        lst.append(i)
        return lst

    def __get_title(self, book, delimiter, authors) -> str:
        w = deepcopy(book)
        for name in authors:
            w = w.replace(name, "")
        w = ' '.join(w.split()).strip()
        w = re.sub("[^A-Za-z0-9 " + delimiter + "]+", "", w)
        res = [{"string": w, "len": len(w)} for w in w.split(delimiter)]
        res = sorted(res, key=lambda x: x['len'], reverse=True)
        return res[0]["string"] #+ " " + res[1]["string"]
    
    def __get_year(self, book):
        raise NotImplementedError
    
    def get_data_obj(self, book: str, delimiters: List[str]) -> ParseInfo:
        delimiter = self.__get_delimiter(book, delimiters)
        volume, found_volume = self.__get_volume(book, delimiter)
        authors = self.__get_authors(book)
        title = self.__get_title(book, delimiter, authors)
        return ParseInfo(title, authors, 999, volume, found_volume)
