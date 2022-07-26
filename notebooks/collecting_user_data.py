import difflib

class User:
    def __init__(self):
        self.name = None
        self.search_terms = []
        self.fav_movie = None
    
    def get_genres(self):
        genres = input("What Movie Genre are you interested in (if multiple, please separate them with a comma)? [Type 'skip' to skip this question] ")
        genres = " ".join(["".join(n.split()) for n in genres.lower().split(',')])
        return genres

    def get_keywords(self):
        keywords = input("What are some of the keywords that describe the movie you want to watch, like elements of the plot, whether or not it is about friendship, etc? (if multiple, please separate them with a comma)? [Type 'skip' to skip this question] ")
        keywords = " ".join(["".join(n.split()) for n in keywords.lower().split(',')])
        return keywords
    
    def get_fav_movie(self, titles):
        confirmations = {"yes", "yep", "ye", "yeah", "yessir"}
        fav_movie = input("What is one of your favorite movies?")
        fav_movie = " ".join(["".join(n.split()) for n in fav_movie.lower().split(',')])
        if fav_movie.lower() == "skip" or fav_movie is None:
            self.fav_movie = None
            return
        else:
            closest_titles = difflib.get_close_matches(fav_movie, titles)
            for movie in closest_titles:
                is_movie = input(f"Did you mean {movie}? (yes or no)")
                if is_movie.lower() in confirmations:
                    self.fav_movie = movie
                    return
            try_again = input("Hmmmm I don't think I know that movie, would you like to try again?")
            if try_again in confirmations:
                self.get_fav_movie(titles)
            else:
                return
        

    def get_searchTerms(self):
        genres = self.get_genres()
        if genres != 'skip':
            self.search_terms.append(genres)

        keywords = self.get_keywords()
        if keywords != 'skip':
            self.search_terms.append(keywords)