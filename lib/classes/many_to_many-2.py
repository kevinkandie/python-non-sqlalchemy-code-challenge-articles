class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []
    
    def add_article(self, article):
        if article not in self.articles:
            self.articles.append(article)
    
    def magazines(self):
        """Returns a list of unique magazines this author has published in"""
        return list(set(article.magazine for article in self.articles))


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []
    
    def add_article(self, article):
        if article not in self.articles:
            self.articles.append(article)
    
    def contributors(self):
        """Returns a list of unique authors who have published in this magazine"""
        return list(set(article.author for article in self.articles))


class Article:
    all = []
    
    
    def __init__(self, author, magazine, title):
        # Validate the input types
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("title must be a non-empty string")

        # Set the instance attributes
        self.author = author
        self.magazine = magazine
        self.title = title.strip()
        
        # Append the article to the global list of all articles
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        # Title is immutable, so we don't change it
        pass
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        # Remove from old author's articles if there was one
        if self._author and self in self._author.articles:
            self._author.articles.remove(self)
        
        # Set new author
        self._author = author
        
        # Add to new author's articles
        if author and self not in author.articles:
            author.add_article(self)
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        # Remove from old magazine's articles if there was one
        if self._magazine and self in self._magazine.articles:
            self._magazine.articles.remove(self)
        
        # Set new magazine
        self._magazine = magazine
        
        # Add to new magazine's articles
        if magazine and self not in magazine.articles:
            magazine.add_article(self)