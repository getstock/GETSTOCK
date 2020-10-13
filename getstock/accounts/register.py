import csv

data = []
t = "!@#$%^&*()_-=+-"

with open('accounts.csv') as file:
  csv_reader = csv.reader(file, delimiter = ',')


  for row in csv_reader:
     data.append(row)


def lower_letter(s):
    have = 0
    for ch in s:
        if ('a' <= ch and ch <= 'z'):
            have += 1
    return have

def upper_letter(s):
    have = 0
    for ch in s:
        if ('A' <= ch and ch <= 'Z'):
            have += 1
    return have

def digits(s):
    have = 0
    for ch in s:
        if ('0' <= ch and ch <= '9'):
            have += 1
    return have

def special_ch(s):
    have = 0
    for ch in s:
        if (ch in t):
            have += 1
    return have


def main(login, password, repeated_password):
    error = error2 = 0
    #login = input("Your login: ")
    exist = 0
    for logins in data:
        if (logins[0] == login):
            exist = 1
    bad = 0
    if (exist):
        print('!!!!FAILURE!!!!')
        print('This login is already registered')
        bad = 1
    #login:
    #length from 5 to 20
    #minimum 1 letter and 1 digit
    #password
    #length from 8 to 20
    #minimum 1 letter and 1 digit
    U = upper_letter(login)
    L = lower_letter(login)
    D = digits(login)
    S = special_ch(login)
    o = 0
    if L + U + D + S < len(login):
        o = 1
    if o != 0 or D == 0 or L + U == 0 or len(login) < 5 or len(login) > 20:
        error2 = 1
    if (error2 == 1 and bad == 0):
        print("!!!!FAILURE!!!!")
        bad = 1
    if (len(login) < 5 or len(login) > 20):
        if len(login) < 5:
            print("Login's length is less than 5")
        else:
            print("Login's length is more than 20")
    if (o != 0):
        print("Login has other languages or symbols instead of english or special symbols")
    if (D == 0):
        print("Login has not any digit")
    L = lower_letter(password)
    U = upper_letter(password)
    D = digits(password)
    S = special_ch(password)
    o = 1
    if L + U + D + S < len(password):
        o = 1
    error = 0
    if (L + U == 0 or D == 0 or o == 1 or len(password) < 8 or len(password) > 20):
        error = 1
    if (error and bad == 0):
        print("!!!!FAILURE!!!!")
    if (L + U == 0):
        print("Password has not any letter")
    if (D == 0):
        print("Password has not any digit")
    if o != 0:
        print("Password has other languages or symbols instead of english or special symbols")
    if (len(password) < 8 or len(password) > 20):
        if (len(password) < 8):
            print("Password's length is less than 8")
        else:
            print("Password's length is more than 20")
    if (password != repeated_password):
        if (bad == 0):
            print('!!!!FAILURE!!!!')
            bad = 1
        print("Passwords are not same")
        return [login, password, 1]
    return [login, password, bad]

if __name__ == '__main__':
    main()
