class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string and between 5 and 50 characters.")
        
        self.author = author
        self.magazine = magazine
        self.title = title

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        
        self.name = name
        self._articles = []  # Store articles as an internal list
    
    @property
    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.articles.append(article)
        return article

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    all_magazines = []  # Class-level list to track all magazine instances
    
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        
        self.name = name
        self.category = category
        self._articles = []  # Internal list to store articles
    
        Magazine.all_magazines.append(self)

    @property
    def articles(self):
        return self._articles
    
    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            authors_count[article.author] = authors_count.get(article.author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda magazine: len(magazine.articles))

# Testing the implementation:
# Create some authors and magazines to see if everything works as expected.

author1 = Author("John Doe")
author2 = Author("Jane Smith")

mag1 = Magazine("Tech Today", "Technology")
mag2 = Magazine("Health Weekly", "Health")

# Add articles
article1 = author1.add_article(mag1, "The Future of AI")
article2 = author1.add_article(mag1, "Advancements in Robotics")
article3 = author2.add_article(mag1, "The Rise of Quantum Computing")
article4 = author1.add_article(mag2, "New Trends in Healthcare")

# Check some properties
print(f"Articles by {author1.name}: {[article.title for article in author1.articles]}")
print(f"Magazines by {author1.name}: {[mag.name for mag in author1.magazines()]}")
print(f"Topic areas by {author1.name}: {author1.topic_areas()}")
print(f"Contributors to {mag1.name}: {[author.name for author in mag1.contributors()]}")
print(f"Authors with more than 2 publications in {mag1.name}: {[author.name for author in mag1.contributing_authors()]}")
print(f"Magazine with most articles: {Magazine.top_publisher().name}")
