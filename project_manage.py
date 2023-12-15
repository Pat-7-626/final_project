# import database module
from datetime import date
import database
import random

my_database = database.DB()


# define a function called initializing
def initializing():
    # here are things to do in this function:
    # create an object to read all csv files that will serve
    # as a persistent state for this program
    persons_csv = database.csv_path("persons")
    login_csv = database.csv_path("login")
    project_csv = database.csv_path("project")
    advisor_pending_request_csv = database.csv_path("advisor_pending_request")
    member_pending_request_csv = database.csv_path("member_pending_request")
    project_data_csv = database.csv_path("project_data")

    # create all the corresponding tables for those csv files
    # see the guide how many tables are needed
    persons = database.Table("persons", persons_csv)
    logins = database.Table("login", login_csv)
    project = database.Table("project", project_csv)
    advisor_pending_request = database.Table("advisor_pending_request",
                                             advisor_pending_request_csv)
    member_pending_request = database.Table("member_pending_request",
                                            member_pending_request_csv)
    project_data = database.Table("project_data", project_data_csv)

    # add all these tables to the database
    my_database.insert(persons)
    my_database.insert(logins)
    my_database.insert(project)
    my_database.insert(advisor_pending_request)
    my_database.insert(member_pending_request)
    my_database.insert(project_data)


# define a function called login
def login():
    # here are things to do in this function:
    # add code that performs a login task
    # ask a user for a username and password
    # returns [ID, role] if valid, otherwise returning None
    logins = my_database.search("login")
    user = str(input("Enter the username: "))
    password = str(input("Enter the password: "))
    user = (logins.filter(lambda x: x["username"] == user)
            .filter(lambda x: x["password"] == password))
    if not user.table:
        result = None
    else:
        result = [user.table[0]["ID"], user.table[0]["role"]]
    return result


# define a function called exit here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv
# files By now, you know how to read in a csv file and transform it into a
# list of dictionaries. For this project, you also need to know how to do
# the reverse, i.e., writing out to a csv file given a list of dictionaries.
# See the link below for a tutorial on how to do this:
# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python
def exit():
    database.update_csv(my_database.search("persons"),
                        ["ID", "first",
                         "last", "type"])
    database.update_csv(my_database.search("login"),
                        ["ID", "username",
                         "password", "role"])
    database.update_csv(my_database.search("project"),
                        ["ProjectID", "Title",
                         "Lead", "Member1",
                         "Member2", "Advisor",
                         "Status"])
    database.update_csv(my_database.search("advisor_pending_request"),
                        ["ProjectID", "to_be_advisor",
                         "Response", "Response_date"])
    database.update_csv(my_database.search("member_pending_request"),
                        ["ProjectID", "to_be_member",
                         "Response", "Response_date"])
    database.update_csv(my_database.search("project_data"),
                        ["ProjectID", "Title",
                         "Proposal", "Report",
                         "Status"])


# make calls to the initializing and login functions defined above
initializing()
logins = my_database.search("login")
project = my_database.search("project")
persons = my_database.search("persons")
advisor_pending_request = my_database.search("advisor_pending_request")
member_pending_request = my_database.search("member_pending_request")
project_data = my_database.search("project_data")
print(logins)
val = login()


# based on the return value for login, activate the code that performs
# activities according to the role defined for that person_id

# if val[1] = 'admin':
# see and do admin related activities
# elif val[1] = 'student':
# see and do student related activities
# elif val[1] = 'member':
# see and do member related activities
# elif val[1] = 'lead':
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities


class User:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    def name(self):
        return username(self.id)


