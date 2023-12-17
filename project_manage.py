from datetime import date
import database
import random

my_database = database.DB()

persons_key = ["ID", "fist", "last", "type"]
logins_key = ["ID", "username", "password", "role"]
project_key = ["ProjectID", "Title", "Lead", "Member1",
               "Member2", "Advisor", "Status"]
advisor_pending_request_key = ["ProjectID", "to_be_advisor",
                               "Response", "Response_date"]
member_pending_request_key = ["ProjectID", "to_be_member",
                              "Response", "Response_date"]
project_data_key = ["ProjectID", "Title", "Proposal", "Report", "Status"]
proposal_data_key = ["ProjectID", "eva_1", "review_1", "eva_2",
                     "review_2", "eva_3", "review_3", "result",
                     "proposal", "faculty_1", "faculty_2", "faculty_3"]
status_list = ["has not submitted a project proposal",
               "has submitted a project proposal (waiting for evaluation)",
               "a project proposal evaluation; disapproved",
               "a project proposal evaluation; approved "
               "(waiting for a project report)",
               "has submitted a finale project report "
               "(waiting for advisor approval)",
               "a finale project report approval; disapproved",
               "a finale project report approval; approved"]


def initializing():
    persons_csv = database.csv_path("persons")
    login_csv = database.csv_path("login")
    project_csv = database.csv_path("project")
    advisor_pending_request_csv = database.csv_path("advisor_pending_request")
    member_pending_request_csv = database.csv_path("member_pending_request")
    project_data_csv = database.csv_path("project_data")
    proposal_data_csv = database.csv_path("proposal_data")

    persons = database.Table("persons", persons_csv)
    logins = database.Table("login", login_csv)
    project = database.Table("project", project_csv)
    advisor_pending_request = database.Table("advisor_pending_request",
                                             advisor_pending_request_csv)
    member_pending_request = database.Table("member_pending_request",
                                            member_pending_request_csv)
    project_data = database.Table("project_data", project_data_csv)
    proposal_data = database.Table("proposal_data", proposal_data_csv)

    my_database.insert(persons)
    my_database.insert(logins)
    my_database.insert(project)
    my_database.insert(advisor_pending_request)
    my_database.insert(member_pending_request)
    my_database.insert(project_data)
    my_database.insert(proposal_data)


def login():
    logins = my_database.search("login")
    while True:
        name = str(input("Enter the username: "))
        if name in logins.aggregate(lambda x: x, "username"):
            break
        print("Please input a valid username.")
    while True:
        password = str(input("Enter the password: "))
        result = logins.filter(
            lambda x:
            (x["username"] == name) and
            (x["password"] == password))
        if result.table:
            break
        print("Wrong password. Please try again.")
    user = [result.table[0]["ID"], result.table[0]["role"]]
    return user


def exit():
    database.update_csv(my_database.search("persons"), persons_key)
    database.update_csv(my_database.search("login"), logins_key)
    database.update_csv(my_database.search("project"), project_key)
    database.update_csv(my_database.search("advisor_pending_request"),
                        advisor_pending_request_key)
    database.update_csv(my_database.search("member_pending_request"),
                        member_pending_request_key)
    database.update_csv(my_database.search("project_data"), project_data_key)
    database.update_csv(my_database.search("proposal_data"), proposal_data_key)


def all_name(role_value):
    user = logins.filter(
        lambda x:
        x["role"] == role_value)
    name_id_list = [f"{'ID':^20}{'Username':^20}", "\n"]
    for i in user.table:
        name = f"{i['ID']:^20}{i['username']:^20}"
        name_id_list.append(name)
    return name_id_list


def input_number(number):
    while True:
        num = str(input("Input number: "))
        if num in [str(i) for i in range(1, number + 1)]:
            break
        print("Please input a valid number.")
    return int(num)


def check_id(table, ID):
    while True:
        the_id = str(input(f"Input {ID}: "))
        result = table.filter(lambda x: x[ID] == the_id)
        if result.table:
            break
        print("Please input valid ID.")
    return result.table[0], the_id


def title(ID):
    the_project = project.filter(
        lambda x:
        x["ProjectID"] == ID)
    return the_project.table[0]["Title"]


def display(table_key, dict_user):
    the_list = []
    num = 0
    for k, j in dict_user.items():
        the_list.append(f"{table_key[num]}: {j}")
        num += 1
    display_list(the_list)


def display_list(the_list):
    print(("_" * 100) + "\n")
    for i in the_list:
        print(f"{str(i):^100}")
    print("\n" + ("_" * 100) + "\n")


def format_table(dict_key, table):
    head_format = ""
    for i in dict_key:
        head_format += f"{i:^25}"
    print("\n" + ("_" * 100) + "\n")
    print(f"{head_format:^100}", "\n")
    for i in table:
        info_format = ""
        for k, j in i.items():
            info_format += f"{j:^25}"
        print(f"{info_format:^100}")
    print(("_" * 100) + "\n")


def format_solo(dict_key, table):
    print("\n" + ("_" * 100) + "\n")
    for i in table:
        info_format = ""
        num = 0
        for k, j in i.items():
            info_format += (" " * 5) + f"{dict_key[num]}: {j}" + "\n"
            num += 1
        print(f"{info_format:^100}")
    print(("_" * 100) + "\n")


def accept_or_deny():
    while True:
        answer = str(input("Do you wish to accept or deny?(accept/deny): "))
        if (answer == "accept") or (answer == "deny"):
            break
        print("Please input a valid answer.")
    return answer


