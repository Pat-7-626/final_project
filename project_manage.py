# import database module
import database

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

    # create all the corresponding tables for those csv files
    # see the guide how many tables are needed
    persons = database.Table("persons", persons_csv)
    logins = database.Table("login", login_csv)
    project = database.Table("project", project_csv)
    advisor_pending_request = database.Table("advisor_pending_request",
                                             advisor_pending_request_csv)
    member_pending_request = database.Table("member_pending_request",
                                            member_pending_request_csv)

    # add all these tables to the database
    my_database.insert(persons)
    my_database.insert(logins)
    my_database.insert(project)
    my_database.insert(advisor_pending_request)
    my_database.insert(member_pending_request)


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
                        ["ID", "fist",
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


# make calls to the initializing and login functions defined above
initializing()
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

# once everything is done, make a call to the exit function
exit()
