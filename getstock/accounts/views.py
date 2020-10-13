from django.shortcuts import render

# Create your views here.
from .models import *

import login
import register
import csv
import friends
data = []

def login(request, login, password):
    with open('accounts.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)
        if login.main(login, password) == "cannot":
            #ERROR
            exit(0)
        return render(request, '')

def register(request, username, password, repeated_password):
    with open('accounts.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)

        result = register.main(username, password, repeated_password)
        if (result[2] == 0):
            print('Successful registration!')
            with open('accounts.csv', 'w', newline='') as file:
                csv_writer = csv.writer(file, delimiter = ',')
                for row in data:
                    csv_writer.writerow(row)
                csv_writer.writerow([result[0], result[1]])
        return render(request, '')

def do_individual_actions(request, username, type):
    with open('accounts.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        if (type == '1'):
            for row in data:
                if (row[0] != username):
                    print(row[0])
        elif (type == '2'):
            friends.print_friends(username)
        elif (type == '3'):
            friends.print_request_friends(username)
        return render(request, '')

def do_interactive_actions(request, username, friend, type):
        if (type == '4'):
            #existing of user
            friends.print_friends(friend)
        elif (type == '5'):
            #existing of friend
            friends.print_conversation(username, friend)
            friends.send_message(username, friend)
        elif (want == '6'):
            #you have already requested him
            #existing of new friend
            friends.send_request(username, friend)
        elif (want == '7'):
            #existing of user
            friends.accept_request(username, friend)
        else:
            #existing of user
            friends.deny_request(username, friend)

def see_all_users(request, username):
    do_individual_actions(request, username, '1')

def print_all_friends(request, username):
    do_individual_actions(request, username, '2')

def print_requested_friends(request, username):
    do_individual_actions(request, username, '3')

def print_friends_of_some_user(request, username, friend):
    do_interactive_actions(request, username, friend, '4')

def print_conversation_of_users(request, username, friend):
    do_interactive_actions(request, username, friend, '5')

def send_request_to_some_user(request, username, friend):
    do_interactive_actions(request, username, friend, '6')

def accept_request_of_some_user(request, username, friend):
    do_interactive_actions(request, username, friend, '7')

def deny_request_of_some_user(request, username, friend):
    do_interactive_actions(request, username, friend, '8')

def user(request, login):
    context = dict()
    user = Account.objects.get(login = login)
    context['user'] = user
    return render(request, '/Users/dalenamir/Desktop/projects/stocks/stocks/templates/accounts/user.html', context)

def all(request):
    context = dict()
    users = Account.objects.all()
    context['users'] = users
    return render(request, '/Users/dalenamir/Desktop/projects/stocks/stocks/templates/accounts/all_users.html', context)
