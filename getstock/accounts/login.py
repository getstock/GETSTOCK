import csv

def main(login, password):
    data = []
    may = 0
    exist = 0
    with open('accounts.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)
    for logins in data:
        if logins[0] == login:
            exist = 1
            if password == logins[1]:
                may = 1
    if exist == 0:
        print('!!!!FAILURE!!!!')
        print('There is no account with this login')
    elif (may == 0):
        print('!!!!FAILURE!!!!')
        print('Password is incorrect')
    else:
        print('You successfully logged in to your account')
        return "can"
    return "cannot"
if __name__ == '__main__':
    main()
