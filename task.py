import string


def evaluate_info():
    info = input().split(' ')
    email = info[-1]
    name = info[0]
    list_last_name = info[1:-1]
    last_name = ' '.join([str(elem) for elem in list_last_name])
    if len(info) < 3 and info[0] != 'back':
        return 'Incorrect credentials.'
    elif info[0] == 'back':
        return 'back'
    elif check_name(name) == 'Incorrect':
        return 'Incorrect first name.'
    if check_name(last_name) == 'Incorrect':
        return 'Incorrect last name.'
    elif check_email(email) == 'Incorrect email.':
        return 'Incorrect email.'
    else:
        return email, name, last_name


def check_email(email):
    ats = email.count('@')
    mail = email.split('@')
    name_part = mail[0]
    address_part = mail[-1]
    address = address_part.split('.')
    if ats > 1:
        return 'Incorrect email.'
    elif '@' not in email or '.' not in address_part:
        return 'Incorrect email.'
    elif len(name_part) <= 0 or len(address[0]) <= 0 or len(address[1]) <= 0:
        return 'Incorrect email.'
    else:
        return email


def check_name(name):
    symbols = ["-", "'", ' ']
    lc_letters = string.ascii_lowercase
    up_letters = string.ascii_uppercase
    last_symbol = len(name) - 1
    for i in range(len(name)):
        if i == 0 and name[i] == "-" or name[0] == "'":
            return 'Incorrect'
        elif i == last_symbol and name[last_symbol] == "-" or name[last_symbol] == "'":
            return 'Incorrect'
        elif len(name) <= 1:
            return 'Incorrect'
        elif "-'" in name or "'-" in name or "--" in name or "''" in name:
            return 'Incorrect'
        elif name[i] in symbols or name[i] in lc_letters or name[i] in up_letters:
            continue
        else:
            return 'Incorrect'
    return name


def add_students():
    count = 0
    print("Enter student credentials or 'back' to return:")
    while True:
        result = evaluate_info()
        if result == 'back':
            if count == 1:
                return "Total", str(count), "student has been added."
            else:
                return "Total", str(count), "students have been added."
        elif result == 'Incorrect credentials.':
            print(result)
        elif result == 'Incorrect first name.' or result == 'Incorrect last name.' or result == 'Incorrect email.':
            print(result)
        else:
            print('The student has been added.')
            count += 1


print("Learning progress tracker")
inp = input()
while True:
    if len(inp.strip()) == 0:
        print('No input.')
        inp = input()
    elif inp == 'add students':
        reply = add_students()
        print(' '.join(reply))
        inp = input()
    elif inp == 'back':
        print("Enter 'exit' to exit the program")
        inp = input()
    elif inp == 'exit':
        print('Bye!')
        break
    else:
        print("Unknown command!")
        inp = input()