def admin_login(id):
    admin = User(id)
    print("(1) See information")
    print("(2) Update information")
    print("(3) Exit")
    number = input_number([1, 2, 3])

    if number == 1:
        print("(1) Persons Table")
        print("(2) Login Table")
        print("(3) Project Table")
        print("(4) Project_data Table")
        print("(5) Member_pending_request Table")
        print("(6) Advisor_pending_request Table")
        number = input_number([1, 2, 3, 4, 5, 6])

        if number == 1:
            head_format = (f"{"ID":^25}{"first":^25}"
                           f"{"last":^25}{"type":^25}")
            print()
            print("___________________________________________________________"
                  "_________________________________________")
            print()
            print(f"{head_format:^100}")
            print()
            for i in persons.table:
                info_format = (f"{i["ID"]:^25}{i["first"]:^25}"
                               f"{i["last"]:^25}{i["type"]:^25}")
                print(f"{info_format:^100}")
            print()
            print("___________________________________________________________"
                  "_________________________________________")
            print()
            continue_or_not(admin.id)

        if number == 2:
            head_format = (f"{"ID":^25}{"username":^25}"
                           f"{"password":^25}{"role":^25}")
            print()
            print("___________________________________________________________"
                  "_________________________________________")
            print()
            print(f"{head_format:^100}")
            print()
            for i in logins.table:
                info_format = (f"{i["ID"]:^25}{i["username"]:^25}"
                               f"{i["password"]:^25}{i["role"]:^25}")
                print(f"{info_format:^100}")
            print()
            print("___________________________________________________________"
                  "_________________________________________")
            print()
            continue_or_not(admin.id)

        if number == 3:
            print()
            print("___________________________________________________________"
                  "_________________________________________")
            print()
            for i in project.table:
                info_format = (f"   ProjectID: {i["ProjectID"]}\n"
                               f"   Title: {i["Title"]}\n"
                               f"   Lead: {i["Lead"]}\n"
                               f"   Member1: {i["Member1"]}\n"
                               f"   Member2: {i["Member2"]}\n"
                               f"   Advisor: {i["Advisor"]}\n"
                               f"   Status: {i["Status"]}\n")
                print(f"{info_format}")
            print("___________________________________________________________"
                  "_________________________________________")
            print()
            continue_or_not(admin.id)

        if number == 4:
            print()
            print("___________________________________________________________"
                  "_________________________________________")
            print()
            for i in project_data.table:
                info_format = (f"   ProjectID: {i["ProjectID"]}\n"
                               f"   Title: {i["Title"]}\n"
                               f"   Proposal: {i["Proposal"]}\n"
                               f"   Report: {i["Report"]}\n"
                               f"   Status: {i["Status"]}\n")
                print(f"{info_format}")
            print("___________________________________________________________"
                  "_________________________________________")
            print()
            continue_or_not(admin.id)

        if number == 5:
            head_format = (f"{"ProjectID":^25}{"to_be_member":^25}"
                           f"{"Response":^25}{"Response_date":^25}")
            print()
            print("___________________________________________________________"
                  "_________________________________________")
            print()
            print(f"{head_format:^100}")
            print()
            for i in member_pending_request.table:
                info_format = (f"{i["ProjectID"]:^25}{i["to_be_member"]:^25}"
                               f"{i["Response"]:^25}{i["Response_date"]:^25}")
                print(f"{info_format:^100}")
            print()
            print("___________________________________________________________"
                  "_________________________________________")
            print()
            continue_or_not(admin.id)

        if number == 6:
            head_format = (f"{"ProjectID":^25}{"to_be_advisor":^25}"
                           f"{"Response":^25}{"Response_date":^25}")
            print()
            print("___________________________________________________________"
                  "_________________________________________")
            print()
            print(f"{head_format:^100}")
            print()
            for i in advisor_pending_request.table:
                info_format = (f"{i["ProjectID"]:^25}{i["to_be_advisor"]:^25}"
                               f"{i["Response"]:^25}{i["Response_date"]:^25}")
                print(f"{info_format:^100}")
            print()
            print("___________________________________________________________"
                  "_________________________________________")
            print()
            continue_or_not(admin.id)

    if number == 2:
        pass #fuck