def continue_or_not(ID):
    while True:
        answer = str(input("Do you wish to continue?(yes/no): "))
        if (answer == "yes") or (answer == "no"):
            break
        print("Please input a valid answer.")
    if answer == "yes":
        role = logins.filter(
            lambda x:
            x["ID"] == ID)
        check_role(role.table[0]["role"], ID)
    elif answer == "no":
        print("Exit the program.")


def print_dict(the_dict):
    for i, k in the_dict.items():
        print(f"{i}: {k}")


def new_data(table_key):
    new_list = []
    for i in table_key:
        new_value = str(input(f"Input new {i}: "))
        new_list.append(new_value)
    return new_list


def new_dictionary(table_key, new_list):
    new_dict = {}
    num = 0
    for i in table_key:
        new_dict[i] = new_list[num]
        num += 1
    return new_dict


def date_today():
    return str(date.today())


def check_role(role, ID):
    print()
    if role == "admin":
        admin_login(ID)
    elif role == "student":
        student_login(ID)
    elif role == "member":
        member_login(ID)
    elif role == "lead":
        lead_login(ID)
    elif role == "faculty":
        faculty_login(ID)
    elif role == "advisor":
        advisor_login(ID)


class User:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    def name(self):
        user = logins.filter(lambda x: x["ID"] == self.id)
        return user.table[0]["username"]


