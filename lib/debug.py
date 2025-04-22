#!/usr/bin/env python3
import ipdb; ipdb.set_trace()



from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

# classes/many_to_many.py

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name.strip()) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({article.magazine.category for article in self.articles()})


class Magazine:
    _all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string.")
        if len(value.strip()) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        result = []
        for author in set(authors):
            if authors.count(author) > 2:
                result.append(author)
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls._all:
            return None
        return max(cls._all, key=lambda mag: len(mag.articles()), default=None)


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Must be an Author instance.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Must be a Magazine instance.")
        self._magazine = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed after initialization.")
        if not isinstance(value, str):
            raise TypeError("Title must be a string.")
        if not (5 <= len(value) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")
        self._title = value



if __name__ == '__main__':
    # don't remove this line, it's for debugging!
 ipdb.set_trace()
