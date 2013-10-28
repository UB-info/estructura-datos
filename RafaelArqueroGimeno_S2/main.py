#author: Rafa Arquero Gimeno

#we need split
import string
from film import Film

#read field data in file
def field_parser(raw_field):
    return string.split(raw_field, "&&")

def parser():
    #init matrix
    M = []

    #the file could not be here, so...
    try:
        raw = open("./peliculas100.dat")
        raw = file.readlines(raw)

        #trick: avoid append => performance boost
        M = [0] * len(raw)
        
        #each line in file is an entire film
        for id in xrange(len(raw)):
            #gets film's fields, and the field_parser function will parse them
            M[id] = Film()
            M[id].fromlist(map(field_parser, string.split(raw[id], "|")))
    except IOError:
        #file not found
        print "[!] peliculas100.dat not found"

    return M
    
def main():    
    films = parser()

    #field names
    film_headers = ["title", "director", "cast", "producer", "writer", "country", "language", "year", "genres", "votes", "rating", "runtime", "plot", "cover url"]

    for film_id in xrange(len(films)):
        print "Film", film_id + 1, ":"        
        print films[film_id]
    
main()