def admin_login(ID):
    admin = User(ID)
    print("(1) See information")
    print("(2) Update information")
    print("(3) Exit")
    number = input_number(3)
    print()

    if number == 1:
        print("(1) Persons Table")
        print("(2) Login Table")
        print("(3) Project Table")
        print("(4) Project_data Table")
        print("(5) Member_pending_request Table")
        print("(6) Advisor_pending_request Table")
        print("(7) Proposal_data Table")
        number = input_number(7)

        if number == 1:
            format_table(persons_key, persons.table)

        elif number == 2:
            format_table(logins_key, logins.table)

        elif number == 3:
            format_solo(project_key, project.table)

        elif number == 4:
            format_solo(project_data_key, project_data.table)

        elif number == 5:
            format_table(member_pending_request_key,
                         member_pending_request.table)

        elif number == 6:
            format_table(advisor_pending_request_key,
                         advisor_pending_request.table)

        elif number == 7:
            format_solo(proposal_data_key, proposal_data.table)
        continue_or_not(admin.id)

    elif number == 2:
        print("(1) Persons Table")
        print("(2) Login Table")
        print("(3) Project Table")
        print("(4) Project_data Table")
        print("(5) Member_pending_request Table")
        print("(6) Advisor_pending_request Table")
        print("(7) Proposal_data Table")
        number = input_number(7)
        print()

        if number == 1:
            print("(1) Update existing data")
            print("(2) Update new data")
            number = input_number(2)

            if number == 1:
                old_dict, old_id = check_id(persons, "ID")
                print(f"The data now is")
                print_dict(old_dict)
                while True:
                    new_list = new_data(persons_key)
                    if new_list[3] in ["admin", "student", "faculty"]:
                        if (new_list[0] not in persons.aggregate(
                                lambda x: x, "ID") or
                                new_list[0] == old_id):
                            break
                        print("The ID already exists for other user.")
                    print("Please input valid data.")
                for i in persons.table:
                    if i["ID"] == old_id:
                        persons.table.remove(i)
                new_dict = new_dictionary(persons_key, new_list)
                persons.table.append(new_dict)

            elif number == 2:
                while True:
                    new_list = new_data(persons_key)
                    if new_list[3] in ["admin", "student", "faculty"]:
                        if new_list[0] not in persons.aggregate(lambda x:
                                                                x, "ID"):
                            break
                        print("The ID already exists for other user.")
                    print("Please input valid data.")
                new_dict = new_dictionary(persons_key, new_list)
                persons.table.append(new_dict)

        elif number == 2:
            print("(1) Update existing data")
            print("(2) Update new data")
            number = input_number(2)

            if number == 1:
                old_dict, old_id = check_id(logins, "ID")
                print(f"The data now is")
                print_dict(old_dict)
                while True:
                    new_list = new_data(logins_key)
                    if new_list[3] in ["admin", "student", "lead", "member",
                                       "faculty", "advisor"]:
                        if (new_list[0] not in logins.aggregate(
                                lambda x: x, "ID") or
                                new_list[0] == old_id):
                            break
                        print("The ID already exists for other user.")
                    print("Please input valid data.")
                for i in logins.table:
                    if i["ID"] == old_id:
                        logins.table.remove(i)
                new_dict = new_dictionary(logins_key, new_list)
                logins.table.append(new_dict)

            elif number == 2:
                while True:
                    new_list = new_data(logins_key)
                    if new_list[3] in ["admin", "student", "lead", "member",
                                       "faculty", "advisor"]:
                        if new_list[0] not in logins.aggregate(lambda x:
                                                               x, "ID"):
                            break
                        print("The ID already exists for other user.")
                    print("Please input valid data.")
                new_dict = new_dictionary(logins_key, new_list)
                logins.table.append(new_dict)

        elif number == 3:
            print("(1) Update existing data")
            print("(2) Update new data")
            number = input_number(2)

            if number == 1:
                old_dict, old_id = check_id(project, "ProjectID")
                print(f"The data now is")
                print_dict(old_dict)
                while True:
                    new_list = new_data(project_key)
                    if new_list[-1] in status_list:
                        if (new_list[0] not in project.aggregate(
                                lambda x: x, "ProjectID") or
                                new_list[0] == old_id):
                            break
                        print("The ProjectID already exists for other user.")
                    print("Please input valid data.")
                for i in project.table:
                    if i["ProjectID"] == old_id:
                        project.table.remove(i)
                new_dict = new_dictionary(project_key, new_list)
                project.table.append(new_dict)

            elif number == 2:
                while True:
                    new_list = new_data(project_key)
                    if new_list[-1] in status_list:
                        if new_list[0] not in project.aggregate(lambda x: x,
                                                                "ProjectID"):
                            break
                        print("The ProjectID already exists for other user.")
                    print("Please input valid data.")
                new_dict = new_dictionary(project_key, new_list)
                project.table.append(new_dict)

        elif number == 4:
            print("(1) Update existing data")
            print("(2) Update new data")
            number = input_number(2)

            if number == 1:
                old_dict, old_id = check_id(project_data, "ProjectID")
                print(f"The data now is")
                print_dict(old_dict)
                while True:
                    new_list = new_data(project_data_key)
                    if new_list[-1] in status_list:
                        if (new_list[0] not in project_data.aggregate(
                                lambda x: x, "ProjectID") or
                                new_list[0] == old_id):
                            break
                        print("The ProjectID already exists for other user.")
                    print("Please input valid data.")
                for i in project_data.table:
                    if i["ProjectID"] == old_id:
                        project_data.table.remove(i)
                new_dict = new_dictionary(project_data_key, new_list)
                project_data.table.append(new_dict)

            elif number == 2:
                while True:
                    new_list = new_data(project_data_key)
                    if new_list[-1] in status_list:
                        if new_list[0] not in project_data.aggregate(
                                lambda x: x, "ProjectID"):
                            break
                        print("The ProjectID already exists for other user.")
                    print("Please input valid data.")
                new_dict = new_dictionary(project_data_key, new_list)
                project_data.table.append(new_dict)

        elif number == 5:
            print("(1) Update existing data")
            print("(2) Update new data")
            number = input_number(2)

            if number == 1:
                while True:
                    old_id = str(input(f"Input ProjectID: "))
                    to_be_member = str(input(f"Input to_be_member: "))
                    Response = str(input(f"Input Response: "))
                    result = member_pending_request.filter(
                        lambda x: (x["ProjectID"] == old_id) and
                                  (x["to_be_member"] == to_be_member) and
                                  (x["Response"] == Response))
                    if result.table:
                        break
                    print("Please input valid data.")
                old_dict = result.table[0]
                print(f"The data now is")
                print_dict(old_dict)
                while True:
                    new_list = new_data(member_pending_request_key)
                    if new_list[2] in ["accepted", "denied",
                                       "waiting for a response"]:
                        break
                    print("Please input valid data.")
                for i in member_pending_request.table:
                    if (i["ProjectID"] == old_id and
                            i["to_be_member"] == to_be_member and
                            i["Response"] == Response):
                        member_pending_request.table.remove(i)
                new_dict = new_dictionary(member_pending_request_key, new_list)
                member_pending_request.table.append(new_dict)

            elif number == 2:
                while True:
                    new_list = new_data(member_pending_request_key)
                    if new_list[2] in ["accepted", "denied",
                                       "waiting for a response"]:
                        break
                    print("Please input valid data.")
                new_dict = new_dictionary(member_pending_request_key, new_list)
                member_pending_request.table.append(new_dict)

        elif number == 6:
            print("(1) Update existing data")
            print("(2) Update new data")
            number = input_number(2)

            if number == 1:
                while True:
                    old_id = str(input(f"Input ProjectID: "))
                    to_be_advisor = str(input(f"Input to_be_advisor: "))
                    Response = str(input(f"Input Response: "))
                    result = advisor_pending_request.filter(
                        lambda x: (x["ProjectID"] == old_id) and
                                  (x["to_be_advisor"] == to_be_advisor) and
                                  (x["Response"] == Response))
                    if result.table:
                        break
                    print("Please input valid data.")
                old_dict = result.table[0]
                print(f"The data now is")
                print_dict(old_dict)
                while True:
                    new_list = new_data(advisor_pending_request_key)
                    if new_list[2] in ["accepted", "denied",
                                       "waiting for a response"]:
                        break
                    print("Please input valid data.")
                for i in advisor_pending_request.table:
                    if (i["ProjectID"] == old_id and
                            i["to_be_advisor"] == to_be_advisor and
                            i["Response"] == Response):
                        advisor_pending_request.table.remove(i)
                new_dict = new_dictionary(advisor_pending_request_key,
                                          new_list)
                advisor_pending_request.table.append(new_dict)

            elif number == 2:
                while True:
                    new_list = new_data(advisor_pending_request_key)
                    if new_list[2] in ["accepted", "denied",
                                       "waiting for a response"]:
                        break
                    print("Please input valid data.")
                new_dict = new_dictionary(advisor_pending_request_key,
                                          new_list)
                advisor_pending_request.table.append(new_dict)

        elif number == 7:
            print("(1) Update existing data")
            print("(2) Update new data")
            number = input_number(2)

            if number == 1:
                while True:
                    old_id = str(input(f"Input ProjectID: "))
                    proposal = str(input(f"Input a proposal PDF link: "))
                    result = proposal_data.filter(
                        lambda x: (x["ProjectID"] == old_id) and
                                  (x["proposal"] == proposal))
                    if result.table:
                        break
                    print("Please input valid data.")
                old_dict = result.table[0]
                print(f"The data now is")
                print_dict(old_dict)
                while True:
                    new_list = new_data(proposal_data_key)
                    if (new_list[1] and new_list[3] and
                            new_list[5] and new_list[7] in
                            ["waiting for evaluation", "disapproved",
                             "approved"]):
                        break
                    print("Please input valid data.")
                for i in proposal_data.table:
                    if (i["ProjectID"] == old_id and
                            i["proposal"] == proposal):
                        proposal_data.table.remove(i)
                new_dict = new_dictionary(proposal_data_key,
                                          new_list)
                proposal_data.table.append(new_dict)

            elif number == 2:
                while True:
                    new_list = new_data(proposal_data_key)
                    if (new_list[1] and new_list[3] and
                            new_list[5] and new_list[7] in
                            ["waiting for evaluation", "disapproved",
                             "approved"]):
                        break
                    print("Please input valid data.")
                new_dict = new_dictionary(proposal_data_key,
                                          new_list)
                proposal_data.table.append(new_dict)

        print("You have updated data.")
        continue_or_not(admin.id)

    elif number == 3:
        print("Exit the program.")


