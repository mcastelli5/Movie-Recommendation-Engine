def get_genres():
  genres = input("What Movie Genre are you interested in (if multiple, please separate them with a comma)? [Type 'skip' to skip this question] ")
  genres = " ".join(["".join(n.split()) for n in genres.lower().split(',')])
  return genres

def get_keywords():
  keywords = input("What are some of the keywords that describe the movie you want to watch, like elements of the plot, whether or not it is about friendship, etc? (if multiple, please separate them with a comma)? [Type 'skip' to skip this question] ")
  keywords = " ".join(["".join(n.split()) for n in keywords.lower().split(',')])
  return keywords

def get_searchTerms():
  searchTerms = [] 
  genres = get_genres()
  if genres != 'skip':
    searchTerms.append(genres)

  keywords = get_keywords()
  if keywords != 'skip':
    searchTerms.append(keywords)
  
  return searchTerms