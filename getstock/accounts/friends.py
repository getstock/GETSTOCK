import csv

data = []
data2 = []
data1 = []
#accept, deny, write_to_somebody, print_friends, print_request_friends, print_conversation
#login = "", password = "", list_of_friends = [ [friend_login, [conversation]] ], list_of_requests = [login]
#[login, password] -> data
#[name1, name2, friend or requeste(1/0)] -> data1
#[conversation] -> data2

with open('conversation.csv') as file:
    csv_reader2 = csv.reader(file, delimiter = ',')
    for row in csv_reader2:
            data2.append(row)
    with open('friend.csv') as file:
        csv_reader1 = csv.reader(file, delimiter = ',')
        for row in csv_reader1:
                data1.append(row)
        with open('accounts.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                    data.append(row)
            def print_friends(username):
                ok = 0
                for row in data:
                    if row[0] == username:
                        ok = 1
                if ok == 0:
                    print('!!!!FAILURE!!!!')
                    print('This login does not exist')
                    return
                for row in data1:
                    if row[2] == '1':
                        if (row[0] == username):
                            print(row[1])
                        elif (row[1] == username):
                            print(row[0])
            def print_request_friends(username):
                ok = 0
                for row in data:
                    if row[0] == username:
                        ok = 1
                if ok == 0:
                    print('!!!!FAILURE!!!!')
                    print('This login does not exist')
                    return
                for row in data1:
                    if row[2] == '0':
                        if (row[1] == username):
                            print(row[0])

            def print_conversation(username, friend):
                if (username == friend):
                    print("It's your account")
                    return
                was = 0
                was1 = 0
                for row in data:
                    if row[0] == username:
                        was = 1
                    if row[0] == friend:
                        was1 = 1
                if was == 0:
                    print('!!!!FAILURE!!!!')
                    print('This login does not exist')
                    return
                if was1 == 0:
                    print('!!!!FAILURE!!!!')
                    print('This friend does not exist')
                    return
                ok = 0
                for row in data1:
                    if row[0] == username and row[1] == friend and row[2] == '1':
                        ok = 1
                    if row[1] == username and row[0] == friend and row[2] == '1':
                        ok = 1
                if ok == 0:
                    print("You are not friends")
                    return
                for i in range(len(data1)):
                    yes = 0
                    if data1[i][0] == username and data1[i][1] == friend and data1[i][2] == '1':
                        yes = 1
                    if data1[i][0] == friend and data1[i][1] == username and data1[i][2] == '1':
                        yes = 1
                    if (yes == 1):
                        print(*data2[i], sep = '\n')
                        break

            def send_message(username, friend):
                if (username == friend):
                    print("It's your account")
                    return
                was = 0
                was1 = 0
                for row in data:
                    if row[0] == username:
                        was = 1
                    if row[0] == friend:
                        was1 = 1
                if was == 0:
                    print('!!!!FAILURE!!!!')
                    print('This login does not exist')
                    return
                if was1 == 0:
                    print('!!!!FAILURE!!!!')
                    print('This friend does not exist')
                    return
                ok = 0
                for row in data1:
                    if row[0] == username and row[1] == friend and row[2] == '1':
                        ok = 1
                    if row[1] == username and row[0] == friend and row[2] == '1':
                        ok = 1
                if ok == 0:
                    print("You are not friends")
                    return
                text = input('Type text: ')
                with open('conversation.csv', 'w', newline='') as file:
                    csv_writer = csv.writer(file, delimiter = ',')
                    for i in range(len(data1)):
                        if data1[i][0] == username and data1[i][1] == friend and data1[i][2] == '1':
                            yes = 1
                        if data1[i][0] == friend and data1[i][1] == username and data1[i][2] == '1':
                            yes = 1
                        if (yes == 1):
                            data2[i].append(username + ': ' + text)
                        csv_writer.writerow(data2[i])



            def send_request(username, friend):
                if (username == friend):
                    print("It's your account")
                    return
                #existing username and friends(done)
                #not friends(done)
                #before no requests between them(done)
                was = 0
                was1 = 0
                for row in data:
                    if row[0] == username:
                        was = 1
                    if row[0] == friend:
                        was1 = 1
                if was == 0:
                    print('!!!!FAILURE!!!!')
                    print('This login does not exist')
                    return
                if was1 == 0:
                    print('!!!!FAILURE!!!!')
                    print('This friend does not exist')
                    return
                ok = 0
                ok2 = 0
                for row in data1:
                    if row[0] == username and row[1] == friend and row[2] == '1':
                        ok = 1
                    if row[1] == username and row[0] == friend and row[2] == '1':
                        ok = 1
                    if row[0] == username and row[1] == friend and row[2] == '0':
                        ok2 = 1
                    if row[0] == friend and row[1] == username and row[2] == '0':
                        ok2 = 1
                if ok == 1:
                    print("You are friends")
                    return
                if ok2 == 1:
                    print("One of you already has sent the request")
                    return

                with open('conversation.csv', 'w', newline='') as file:
                    csv_writer2 = csv.writer(file, delimiter = ',')
                    with open('friend.csv', 'w', newline='') as file:
                        csv_writer1 = csv.writer(file, delimiter = ',')
                        data1.append([username, friend, 0])
                        data2.append([])
                        for i in range(len(data1)):
                            csv_writer2.writerow(data2[i])
                            csv_writer1.writerow(data1[i])

            def accept_request(username, friend):
                if (username == friend):
                    print("It's your account")
                    return
                #existing username and friends(done)
                #not friends(done)
                #before no requests between them(done)
                was = 0
                was1 = 0
                for row in data:
                    if row[0] == username:
                        was = 1
                    if row[0] == friend:
                        was1 = 1
                if was == 0:
                    print('!!!!FAILURE!!!!')
                    print('This login does not exist')
                    return
                if was1 == 0:
                    print('!!!!FAILURE!!!!')
                    print('This friend does not exist')
                    return
                ok = 0
                ok2 = 0
                for row in data1:
                    if row[0] == username and row[1] == friend and row[2] == '1':
                        ok = 1
                    if row[1] == username and row[0] == friend and row[2] == '1':
                        ok = 1
                    if row[0] == friend and row[1] == username and row[2] == '0':
                        ok2 = 1
                if ok == 1:
                    print("You are friends")
                    return
                if ok2 == 0:
                    print("You don't have this request")
                    return

                with open('friend.csv', 'w', newline='') as file:
                    csv_writer1 = csv.writer(file, delimiter = ',')
                    for row in data1:
                        if row[0] == friend and row[1] == username and row[2] == '0':
                            row[2] = 1
                        csv_writer1.writerow(row)

            def deny_request(username, friend):
                if (username == friend):
                    print("It's your account")
                    return
                #existing username and friends(done)
                #not friends(done)
                #before no requests between them(done)
                was = 0
                was1 = 0
                for row in data:
                    if row[0] == username:
                        was = 1
                    if row[0] == friend:
                        was1 = 1
                if was == 0:
                    print('!!!!FAILURE!!!!')
                    print('This login does not exist')
                    return
                if was1 == 0:
                    print('!!!!FAILURE!!!!')
                    print('This friend does not exist')
                    return
                ok = 0
                ok2 = 0
                for row in data1:
                    if row[0] == username and row[1] == friend and row[2] == '1':
                        ok = 1
                    if row[1] == username and row[0] == friend and row[2] == '1':
                        ok = 1
                    if row[0] == friend and row[1] == username and row[2] == '0':
                        ok2 = 1
                if ok == 1:
                    print("You are friends")
                    return
                if ok2 == 0:
                    print("You don't have this request")
                    return
                with open('conversation.csv', 'w', newline='') as file:
                    csv_writer2 = csv.writer(file, delimiter = ',')
                    with open('friend.csv', 'w', newline='') as file:
                        csv_writer1 = csv.writer(file, delimiter = ',')
                        for i in range(len(data1)):
                            if data1[i][0] == friend and data1[i][1] == username and data1[i][2] == '0':
                                continue
                            csv_writer1.writerow(data1[i])
                            csv_writer2.writerow(data2[i])
