from model import *

def parser(user_file, Type):
	"Parses the file of users"

	count = 0
	users = Type()
	with open(user_file, 'r') as usersFile:
		for line in usersFile:
			disks_played = []
			user_first = line.split("||")
			user_second = map(lambda x: x.split("&&"), user_first)
			#I found names like ":wumpscut:" that breaks the old parser
			user_disks = map(lambda x: x.rsplit("::", 1), user_second[4])			

                        artists         = [Artist(*disk) for disk in user_disks]
			user            = User(user_second[0][0], user_second[2][0], user_second[1][0], user_second[3][0], artists)

			users.enqueue(user)
			count += 1

                        #we have 1000k users
			if(count % 1000 == 0):
                                yield users
                                users = Type()#reset users