def student_login(id):
    student = User(id)
    print("(1) See invitations")
    print("(2) Accept or deny invitations")
    print("(3) Create a project")
    print("(4) Exit")
    number = input_number([1, 2, 3, 4])

    if number == 1:
        list_response = (member_pending_request.filter(
            lambda x:
            (x["to_be_member"] == student.name()) and
            (x["Response"] == "waiting for a response")))
        list_response = list_response.select("ProjectID")
        list_id_title = []
        for i in list_response:
            for j, k in i.items():
                list_id_title.append(f"{k}, {title(k)}")
        display_list(list_id_title)
        continue_or_not(student.id)

    if number == 2:
        while True:
            ProjectID = str(input("Input ProjectID: "))
            if ((member_pending_request.filter(
                    lambda x:
                    (x["to_be_member"] == student.name())
                    and (x["Response"] == "waiting for a response")
                    and (x["ProjectID"] == ProjectID))).table):
                break
            print("Please input a valid ProjectID.")
        while True:
            answer = str(input("Do you wish to accept or deny?"
                               "(accept/deny): "))
            if (answer == "accept") or (answer == "deny"):
                break
            print("Please input a valid answer.")
        for i in project.table:
            if i["ProjectID"] == ProjectID:
                if (i["Member1"] != "none") and (i["Member2"] != "none"):
                    print("The members are already full.")
                    answer = "deny"
        if answer == "accept":
            two_val_update(member_pending_request, "ProjectID",
                           ProjectID, "to_be_member",
                           student.name(), "Response",
                           "accepted", "Response_date",
                           date_today())
            logins.update("ID", student.id, "role", "member")
            for i in project.table:
                if i["ProjectID"] == ProjectID:
                    if i["Member1"] == "none":
                        i["Member1"] = student.name()
                    else:
                        i["Member2"] = student.name()
            print("You have become a member student of the project.")
        elif answer == "deny":
            two_val_update(member_pending_request, "ProjectID",
                           ProjectID, "to_be_member",
                           student.name(), "Response",
                           "denied", "Response_date",
                           date_today())
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
                            "Status": "has not submitted a project proposal"})
            project_data.insert({"ProjectID": ProjectID, "Title": "untitled",
                                 "Proposal": "none", "Report": "none",
                                 "Status": "has not submitted a project "
                                           "proposal"})
            print("You have become a lead student of your recently created "
                  "project.")
        else:
            print("Must deny all invitation requests first.")
        continue_or_not(student.id)

    if number == 4:
        print("Exit the program.")


def member_login(id):
    member = User(id)
    print("(1) See the details of the project status")
    print("(2) See the details of the project data")
    print("(3) Exit")
    print("Note: Only a lead student is allowed to SUBMIT the modification "
          "into the program. A member must privately send their modification "
          "of their project to their lead student.")
    number = input_number([1, 2, 3, 4])

    their_project_status = project.filter(
        lambda x:
        x["Member1"] == member.name())
    if not their_project_status.table:
        their_project_status = project.filter(
            lambda x:
            x["Member2"] == member.name())
    dict_project_status = their_project_status.table[0]
    ProjectID = dict_project_status["ProjectID"]
    their_project_data = project_data.filter(
        lambda x:
        x["ProjectID"] == ProjectID)
    dict_project_data = their_project_data.table[0]

    if number == 1:
        list_word = [f"ProjectID: {dict_project_status["ProjectID"]}",
                     f"Title: {dict_project_status["Title"]}",
                     f"Lead: {dict_project_status["Lead"]}",
                     f"Member1: {dict_project_status["Member1"]}",
                     f"Member2: {dict_project_status["Member2"]}",
                     f"Advisor: {dict_project_status["Advisor"]}",
                     f"Status: {dict_project_status["Status"]}"]
        display_list(list_word)
        continue_or_not(member.id)

    elif number == 2:
        list_word = [f"ProjectID: {dict_project_data["ProjectID"]}",
                     f"Title: {dict_project_data["Title"]}",
                     f"Proposal: {dict_project_data["Proposal"]}",
                     f"Report: {dict_project_data["Report"]}",
                     f"Status: {dict_project_data["Status"]}"]
        display_list(list_word)
        continue_or_not(member.id)

    elif number == 3:
        print("Exit the program.")


