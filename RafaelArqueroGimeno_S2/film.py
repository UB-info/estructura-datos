import string

class Film:
    
    #static atrbiute
    fields = ["title", "director", "cast", "producer", "writer", "country", "language", "year", "genres", "votes", "rating", "runtime", "plot", "cover_url"]
    
    def __init__(self):
                
        self.title    = "Sin titulo"
        self.director = ""
        self.cast     = ""
        self.producer = ""
        self.writer   = ""
        self.country  = ""
        self.language = ""
        self.year     = 0
        self.genres   = ""
        self.votes    = 0
        self.rating   = 0.0
        self.runtime  = 0
        self.plot     = ""
        self.cover_url  = ""
        
    def fromlist(self, values):        
        for i in xrange(len(values)):       
            setattr(self, Film.fields[i], values[i])    
            
    '''def fromrawdata(self, rawdata):
        print "i"'''
    
    def __str__(self):        
        out = ""
        for field in Film.fields:
            out += ("    %s:\t %s\n" %  (field, string.join(getattr(self, field), ", ")))
        
        return out

'''f = Film()
f.fromlist(["sin titulo", "sin director", "blablabla"])

print f.title, f.director'''