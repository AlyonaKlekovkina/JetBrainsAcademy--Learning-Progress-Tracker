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


def add_students(students, id_list):
    count = 0
    print("Enter student credentials or 'back' to return:")
    while True:
        result = evaluate_info()
        if result == 'back':
            return "Total", str(count), "students have been added."
        elif result == 'Incorrect credentials.':
            print(result)
        elif result == 'Incorrect first name.' or result == 'Incorrect last name.' or result == 'Incorrect email.':
            print(result)
        else:
            the_id = create_id(result[0])
            if the_id in students:
                print('This email is already taken.')
            else:
                print('The student has been added.')
                count += 1
                students.add(the_id)
                id_list.update({the_id: {'name': result[1], 'last name': result[2], 'email': result[0], 'Python': 0, 'DSA': 0, 'Databases': 0, 'Flask': 0}})


def create_id(email):
    hash_symbol = abs(hash(email)) % 100000
    return hash_symbol


def check_student_id(id_to_find):
    try:
        the_id = int(id_to_find)
        if the_id not in id_list:
            return "Not found"
        else:
            return the_id
    except ValueError:
        return "Not found"


#we need to get the id and 4 digits following the id
def check_input(inp_to_check):
    correct_format = inp_to_check.split()
    try:
        id = correct_format[0]
        python = int(correct_format[1])
        dsa = int(correct_format[2])
        databases = int(correct_format[3])
        flask = int(correct_format[4])
        if len(correct_format) != 5 or python < 0 or dsa < 0 or databases < 0 or flask < 0:
            return "Incorrect points format."
        else:
            return id, python, dsa, databases, flask
    except (ValueError, IndexError):
        return "Incorrect points format."


def add_points(id_list):
    print("Enter an id and points or 'back' to return:")
    while True:
        inp = input()
        inp_eval = check_input(inp)
        if inp == 'back':
            return 'back'
        if inp_eval == 'Incorrect points format.':
            print("Incorrect points format.")
        elif check_student_id(inp_eval[0]) == 'Not found':
            print("No student is found for id={}".format(inp_eval[0]))
        else:
            id = int(inp_eval[0])
            python = int(inp_eval[1])
            dsa = int(inp_eval[2])
            databases = int(inp_eval[3])
            flask = int(inp_eval[4])
            id_list[id]['Python'] += python
            id_list[id]['DSA'] += dsa
            id_list[id]['Databases'] += databases
            id_list[id]['Flask'] += flask
            print("Points updated.")


def return_points(id_list):
    print("Enter an id or 'back' to return:")
    while True:
        input_to_find = input()
        if input_to_find == 'back':
            return 'back'
        elif check_student_id(input_to_find) == 'Not found':
            print("No student is found for id={}".format(input_to_find))
        else:
            p = id_list[int(input_to_find)]['Python']
            ds = id_list[int(input_to_find)]['DSA']
            db = id_list[int(input_to_find)]['Databases']
            fl = id_list[int(input_to_find)]['Flask']
            print("{} points: Python={}; DSA={}; Databases={}; Flask={}".format(input_to_find, p, ds, db, fl))


id_list = {}
students = set()
print("Learning progress tracker")
inp = input()
while True:
    if len(inp.strip()) == 0:
        print('No input.')
        inp = input()
    elif inp == 'add students':
        reply = add_students(students, id_list)
        print(' '.join(reply))
        inp = input()
    elif inp == 'back':
        print("Enter 'exit' to exit the program")
        inp = input()
    elif inp == 'exit':
        print('Bye!')
        break
    elif inp == 'list':
        if len(id_list) == 0:
            print("No students found.")
            inp = input()
        else:
            print('Students:')
            for v in id_list:
                print(v)
            inp = input()
    elif inp == 'add points':
        result = add_points(id_list)
        if result == 'back':
            inp = input()
        else:
            print(result)
    elif inp == "find":
        find_result = return_points(id_list)
        if find_result == 'back':
            inp = input()
        else:
            print(find_result)
    else:
        print("Unknown command!")
        inp = input()