def lead_login(id):
    lead = User(id)
    print("(1) See the details of the project status")
    print("(2) See the details of the project data")
    print("(3) Modify and/or submit the project proposal/report")
    print("(4) Find all non-member students")
    print("(5) Find all faculties")
    print("(6) Send invitational messages to potential members")
    print("(7) Send invitational messages to potential advisors")
    print("(8) Exit")
    number = input_number([1, 2, 3, 4, 5, 6, 7, 8])

    their_project_status = project.filter(
        lambda x:
        x["Lead"] == lead.name())
    dict_project_status = their_project_status.table[0]
    ProjectID = dict_project_status["ProjectID"]
    their_project_data = project_data.filter(
        lambda x:
        x["ProjectID"] == ProjectID)
    dict_project_data = their_project_data.table[0]

    if number == 1:
        list_word = [f"ProjectID: {dict_project_status["ProjectID"]}",
                     f"Title: {dict_project_status["Title"]}",
                     f"Lead: {dict_project_status["Lead"]}",
                     f"Member1: {dict_project_status["Member1"]}",
                     f"Member2: {dict_project_status["Member2"]}",
                     f"Advisor: {dict_project_status["Advisor"]}",
                     f"Status: {dict_project_status["Status"]}"]
        display_list(list_word)
        continue_or_not(lead.id)

    elif number == 2:
        list_word = [f"ProjectID: {dict_project_data["ProjectID"]}",
                     f"Title: {dict_project_data["Title"]}",
                     f"Proposal: {dict_project_data["Proposal"]}",
                     f"Report: {dict_project_data["Report"]}",
                     f"Status: {dict_project_data["Status"]}"]
        display_list(list_word)
        continue_or_not(lead.id)

    elif number == 3:
        print("(1) Modify the project title")
        print("(2) Modify and/or submit the project proposal")
        print("(3) Modify and/or submit the finale project report")
        number = input_number([1, 2, 3])

        if number == 1:
            title = str(input("Input a new title: "))
            project.update("ProjectID", ProjectID, "Title", title)
            project_data.update("ProjectID", ProjectID, "Title", title)
            print("You have modified the project title.")

        elif number == 2:
            if ((dict_project_status["Title"] == "untitled") or
                    dict_project_status["Member1"] == "none" or
                    dict_project_status["Member2"] == "none" or
                    dict_project_status["Advisor"] == "none"):
                print("Must has all members, an advisor, and a title before "
                      "sending a project proposal. Check your project "
                      "details.")
            else:
                if ((dict_project_status["Status"] == "has not submitted a "
                                                      "project proposal") or
                        (dict_project_status["Status"] == "a project "
                                                          "proposal "
                                                          "evaluation; "
                                                          "disapproved")):
                    proposal = str(input("Input a proposal: "))
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
                      "waiting for advisor approval.")
            elif dict_project_status["Status"] == ("a finale project report "
                                                   "approval; approved"):
                print("Denied: The finale project report has already been "
                      "approved.")
            else:
                print("Denied: The proposal must have been approved before "
                      "submitting the finale project report.")
        continue_or_not(lead.id)

    elif number == 4:
        display_list(all_name("student"))
        continue_or_not(lead.id)

    elif number == 5:
        display_list(all_name("faculty"))
        continue_or_not(lead.id)

    elif number == 6:
        if ((dict_project_status["Member1"] != "none") and
                (dict_project_status["Member2"] != "none")):
            print("The members are already full.")
        else:
            name = str(input("Input the username: "))
            member_pending_request.insert({"ProjectID": ProjectID,
                                           "to_be_member": name,
                                           "Response": "waiting for a "
                                                       "response",
                                           "Response_date": "none"})
            print("You have sent the invitation.")
            continue_or_not(lead.id)

    elif number == 7:
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
                    name = str(input("Input the username: "))
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

    elif number == 8:
        print("Exit the program.")


