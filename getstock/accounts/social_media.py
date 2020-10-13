import login
import register
import csv
import friends
data = []
step = 0

with open('accounts.csv') as file:
  csv_reader = csv.reader(file, delimiter = ',')


  for row in csv_reader:
     data.append(row)

A = input('Do you want register the account or log in to the account(r/l): ')
if (A == 'l'):
    login = input('Your login: ')
    password = input('Your password: ')
    if login.main(login, password) == "cannot":
        exit(0)
    want = input('list of all users(1)   list of your friends?(2)   list of requests for adding friends(3)   list of friends of some user(4)   chat with somebody(5)   send a request for friendship(6)  accept or deny a request of some user(7/8): ')
    if (want == '1'):
        for row in data:
            if (row[0] != username):
                print(row[0])
    elif (want == '2'):
        friends.print_friends(username)
    elif (want == '3'):
        friends.print_request_friends(username)
    elif (want == '4'):
        friend = input('Write the username: ')
        #existing of user
        friends.print_friends(friend)
    elif (want == '5'):
        #existing of friend
        friend = input('Write the username: ')
        friends.print_conversation(username, friend)
        if input('Do you want to write something to ' + friend + '(y/n): ') == 'y':
            friends.send_message(username, friend)
    elif (want == '6'):
        #you have already requested him
        #existing of new friend
        friend = input('Write the username: ')
        friends.send_request(username, friend)
    elif (want == '7'):
        #existing of user
        friend = input('Write the username: ')
        friends.accept_request(username, friend)
    else:
        #existing of user
        friend = input('Write the username: ')
        friends.deny_request(username, friend)

else:
    wow = register.main()
    if (wow[2] == 0):
        print('Successful registration!')
        with open('accounts.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            for row in data:
                csv_writer.writerow(row)
            csv_writer.writerow([wow[0], wow[1]])
