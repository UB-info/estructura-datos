from ABB_Rafael_Arquero import *
import parserLastFM 

def main():
    users = ABB()
    parser = parserLastFM.parser('LastFM_small.dat', users, 100)#100 by 100
   
    parser.next()#Load 100
    #load 100 + 100
    #parser.next()
    #
    

    users.inorder()
    
    users.swap()
    users.inorder()
    
    print users.depth()

main()