def faculty_login(id):
    faculty = User(id)
    print("(1) See the details of project status")
    print("(2) See the details of project data")
    print("(3) See invitations")
    print("(4) Accept or deny invitations")
    print("(5) Evaluate project proposals")
    print("(6) Exit")
    number = input_number([1, 2, 3, 4, 5, 6])

    if number == 1:
        ProjectID = str(input("Input a ProjectID: "))
        their_project_status = project.filter(
            lambda x:
            x["ProjectID"] == ProjectID)
        dict_project_status = their_project_status.table[0]
        list_word = [f"ProjectID: {dict_project_status["ProjectID"]}",
                     f"Title: {dict_project_status["Title"]}",
                     f"Lead: {dict_project_status["Lead"]}",
                     f"Member1: {dict_project_status["Member1"]}",
                     f"Member2: {dict_project_status["Member2"]}",
                     f"Advisor: {dict_project_status["Advisor"]}",
                     f"Status: {dict_project_status["Status"]}"]
        display_list(list_word)
        continue_or_not(faculty.id)

    elif number == 2:
        ProjectID = str(input("Input a ProjectID: "))
        their_project_data = project_data.filter(
            lambda x:
            x["ProjectID"] == ProjectID)
        dict_project_data = their_project_data.table[0]
        list_word = [f"ProjectID: {dict_project_data["ProjectID"]}",
                     f"Title: {dict_project_data["Title"]}",
                     f"Proposal: {dict_project_data["Proposal"]}",
                     f"Report: {dict_project_data["Report"]}",
                     f"Status: {dict_project_data["Status"]}"]
        display_list(list_word)
        continue_or_not(faculty.id)

    elif number == 3:
        list_response = advisor_pending_request.filter(
            lambda x:
            (x["to_be_advisor"] == faculty.name()) and
            (x["Response"] == "waiting for a response"))
        list_response = list_response.select("ProjectID")
        list_id_title = []
        for i in list_response:
            for j, k in i.items():
                list_id_title.append(f"{k}, {title(k)}")
        display_list(list_id_title)
        continue_or_not(faculty.id)

    elif number == 4:
        while True:
            ProjectID = str(input("Input ProjectID: "))
            if (advisor_pending_request.filter(
                    lambda x:
                    (x["to_be_advisor"] == faculty.name()) and
                    (x["ProjectID"] == ProjectID) and
                    (x["Response"] == "waiting for a response"))).table:
                break
            print("Please input a valid ProjectID.")
        while True:
            answer = str(input("Do you wish to accept or deny?"
                               "(accept/deny): "))
            if (answer == "accept") or (answer == "deny"):
                break
            print("Please input a valid answer.")
        for i in project.table:
            if i["ProjectID"] == ProjectID:
                if i["Advisor"] != "none":
                    print("The project already has an advisor.")
                    answer = "deny"
        if answer == "accept":
            two_val_update(advisor_pending_request, "ProjectID",
                           ProjectID, "to_be_advisor",
                           faculty.name(), "Response",
                           "accepted", "Response_date",
                           date_today())
            logins.update("ID", faculty.id, "role", "advisor")
            for i in project.table:
                if i["ProjectID"] == ProjectID:
                    i["Advisor"] = faculty.name()
            print("You have become an advisor of the project.")
        elif answer == "deny":
            two_val_update(advisor_pending_request, "ProjectID",
                           ProjectID, "to_be_advisor",
                           faculty.name(), "Response",
                           "denied", "Response_date",
                           date_today())
            print("You have denied the invitation.")
        continue_or_not(faculty.id)

    elif number == 5:
        pass  # shit

    elif number == 6:
        print("Exit the program.")