def student_login(ID):
    student = User(ID)
    print("(1) See invitations")
    print("(2) Accept or deny invitations")
    print("(3) Create a project")
    print("(4) Exit")
    number = input_number(4)

    if number == 1:
        list_response = (member_pending_request.filter(
            lambda x:
            (x["to_be_member"] == student.name()) and
            (x["Response"] == "waiting for a response")))
        list_response = list_response.select("ProjectID")
        list_id_title = ["ProjectID, Title", ""]
        for i in list_response:
            for j, k in i.items():
                list_id_title.append(f"{k}, {title(k)}")
        display_list(list_id_title)
        continue_or_not(student.id)

    if number == 2:
        answer = "none"
        while True:
            ProjectID = str(input("Input ProjectID: "))
            if ((member_pending_request.filter(
                    lambda x:
                    (x["to_be_member"] == student.name()) and
                    (x["Response"] == "waiting for a response") and
                    (x["ProjectID"] == ProjectID))).table):
                break
            print("Please input a valid ProjectID.")
        for i in project.table:
            if i["ProjectID"] == ProjectID:
                if (i["Member1"] != "none") and (i["Member2"] != "none"):
                    print("The members are already full. "
                          "Denying the invitation.")
                    answer = "deny"
        if answer != "deny":
            while True:
                answer = str(input("Do you wish to accept or deny?"
                                   "(accept/deny): "))
                if (answer == "accept") or (answer == "deny"):
                    break
                print("Please input a valid answer.")
        if answer == "accept":
            member_pending_request.update_three("ProjectID", ProjectID,
                                                "to_be_member", student.name(),
                                                "Response", "waiting for "
                                                            "a response",
                                                "Response", "accepted",
                                                "Response_date", date_today())
            logins.update("ID", student.id, "role", "member")
            for i in project.table:
                if i["ProjectID"] == ProjectID:
                    if i["Member1"] == "none":
                        i["Member1"] = student.name()
                    else:
                        i["Member2"] = student.name()
            print("You have become a member student of the project.")
        elif answer == "deny":
            member_pending_request.update_three("ProjectID", ProjectID,
                                                "to_be_member", student.name(),
                                                "Response", "waiting for "
                                                            "a response",
                                                "Response", "denied",
                                                "Response_date", date_today())
            print("You have denied the invitation.")
        continue_or_not(student.id)

    if number == 3:
        waiting = member_pending_request.filter(
            lambda x:
            (x["to_be_member"] == student.name()) and
            (x["Response"] == "waiting for a response"))
        if not waiting.table:
            while True:
                ProjectID = (str(random.randint(0, 9))
                             + str(random.randint(0, 9))
                             + str(random.randint(0, 9))
                             + str(random.randint(0, 9)))
                if ProjectID not in project.select("ProjectID"):
                    break
            logins.update("ID", student.id, "role", "lead")
            project.insert({"ProjectID": ProjectID, "Title": "untitled",
                            "Lead": student.name(), "Member1": "none",
                            "Member2": "none", "Advisor": "none",
                            "Status": "has not submitted a project "
                                      "proposal"})
            project_data.insert(
                {"ProjectID": ProjectID, "Title": "untitled",
                 "Proposal": "none", "Report": "none",
                 "Status": "has not submitted a project "
                           "proposal"})
            print("You have become a lead student of your recently "
                  "created project.")
        else:
            print("Must deny all invitation requests first.")
        continue_or_not(student.id)

    if number == 4:
        print("Exit the program.")


def member_login(ID):
    member = User(ID)
    print("(1) See the details of the project status")
    print("(2) See the details of the project data")
    print("(3) See the details of the proposal data")
    print("(4) Exit")
    print("Note: Only a lead student is allowed to SUBMIT the modification "
          "into the program. A member must privately send their modification "
          "of their project to their lead student.")
    number = input_number(4)

    their_project_status = project.filter(lambda x:
                                          x["Member1"] == member.name())
    if not their_project_status.table:
        their_project_status = project.filter(lambda x:
                                              x["Member2"] == member.name())
    dict_project_status = their_project_status.table[0]
    ProjectID = their_project_status.table[0]["ProjectID"]
    their_project_data = project_data.filter(lambda x:
                                             x["ProjectID"] == ProjectID)
    dict_project_data = their_project_data.table[0]

    if number == 1:
        display(project_key, dict_project_status)
        continue_or_not(member.id)

    elif number == 2:
        display(project_data_key, dict_project_data)
        continue_or_not(member.id)

    elif number == 3:
        the_project = proposal_data.filter(lambda x:
                                           x["ProjectID"] == ProjectID).table
        if the_project:
            format_solo(proposal_data_key, the_project)
        else:
            print("Your project hasn't been submitted a project proposal yet.")
        continue_or_not(member.id)

    elif number == 4:
        print("Exit the program.")


