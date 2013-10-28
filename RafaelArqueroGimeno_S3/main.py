from new import *
from old import Film, parser
import test

def main():
    movieList = parser('peliculas100.dat')
    movieList = movieList[:20]

    test.stack(movieList)
    test.queue(movieList)
    

main()
    


    