def advisor_login(id):
    advisor = User(id)
    print("(1) See the details of project status")
    print("(2) See the details of project data")
    print("(3) See the details of the project status you are serving as an "
          "advisor")
    print("(4) See the details of the project data you are serving as an "
          "advisor")
    print("(5) Evaluate project proposals")
    print("(6) Approve or deny a final project report approval")
    print("(7) Exit")
    number = input_number([1, 2, 3, 4, 5, 6, 7])

    their_project_status = project.filter(
        lambda x:
        x["Advisor"] == advisor.name())
    dict_project_status = their_project_status.table[0]
    ProjectID = dict_project_status["ProjectID"]
    their_project_data = project_data.filter(
        lambda x:
        x["ProjectID"] == ProjectID)
    dict_project_data = their_project_data.table[0]

    if number == 1:
        ProjectID = str(input("Input a ProjectID: "))
        their_project_status = project.filter(
            lambda x:
            x["ProjectID"] == ProjectID)
        dict_project_status = their_project_status.table[0]
        list_word = [f"ProjectID: {dict_project_status["ProjectID"]}",
                     f"Title: {dict_project_status["Title"]}",
                     f"Lead: {dict_project_status["Lead"]}",
                     f"Member1: {dict_project_status["Member1"]}",
                     f"Member2: {dict_project_status["Member2"]}",
                     f"Advisor: {dict_project_status["Advisor"]}",
                     f"Status: {dict_project_status["Status"]}"]
        display_list(list_word)
        continue_or_not(advisor.id)

    elif number == 2:
        ProjectID = str(input("Input a ProjectID: "))
        their_project_data = project_data.filter(
            lambda x:
            x["ProjectID"] == ProjectID)
        dict_project_data = their_project_data.table[0]
        list_word = [f"ProjectID: {dict_project_data["ProjectID"]}",
                     f"Title: {dict_project_data["Title"]}",
                     f"Proposal: {dict_project_data["Proposal"]}",
                     f"Report: {dict_project_data["Report"]}",
                     f"Status: {dict_project_data["Status"]}"]
        display_list(list_word)
        continue_or_not(advisor.id)

    if number == 3:
        list_word = [f"ProjectID: {dict_project_status["ProjectID"]}",
                     f"Title: {dict_project_status["Title"]}",
                     f"Lead: {dict_project_status["Lead"]}",
                     f"Member1: {dict_project_status["Member1"]}",
                     f"Member2: {dict_project_status["Member2"]}",
                     f"Advisor: {dict_project_status["Advisor"]}",
                     f"Status: {dict_project_status["Status"]}"]
        display_list(list_word)
        continue_or_not(advisor.id)

    elif number == 4:
        list_word = [f"ProjectID: {dict_project_data["ProjectID"]}",
                     f"Title: {dict_project_data["Title"]}",
                     f"Proposal: {dict_project_data["Proposal"]}",
                     f"Report: {dict_project_data["Report"]}",
                     f"Status: {dict_project_data["Status"]}"]
        display_list(list_word)
        continue_or_not(advisor.id)

    elif number == 5:
        pass  # shit

    elif number == 6:
        pass  # shit

    elif number == 7:
        print("Exit the program.")


def all_name(role):
    user = logins.filter(
        lambda x:
        x["role"] == role)
    name_id_list = [f"{"ID":^20}{"Username":^20}",""]
    for i in user.table:
        name = f"{i["ID"]:^20}{i["username"]:^20}"
        name_id_list.append(name)
    return name_id_list


def input_number(list_number):
    while True:
        number = int(input("Input number: "))
        if number in list_number:
            break
        print("Please input a valid number.")
    return number


def username(id):
    user = logins.filter(lambda x:
                         x["ID"] == id)
    name = ""
    for i in user.table:
        name = i["username"]
    return name


def title(id):
    title = project.filter(lambda x:
                           x["ProjectID"] == id)
    return title.table[0]["Title"]


def role(id):
    role = logins.filter(lambda x:
                         x["ID"] == id)
    return role.table[0]["role"]


def display_list(list):
    print("___________________________________________________________"
          "_________________________________________")
    print()
    for i in list:
        print(f"{str(i):^100}")
    print()
    print("___________________________________________________________"
          "_________________________________________")
    print()


def continue_or_not(ID):
    exit()
    while True:
        answer = str(input("Do you wish to continue?(yes/no): "))
        if (answer == "yes") or (answer == "no"):
            break
        print("Please input a valid answer.")
    if answer == "yes":
        check_role(role(ID), ID)
    elif answer == "no":
        print("Exit the program.")


def two_val_update(table_name, key_id1, id_val1, key_id2,
                   id_val2, key_value1, value1, key_value2,
                   value2):
    for i in table_name.table:
        if (i[key_id1] == id_val1) and (i[key_id2] == id_val2):
            i[key_value1] = value1
            i[key_value2] = value2


def date_today():
    return str(date.today())


def check_role(role, id):
    if role == "admin":
        admin_login(id)
    elif role == "student":
        student_login(id)
    elif role == "member":
        member_login(id)
    elif role == "lead":
        lead_login(id)
    elif role == "faculty":
        faculty_login(id)
    elif role == "advisor":
        advisor_login(id)


check_role(val[1], val[0])  # fix when it is invalid
# once everything is done, make a call to the exit function
exit()