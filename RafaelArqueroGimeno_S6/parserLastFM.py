from model import *

__author__ = "Rafael Arquero Gimeno"


def parser(filename):
    """Parses the file of users
    :param filename: the file path containing users
    """

    with open(filename, 'r') as usersFile:
        for line in usersFile:
            userFirst = line.split("||")
            userSecond = map(lambda x: x.split("&&"), userFirst)
            #I found names like ":wumpscut:" that breaks the old parser
            userDisks = map(lambda x: x.rsplit("::", 1), userSecond[4])

            artists = [Artist(*disk) for disk in userDisks]
            user = User(userSecond[0][0], userSecond[2][0], userSecond[1][0], userSecond[3][0], artists,
                        float(userSecond[5][1][:-1]))

            yield user