def lead_login(ID):
    lead = User(ID)
    print("(1) See the details of the project status")
    print("(2) See the details of the project data")
    print("(3) See the details of the proposal data")
    print("(4) Modify and/or submit the project and "
          "the project proposal/report")
    print("(5) Find all non-member students")
    print("(6) Find all faculties")
    print("(7) Send invitational messages to potential members")
    print("(8) Send invitational messages to potential advisors")
    print("(9) Exit")
    number = input_number(9)

    their_project_status = project.filter(lambda x:
                                          x["Lead"] == lead.name())
    dict_project_status = their_project_status.table[0]
    ProjectID = dict_project_status["ProjectID"]
    their_project_data = project_data.filter(lambda x:
                                             x["ProjectID"] == ProjectID)
    dict_project_data = their_project_data.table[0]

    if number == 1:
        display(project_key, dict_project_status)
        continue_or_not(lead.id)

    elif number == 2:
        display(project_data_key, dict_project_data)
        continue_or_not(lead.id)

    elif number == 3:
        the_project = proposal_data.filter(lambda x:
                                           x["ProjectID"] == ProjectID).table
        if the_project:
            format_solo(proposal_data_key, the_project)
        else:
            print("Your project hasn't been submitted a project proposal yet.")
        continue_or_not(lead.id)

    elif number == 4:
        print("(1) Modify the project title")
        print("(2) Modify and/or submit the project proposal")
        print("(3) Modify and/or submit the finale project report")
        number = input_number(3)

        if number == 1:
            if dict_project_status["Status"] == ("a finale project report "
                                                 "approval; approved"):
                print("The finale project report has been approved. "
                      "You can't change the title.")
            elif dict_project_status["Status"] == ("has submitted a "
                                                   "finale project report "
                                                   "(waiting for advisor "
                                                   "approval)"):
                print("The finale project report has been waiting "
                      "for advisor approval. You can't change the title.")
            else:
                the_title = str(input("Input a new title: "))
                project.update("ProjectID", ProjectID, "Title", the_title)
                project_data.update("ProjectID", ProjectID, "Title", the_title)
                print("You have modified the project title.")

        elif number == 2:
            if ((dict_project_status["Title"] == "untitled") or
                    dict_project_status["Member1"] == "none" or
                    dict_project_status["Member2"] == "none" or
                    dict_project_status["Advisor"] == "none"):
                print("Must has an advisor, a title, and all members before "
                      "sending a project proposal. Check your project "
                      "details.")
            else:
                if ((dict_project_status["Status"] == "has not submitted a "
                                                      "project proposal") or
                        (dict_project_status["Status"] == "a project "
                                                          "proposal "
                                                          "evaluation; "
                                                          "disapproved")):
                    proposal = str(input("Input your proposal PDF link: "))
                    project_data.update("ProjectID", ProjectID,
                                        "Proposal", proposal)
                    project_data.update("ProjectID", ProjectID,
                                        "Status", "has submitted a project "
                                                  "proposal (waiting for "
                                                  "evaluation)")
                    project.update("ProjectID", ProjectID,
                                   "Status", "has submitted a project "
                                             "proposal (waiting for "
                                             "evaluation)")
                    proposal_data.insert({"ProjectID": ProjectID,
                                          "eva_1": "waiting for evaluation",
                                          "review_1": "none",
                                          "eva_2": "waiting for evaluation",
                                          "review_2": "none",
                                          "eva_3": "waiting for evaluation",
                                          "review_3": "none",
                                          "result": "waiting for evaluation",
                                          "proposal": proposal,
                                          "faculty_1": "none",
                                          "faculty_2": "none",
                                          "faculty_3": "none"})
                    print("You have modified and/or submitted the project "
                          "proposal.")
                elif dict_project_status["Status"] == ("has submitted a "
                                                       "project proposal "
                                                       "(waiting for "
                                                       "evaluation)"):
                    print("Denied: The project proposal has already been "
                          "waiting for evaluation.")
                else:
                    print("Denied: The project proposal has already been "
                          "approved.")

        elif number == 3:
            if ((dict_project_status["Status"] == "a project proposal "
                                                  "evaluation; approved "
                                                  "(waiting for a "
                                                  "project report)") or
                    (dict_project_status["Status"] == "a finale project "
                                                      "report approval; "
                                                      "disapproved")):
                report = str(input("Input a report: "))
                project_data.update("ProjectID", ProjectID, "Report", report)
                project_data.update("ProjectID", ProjectID,
                                    "Status", "has submitted a finale project "
                                              "report (waiting for "
                                              "advisor approval)")
                project.update("ProjectID", ProjectID,
                               "Status", "has submitted a finale project "
                                         "report (waiting for advisor "
                                         "approval)")
                print("You have modified and/or submitted the finale project "
                      "report.")
            elif dict_project_status["Status"] == ("has submitted a finale "
                                                   "project report (waiting "
                                                   "for advisor approval)"):
                print("Denied: The finale project report has already been "
                      "waiting for an advisor approval.")
            elif dict_project_status["Status"] == ("a finale project report "
                                                   "approval; approved"):
                print("Denied: The finale project report has already been "
                      "approved.")
            else:
                print("Denied: The proposal must have been approved before "
                      "submitting the finale project report.")
        continue_or_not(lead.id)

    elif number == 5:
        display_list(all_name("student"))
        continue_or_not(lead.id)

    elif number == 6:
        display_list(all_name("faculty"))
        continue_or_not(lead.id)

    elif number == 7:
        if ((dict_project_status["Member1"] != "none") and
                (dict_project_status["Member2"] != "none")):
            print("The members are already full.")
        else:
            while True:
                name = str(input("Input the username: "))
                if name in logins.filter(
                        lambda x:
                        (x["username"] == name) and
                        (x["role"] == "student")).aggregate(lambda x: x,
                                                            "username"):
                    break
                print("Please input valid username.")
            if member_pending_request.filter(
                    lambda x: (x["ProjectID"] == ProjectID) and
                              (x["to_be_member"] == name) and
                              (x["Response"] == "waiting for a "
                                                "response")).table:
                print("You have already sent the invitational message to "
                      "this user. Waiting for the answer.")
            else:
                member_pending_request.insert({"ProjectID": ProjectID,
                                               "to_be_member": name,
                                               "Response": "waiting for a "
                                                           "response",
                                               "Response_date": "none"})
                print("You have sent the invitation.")
        continue_or_not(lead.id)

    elif number == 8:
        if dict_project_status["Advisor"] != "none":
            print("The project already has an advisor.")
        else:
            request = advisor_pending_request.filter(
                lambda x:
                (x["ProjectID"] == ProjectID) and
                (x["Response"] == "waiting for a response"))
            if not request.table:
                if ((dict_project_status["Member1"] == "none") or
                        (dict_project_status["Member2"] == "none")):
                    print("You must find all the members first.")
                else:
                    while True:
                        name = str(input("Input the username: "))
                        if (name in logins.filter(
                                lambda x:
                                (x["username"] == name) and
                                (x["role"] == "faculty")).
                                aggregate(lambda x: x, "username")):
                            break
                        print("Please input valid username.")
                    if advisor_pending_request.filter(
                            lambda x: (x["ProjectID"] == ProjectID) and
                                      (x["to_be_advisor"] == name) and
                                      (x["Response"] == "waiting for "
                                                        "a response")).table:
                        print("You have already sent the invitational message "
                              "to this user. Waiting for the answer.")
                    else:
                        advisor_pending_request.insert(
                            {"ProjectID": ProjectID,
                             "to_be_advisor": name,
                             "Response": "waiting for a response",
                             "Response_date": "none"})
                        print("You have sent the invitation.")
            else:
                print("You can only send one invitation at one time. "
                      "(waiting for a response)")
        continue_or_not(lead.id)

    elif number == 9:
        print("Exit the program.")


