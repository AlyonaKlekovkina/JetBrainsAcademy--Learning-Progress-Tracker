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


def add_points(id_list, points_list):
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
            if python != 0:
                points_list["Python"] += 1
            id_list[id]['DSA'] += dsa
            if dsa != 0:
                points_list["DSA"] += 1
            id_list[id]['Databases'] += databases
            if databases != 0:
                points_list["Databases"] += 1
            id_list[id]['Flask'] += flask
            if flask != 0:
                points_list["Flask"] += 1
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


def return_statistics(id_list, points_list):
    try:
        points_dict = {'Python': 0, 'DSA': 0, 'Databases': 0, 'Flask': 0}
        enrolled_students = {'Python': 0, 'DSA': 0, 'Databases': 0, 'Flask': 0}
        average_list = {'Python': 0, 'DSA': 0, 'Databases': 0, 'Flask': 0}
        for v in id_list:
            points_dict['Python'] += id_list[v]['Python']
            if id_list[v]['Python'] != 0:
                enrolled_students['Python'] += 1
            points_dict['DSA'] += id_list[v]['DSA']
            if id_list[v]['DSA'] != 0:
                enrolled_students['DSA'] += 1
            points_dict['Databases'] += id_list[v]['Databases']
            if id_list[v]['Databases'] != 0:
                enrolled_students['Databases'] += 1
            points_dict['Flask'] += id_list[v]['Flask']
            if id_list[v]['Flask'] != 0:
                enrolled_students['Flask'] += 1

        average_list['Python'] = points_dict['Python'] / enrolled_students['Python']
        average_list['DSA'] = points_dict['DSA'] / enrolled_students['DSA']
        average_list['Databases'] = points_dict['Databases'] / enrolled_students['Databases']
        average_list['Flask'] = points_dict['Flask'] / enrolled_students['Flask']

        highest_activity = sorted(points_list.items(), key=lambda x:x[1], reverse=True)
        most_popular = sorted(enrolled_students.items(), key=lambda x:x[1], reverse=True)
        average_sorted = sorted(average_list.items(), key=lambda x:x[1], reverse=True)
        return highest_activity, most_popular, average_sorted
    except ZeroDivisionError:
        return None


def calculate_result(sorted_list):
    most_popular = sorted_list[0][0]
    least_popular = sorted_list[3][0]
    for i in range(3):
        if sorted_list[i][1] == sorted_list[i+1][1]:
            most_popular += ', ' + sorted_list[i+1][0]
    if least_popular in most_popular:
        least_popular = 'n/a'
    return most_popular, least_popular


def calculate_percentage():
    courses = ['python', 'dsa', 'flask', 'databases']
    while True:
        inp = input()
        if inp == 'back':
            return 'back'
        elif inp.casefold() not in courses:
            print('Unknown course.')
        else:
            check_in_dict = ''
            total = 0
            if inp == 'python' or inp == "Python":
                check_in_dict = 'Python'
                total = 600
            elif inp == 'dsa'.casefold() or inp == "DSA":
                check_in_dict = 'DSA'
                total = 400
            elif inp == 'databases'or inp == 'Databases':
                check_in_dict = 'Databases'
                total = 480
            elif inp == 'flask' or inp == 'Flask':
                check_in_dict = 'Flask'
                total = 550
            print(check_in_dict)
            print("id   points completed")
            points_dict = {}
            for v in id_list:
                points = id_list[v][check_in_dict]
                points_dict.update({v: points})

            points_dict_sorted = sorted(points_dict.items(), key=lambda x:x[1], reverse=True)
            for value in points_dict_sorted:
                id = value[0]
                point = int(value[1])
                percent = format((point / total) * 100, ".1f")
                if point != 0:
                    print('{} {}        {}%'.format(id, point, percent))


def statistics_print_statement(id_list):
    print("Type the name of a course to see details or 'back' to quit:")
    if len(id_list) == 0:
        most_popular = 'n/a'
        least_popular = 'n/a'
        highest_activity = 'n/a'
        lowest_activity = 'n/a'
        easiest_course = 'n/a'
        hardest_course = 'n/a'
    else:
        sorted_list = return_statistics(id_list, points_list)
        activity = calculate_result(sorted_list[0])
        popularity = calculate_result(sorted_list[1])
        hardness = calculate_result(sorted_list[2])
        most_popular = popularity[0]
        least_popular = popularity[1]
        highest_activity = activity[0]
        lowest_activity = activity[1]
        easiest_course = hardness[0]
        hardest_course = hardness[1]
    print("Most popular:", most_popular)
    print("Least popular:", least_popular)
    print("Highest activity:", highest_activity)
    print("Lowest activity:", lowest_activity)
    print("Easiest course:", easiest_course)
    print("Hardest course:", hardest_course)


points_list = {"Python": 0, "DSA": 0, "Databases": 0, "Flask": 0}
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
        result = add_points(id_list, points_list)
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
    elif inp == "statistics":
        statistics_print_statement(id_list)
        if calculate_percentage() == 'back':
            inp = input()
        else:
            calculate_percentage()
    else:
        print("Unknown command!")
        inp = input()
