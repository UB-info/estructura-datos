import string

class Film:
    __slots__ = ('title', 'director', 'cast', 'producer', 'writer', 'country', 'language', 'year', \
                'genres', 'votes', 'rating', 'runtime', 'plot', 'cover_url')
    #slots make it slightly faster and lighter.
    
    def __init__(self, *args):

        #initializing default attribute values
        for field in Film.__slots__:
            setattr(self, field, "empty" + field)

        #putting args into attributes
        for i in xrange(min(len(args), len(Film.__slots__))):
            setattr(self, Film.__slots__[i], args[i])

    def getTitle(self):
        return self.title[0]

def parser(filename):
    with open(filename) as f: # Handles file manipulation automagically.
        raw = file.readlines(f)
        return [Film(*map(lambda field: string.split(field, '&&'), string.split(line, '|'))) for line in raw]
        # * symbol allow us to pass list fields as args
