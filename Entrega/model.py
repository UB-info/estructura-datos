class User:
    def __init__(self, uid, age, gender, country, songs_played):        
        self.__uid          = uid       
        self.__age          = age       
        self.__gender       = gender       
        self.__country      = country      
        self.__songs_played = songs_played

        #print max(songs_played) == songs_played[0]#debug

        self.__most_played  = songs_played[0]#assume that are already sorted (I check it before)
        #if we dont asume that artists are already sorted...
        #self.__most_played  = max(songs_played)

        sum_times           = reduce(lambda x, y: x + y.times, songs_played, 0)#sumatory of times of all artists
        coef                = 1.0 * self.__most_played.times / sum_times#percentage of the best respect total
        
        self.__relevance    = coef

    def __str__(self):
        out = ""
        out += "User: " + self.__uid[:16] + "..." + "\n"#id is ellided, is too long!
        out += "Country: " + self.__country + "\n"
        out += "Age: " + str(self.__age) + "\n"
        out += "Gender: " + str(self.__gender) + "\n"
        out += "Most Played: " + self.__most_played.name + "\n"
        out += "Relevance: " + '{0:.2%}'.format(self.__relevance) + "\n"#percentage formating
        return out

    def __cmp__(self, other):
        return cmp(self.__uid, other.uid())

    def uid(self):
        #relevance getter
        return self.__uid

class Artist:
    __slots__ = ('name', 'times')

    def __init__(self, *args):
            self.name  = args[0]
            #I found corruption in big.dat file. An artist parsed without times (i.e. no "::" to split)
            if len(args) > 1:#times is provided
                self.times = int(args[1])
            else:#times is not provided
                self.times = 0   
            
    def __str__(self):
        return self.name + ' ' +  str(self.times)

    def __cmp__(self, other):
        return cmp(self.times, other.times)

