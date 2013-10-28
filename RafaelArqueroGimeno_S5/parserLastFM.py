__author__ = "Rafael Arquero Gimeno"

from model import *


def parser(userFile, users, step=5000, endless=True):
    """Parses the file of users
    :param step:
    :param userFile:
    """

    i = 0  # iterations counter

    with open(userFile, 'r') as usersFile:
        for line in usersFile:
            userFirst = line.split("||")
            userSecond = map(lambda x: x.split("&&"), userFirst)
            #I found names like ":wumpscut:" that breaks the old parser
            userDisks = map(lambda x: x.rsplit("::", 1), userSecond[4])

            artists = [Artist(*disk) for disk in userDisks]
            user = User(userSecond[0][0], userSecond[2][0], userSecond[1][0], userSecond[3][0], artists,
                        float(userSecond[5][1][:-1]))

            users.insert(user)
            i += 1

            if i % step == 0:  # we have n-step users
                yield users

    if endless:
        while True:
            yield users