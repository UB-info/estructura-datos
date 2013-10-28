#author: Rafa Arquero Gimeno

#we need split
import string

#read field data in file
def field_parser(raw_field):
    return tuple(string.split(raw_field, "&&"))

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
            film = map(field_parser, string.split(raw[id], "|"))
            M[id] = film    
    except IOError:
        #file not found
        print "[!] peliculas100.dat not found"

    return M
    
def main():    
    data = parser()

    #field names
    film_headers = ["title", "director", "cast", "producer", "writer", "country", "language", "year", "genres", "votes", "rating", "runtime", "plot", "cover url"]

    for film_id in xrange(len(data)):
        print "Film", film_id, ":"
        
        for field_id in xrange(len(data[film_id])):
            field = data[film_id][field_id]
            #print header
            print (4 * " ") + film_headers[field_id] + ": ",
            #print field, multiples joined by commas
            print "\t" + string.join(field, ", ") 
    
main()
