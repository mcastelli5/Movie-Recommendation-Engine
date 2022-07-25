class User:
    def __init__(self):
        self.name = None
        self.search_terms = []
        self.fav_movie = []
    
    def get_genres(self):
        genres = input("What Movie Genre are you interested in (if multiple, please separate them with a comma)? [Type 'skip' to skip this question] ")
        genres = " ".join(["".join(n.split()) for n in genres.lower().split(',')])
        return genres

    def get_keywords(self):
        keywords = input("What are some of the keywords that describe the movie you want to watch, like elements of the plot, whether or not it is about friendship, etc? (if multiple, please separate them with a comma)? [Type 'skip' to skip this question] ")
        keywords = " ".join(["".join(n.split()) for n in keywords.lower().split(',')])
        return keywords
    
    def get_fav_movie(self):
        fav_movie = input("What is one of your favorite movies?")
        fav_movie = " ".join(["".join(n.split()) for n in fav_movie.lower().split(',')])
        return fav_movie
        
    def set_fav_movie(self):
        self.fav_movie = self.get_fav_movie()

    def get_searchTerms(self):
        genres = self.get_genres()
        if genres != 'skip':
            self.search_terms.append(genres)

        keywords = self.get_keywords()
        if keywords != 'skip':
            self.search_terms.append(keywords)