def faculty_login(ID):
    faculty = User(ID)
    print("(1) See details of project status")
    print("(2) See details of project data")
    print("(3) See details of proposal data")
    print("(4) See invitations")
    print("(5) Accept or deny invitations")
    print("(6) Evaluate project proposals")
    print("(7) Exit")
    number = input_number(7)

    if number == 1:
        format_solo(project_key, project.table)
        continue_or_not(faculty.id)

    elif number == 2:
        format_solo(project_data_key, project_data.table)
        continue_or_not(faculty.id)

    elif number == 3:
        format_solo(proposal_data_key, proposal_data.table)
        continue_or_not(faculty.id)

    elif number == 4:
        list_response = advisor_pending_request.filter(
            lambda x:
            (x["to_be_advisor"] == faculty.name()) and
            (x["Response"] == "waiting for a response"))
        list_response = list_response.select("ProjectID")
        list_id_title = ["ProjectID, Title", ""]
        for i in list_response:
            for j, k in i.items():
                list_id_title.append(f"{k}, {title(k)}")
        display_list(list_id_title)
        continue_or_not(faculty.id)

    elif number == 5:
        answer = ""
        while True:
            ProjectID = str(input("Input ProjectID: "))
            if (advisor_pending_request.filter(
                    lambda x:
                    (x["to_be_advisor"] == faculty.name()) and
                    (x["ProjectID"] == ProjectID) and
                    (x["Response"] == "waiting for a response"))).table:
                break
            print("Please input a valid ProjectID.")
        for i in project.table:
            if i["ProjectID"] == ProjectID:
                if i["Advisor"] != "none":
                    print("The project already has an advisor.")
                    answer = "deny"
                else:
                    answer = accept_or_deny()
        if answer == "accept":
            advisor_pending_request.update_three("ProjectID",
                                                 ProjectID,
                                                 "to_be_advisor",
                                                 faculty.name(),
                                                 "Response",
                                                 "waiting for a response",
                                                 "Response",
                                                 "accepted",
                                                 "Response_date",
                                                 date_today())
            logins.update("ID", faculty.id, "role", "advisor")
            for i in project.table:
                if i["ProjectID"] == ProjectID:
                    i["Advisor"] = faculty.name()
            print("You have become an advisor of the project.")
        elif answer == "deny":
            advisor_pending_request.update_three("ProjectID",
                                                 ProjectID,
                                                 "to_be_advisor",
                                                 faculty.name(),
                                                 "Response",
                                                 "waiting for a response",
                                                 "Response",
                                                 "denied",
                                                 "Response_date",
                                                 date_today())
            print("You have denied the invitation.")
        continue_or_not(faculty.id)

    elif number == 6:
        print()
        project_waiting = proposal_data.filter(
            lambda x: x["result"] == "waiting for evaluation")
        print("The projects waiting for evaluation: ")
        if not project_waiting.table:
            print("No project waiting for evaluation right now.")
        else:
            format_solo(proposal_data_key, project_waiting.table)
            while True:
                ProjectID = str(input(f"Input ProjectID: "))
                result = project_waiting.filter(lambda x:
                                                x["ProjectID"] == ProjectID)
                if result.table:
                    break
                print("Please input valid ID.")
            the_project = result.table[0]
            if (the_project["faculty_1"] == faculty.name() or
                    the_project["faculty_2"] == faculty.name() or
                    the_project["faculty_3"] == faculty.name()):
                print("You have already evaluated this project proposal.")
            else:
                while True:
                    evaluation = str(input("Input your evaluation"
                                           "(disapproved/approved): "))
                    if evaluation in ["disapproved", "approved"]:
                        break
                    print("please input valid answer.")
                review = str(input("Input your review DPF link: "))
                if the_project["eva_1"] == "waiting for evaluation":
                    proposal_data.update_two("ProjectID", ProjectID,
                                             "result",
                                             "waiting for evaluation",
                                             "eva_1", evaluation,
                                             "review_1", review)
                    proposal_data.update_two("ProjectID", ProjectID,
                                             "result",
                                             "waiting for evaluation",
                                             "eva_1", evaluation,
                                             "faculty_1", faculty.name())
                elif the_project["eva_2"] == "waiting for evaluation":
                    proposal_data.update_two("ProjectID", ProjectID,
                                             "result",
                                             "waiting for evaluation",
                                             "eva_2", evaluation,
                                             "review_2", review)
                    proposal_data.update_two("ProjectID", ProjectID,
                                             "result",
                                             "waiting for evaluation",
                                             "eva_2", evaluation,
                                             "faculty_2", faculty.name())
                elif the_project["eva_3"] == "waiting for evaluation":
                    proposal_data.update_two("ProjectID", ProjectID,
                                             "result",
                                             "waiting for evaluation",
                                             "eva_3", evaluation,
                                             "review_3", review)
                    proposal_data.update_two("ProjectID", ProjectID,
                                             "result",
                                             "waiting for evaluation",
                                             "eva_3", evaluation,
                                             "faculty_3", faculty.name())
                    num = 0
                    if the_project["eva_1"] == "approved":
                        num += 1
                    if the_project["eva_2"] == "approved":
                        num += 1
                    if evaluation == "approved":
                        num += 1
                    if num >= 2:
                        proposal_data.update_two("ProjectID", ProjectID,
                                                 "result", "waiting for "
                                                           "evaluation",
                                                 "eva_3", evaluation,
                                                 "result", "approved")
                        project.update("ProjectID", ProjectID,
                                       "Status",
                                       "a project proposal evaluation; "
                                       "approved (waiting for a project "
                                       "report)")
                        project_data.update("ProjectID", ProjectID,
                                            "Status", "a project proposal "
                                                      "evaluation; "
                                                      "approved (waiting for a "
                                                      "project report)")
                    else:
                        proposal_data.update_two("ProjectID", ProjectID,
                                                 "result", "waiting for "
                                                           "evaluation",
                                                 "eva_3", evaluation,
                                                 "result", "disapproved")
                        project.update("ProjectID", ProjectID,
                                       "Status",
                                       "a project proposal evaluation; "
                                       "disapproved")
                        project_data.update("ProjectID", ProjectID,
                                            "Status", "a project proposal "
                                                      "evaluation; disapproved")
        continue_or_not(faculty.id)

    elif number == 7:
        print("Exit the program.")


