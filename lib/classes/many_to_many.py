class Article:
    all = []  # Stores all article instances

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("title must be a non-empty string")

        self.author = author
        self.magazine = magazine
        self.title = title.strip()
        # Add this article to the magazine's articles list
        magazine.add_article(self)  # Ensure this article is added to the magazine's list
        Article.all.append(self)


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("name must be a non-empty string")
        self._name = name.strip()

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
        topics = {article.magazine.category for article in Article.all if article.author == self}
        return list(topics) if topics else None


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []  # Initialize _articles to hold articles for this magazine

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("category must be a string")
        if len(value.strip()) == 0:
            raise ValueError("category cannot be an empty string")
        self._category = value

    def articles(self):
        """Returns a list of all articles for this magazine."""
        return self._articles  # This returns the list of articles for the magazine

    def add_article(self, article):
        """Adds an article to this magazine."""
        self._articles.append(article)

    def contributors(self):
        """Returns a list of unique authors for this magazine."""
        return list({article.author for article in self.articles()})
        

    def article_titles(self):
        """Returns a list of titles for articles in this magazine, or None if no articles."""
        if not self._articles:  # If there are no articles, return None
            return None
        return [article.title for article in self._articles]
    
    def contributing_authors(self):
        """Returns a list of authors who have more than 2 articles in this magazine, or None if no such authors."""
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1

        # Filter authors who have more than 2 articles
        contributing_authors = [author for author, count in author_counts.items() if count > 2]

        # Return None if no author has more than 2 articles
        if not contributing_authors:
            return None

        return contributing_authors