def advisor_login(ID):
    advisor = User(ID)
    print("(1) See details of project status")
    print("(2) See details of project data")
    print("(3) See details of proposal data")
    print("(4) See the details of the project status you are "
          "serving as an advisor")
    print("(5) See the details of the project data you are "
          "serving as an advisor")
    print("(6) See the details of the proposal data you are "
          "serving as an advisor")
    print("(7) Evaluate project proposals")
    print("(8) Approve or deny a final project report approval")
    print("(9) Exit")
    number = input_number(9)

    their_project_status = project.filter(lambda x:
                                          x["Advisor"] == advisor.name())
    dict_project_status = their_project_status.table[0]
    ProjectID = dict_project_status["ProjectID"]
    their_project_data = project_data.filter(lambda x:
                                             x["ProjectID"] == ProjectID)
    dict_project_data = their_project_data.table[0]

    if number == 1:
        format_solo(project_key, project.table)
        continue_or_not(advisor.id)

    elif number == 2:
        format_solo(project_data_key, project_data.table)
        continue_or_not(advisor.id)

    elif number == 3:
        format_solo(proposal_data_key, proposal_data.table)
        continue_or_not(advisor.id)

    elif number == 4:
        display(project_key, dict_project_status)
        continue_or_not(advisor.id)

    elif number == 5:
        display(project_data_key, dict_project_data)
        continue_or_not(advisor.id)

    elif number == 6:
        the_project = proposal_data.filter(lambda x:
                                           x["ProjectID"] == ProjectID).table
        if the_project:
            format_solo(proposal_data_key, the_project)
        else:
            print("The project hasn't been submitted a project proposal yet.")
        continue_or_not(advisor.id)

    elif number == 7:
        print()
        project_waiting = proposal_data.filter(
            lambda x: x["result"] == "waiting for evaluation")
        print("The projects waiting for evaluation: ")
        if not project_waiting.table:
            print("No project waiting for evaluation right now.")
        else:
            format_solo(proposal_data_key, project_waiting.table)
            while True:
                ProjectID = str(input(f"Input ProjectID: "))
                result = project_waiting.filter(lambda x:
                                                x["ProjectID"] == ProjectID)
                if result.table:
                    break
                print("Please input valid ID.")
            the_project = result.table[0]
            if (the_project["faculty_1"] == advisor.name() or
                    the_project["faculty_2"] == advisor.name() or
                    the_project["faculty_3"] == advisor.name()):
                print("You have already evaluated this project proposal.")
            else:
                while True:
                    evaluation = str(input("Input your evaluation"
                                           "(disapproved/approved): "))
                    if evaluation in ["disapproved", "approved"]:
                        break
                    print("please input valid answer.")
                review = str(input("Input your review DPF link: "))
                if the_project["eva_1"] == "waiting for evaluation":
                    proposal_data.update_two("ProjectID", ProjectID,
                                             "result",
                                             "waiting for evaluation",
                                             "eva_1", evaluation,
                                             "review_1", review)
                    proposal_data.update_two("ProjectID", ProjectID,
                                             "result",
                                             "waiting for evaluation",
                                             "eva_1", evaluation,
                                             "faculty_1", advisor.name())
                elif the_project["eva_2"] == "waiting for evaluation":
                    proposal_data.update_two("ProjectID", ProjectID,
                                             "result",
                                             "waiting for evaluation",
                                             "eva_2", evaluation,
                                             "review_2", review)
                    proposal_data.update_two("ProjectID", ProjectID,
                                             "result",
                                             "waiting for evaluation",
                                             "eva_2", evaluation,
                                             "faculty_2", advisor.name())
                elif the_project["eva_3"] == "waiting for evaluation":
                    proposal_data.update_two("ProjectID", ProjectID,
                                             "result",
                                             "waiting for evaluation",
                                             "eva_3", evaluation,
                                             "review_3", review)
                    proposal_data.update_two("ProjectID", ProjectID,
                                             "result",
                                             "waiting for evaluation",
                                             "eva_3", evaluation,
                                             "faculty_3", advisor.name())
                    num = 0
                    if the_project["eva_1"] == "approved":
                        num += 1
                    if the_project["eva_2"] == "approved":
                        num += 1
                    if evaluation == "approved":
                        num += 1
                    if num >= 2:
                        proposal_data.update_two("ProjectID", ProjectID,
                                                 "result", "waiting for "
                                                           "evaluation",
                                                 "eva_3", evaluation,
                                                 "result", "approved")
                        project.update("ProjectID", ProjectID,
                                       "Status",
                                       "a project proposal evaluation; "
                                       "approved (waiting for a project "
                                       "report)")
                        project_data.update("ProjectID", ProjectID,
                                            "Status", "a project proposal "
                                                      "evaluation; "
                                                      "approved (waiting for a "
                                                      "project report)")
                    else:
                        proposal_data.update_two("ProjectID", ProjectID,
                                                 "result", "waiting for "
                                                           "evaluation",
                                                 "eva_3", evaluation,
                                                 "result", "disapproved")
                        project.update("ProjectID", ProjectID,
                                       "Status",
                                       "a project proposal evaluation; "
                                       "disapproved")
                        project_data.update("ProjectID", ProjectID,
                                            "Status", "a project proposal "
                                                      "evaluation; disapproved")
        continue_or_not(advisor.id)

    elif number == 8:
        if dict_project_data["Report"] == "none":
            print("The project hasn't been submitted a finale project "
                  "report yet.")
        elif dict_project_data["Status"] == ("a finale project report "
                                             "approval; approved"):
            print("The finale project report has already been approved.")
        elif dict_project_data["Status"] == ("a finale project report "
                                             "approval; disapproved"):
            print("The project hasn't been submitted a new finale "
                  "project report yet.")
        else:
            print()
            print("The finale project report waiting for approval: ")
            print_dict(dict_project_data)
            print()
            while True:
                approval = str(input("Input your approval"
                                     "(disapproved/approved): "))
                if approval in ["disapproved", "approved"]:
                    break
                print("please input valid answer.")
            if approval == "approved":
                project_data.update("ProjectID", ProjectID,
                                    "Status", "a finale project report "
                                              "approval; approved")
                project.update("ProjectID", ProjectID,
                               "Status", "a finale project report "
                                         "approval; approved")
            elif approval == "disapproved":
                project_data.update("ProjectID", ProjectID,
                                    "Status", "a finale project report "
                                              "approval; disapproved")
                project.update("ProjectID", ProjectID,
                               "Status", "a finale project report approval; "
                                         "disapproved")
        continue_or_not(advisor.id)

    elif number == 9:
        print("Exit the program.")


initializing()
logins = my_database.search("login")
project = my_database.search("project")
persons = my_database.search("persons")
advisor_pending_request = my_database.search("advisor_pending_request")
member_pending_request = my_database.search("member_pending_request")
project_data = my_database.search("project_data")
proposal_data = my_database.search("proposal_data")

print()
val = login()
check_role(val[1], val[0])
exit()
