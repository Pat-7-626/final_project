# The roles

___

- ***An admin***
    - Can see and update all information in the database
        - Can update Person table
        - Can update Login table
        - Can update Project table
        - Can update Advisor_pending_request table
        - Can update Member_pending_request table
        - Can update Project_data table

    #### if val[1] = 'admin':

    Input what a user wants to do
  - If seeing a table: display that table
  - If updating a dictionary in a table: call a function that allows to update a dictionary in a table
  - If updating a value associated with a key in a table: call a function that allows to update a value associated with a key in a table

___

- ***A lead student (+)***
    - Can create, see, and modify a project (creating a project is in student part, before becoming a lead student)
        - Project table needs to be updated
        - Project_data table needs to be updated
    - Can find and send invitational messages to potential members
        - Member_pending_request table needs to be updated
    - Can find and send invitational messages to potential advisors; can only send one invitation at one time and only after finding all the members
        - Member_pending_request table needs to be updated
    - Can submit a project proposal to an advisor (***in Proposal.md***)
    - Can submit a final project report
        - Project table needs to be updated
        - Project_data table needs to be updated

    #### if val[1] = 'lead':

    Input what a user wants to do
  - If seeing a project details: display the project dictionary in Project table and Project_data table
  - If modifying a project: call a function that allows to update a dictionary in Project table or Project_data table or to update a value associated with a key in Project table or Project_data table
  - If finding all potential members: display all students that aren't members of some projects yet.
  - If finding all potential advisors: display all faculties.
  - If sending invitational messages to potential members: call a function that allows to update a value associated with a key in Advisor_pending_request table
  - If sending invitational messages to potential advisors: call a function that allows to update a value associated with a key in Member_pending_request table (conditions: sent one request at one time -> checking Advisor_pending_request table, must not have any pending -> check in Member_pending_request table)
  - If submitting a project proposal to an advisor: ***in Proposal.md***
  - If submitting a final project report: call a function that allows to update a value associated with a key in Project table and Project_data table

___

- ***A member student (++)***
    - Can see and modify a project
        - Project table needs to be updated
        - Project_data table needs to be updated
    
    #### if val[1] = 'member':

    Input what a user wants to do
    - If seeing a project details: display the project dictionary in Project table and Project_data table
    - If modifying a project status: call a function that allows to update a dictionary in Project table or Project_data table or to update a value associated with a key in Project table or Project_data table

___

- ***an advisor (+++)***
    - Can see details of a project
    - Can approve or deny a final project report approval
        - Project table needs to be updated
        - Project_data table needs to be updated
    - Can see other invitations to be an advisor from other lead students
    - Can accept or deny invitations from lead students
        - Advisor_pending_request table needs to be updated
        - if accepting; also become an advisor for another project
            - Project table needs to be updated
    - Evaluate project proposals (***in Proposal.md***)
    
    #### if val[1] = 'advisor':

    Input what a user wants to do
    - If seeing a project details: display the project dictionary in Project table and Project_data table
    - If approving or disapproving a final project report: call a function that allows to update a value associated with a key in Project table and Project_data table
    - If seeing invitations: display the invitation from Advisor_pending_request table
    - If accepting invitations: call a function that allows to update a value associated with a key in Project table and Advisor_pending_request table
    - If denying invitations: call a function that allows to update a value associated with a key in Advisor_pending_request table 
    - Evaluate projects (***in Proposal.md***)

___

- ***A student***
    - Can see invitations to be a member from lead students
    - Can accept or deny the invitations
        - Member_pending_request table needs to be updated
        - if accepting; become a member student
          - Project table needs to be updated
          - Can do all things a member student can do ***(++)***
    - Can create a project and become a lead student; must deny all requests first
        - Login table needs to be updated
        - Project table needs to be updated
        - Project_data table needs to be updated
        - Member_pending_request table needs to be updated
        - Advisor_pending_request table needs to be updated
        - Can do all things a lead student can do ***(+)***
    
    #### if val[1] = 'student':

    Input what a user wants to do
    - If seeing invitations: display the invitation from Member_pending_request table
    - If accepting invitations: call a function that allows to update a value associated with a key in Project table, Login table and Member_pending_request table
    - If denying invitations: call a function that allows to update a value associated with a key in Member_pending_request table
    - If creating a project: call a function that allows to update a dictionary in Project table, Project_data table, Advisor_pending_request table, and Member_pending_request table (becoming a lead student; call a function that allows to update a value associated with a key in Login table, then go into Lead class) (conditions: must deny all request first -> check in Member_pending_request table)

___

- ***a faculty***
    - Can see details of a project
    - Can see invitations to be an advisor 
    - Can accept or deny the invitations from lead students
        - Advisor_pending_request table needs to be updated
        - if accepting; become an advisor
            - Project table needs to be updated
            - Login table needs to be updated
            - Can do all things an advisor can do ***(+++)***
    - Evaluate project proposals (***in Proposal.md***)

    #### if val[1] = 'faculty':

    Input what a user wants to do
    - If seeing a project details: display the project dictionary in Project table and Project_data table
    - If seeing invitations: display the invitation from Advisor_pending_request table
    - If accepting invitations: call a function that allows to update a value associated with a key in Project table, Login table and Advisor_pending_request table (becoming an advisor; call a function that allows to update a value associated with a key in Login table, then go into advisor class)
    - If denying invitations: call a function that allows to update a value associated with a key in Advisor_pending_request table 
    - Evaluate projects (***in Proposal.md***)

---

# Notes: the tables

---

- ***Person table***
    - Attributes (or keys):
        - ID 
        - First 
        - Last 
        - Type
            - admin
            - student
            - faculty
---

- ***Login table***
    - Attributes (or keys):
        - ID
        - Username
        - Password
        - Role
            - admin
            - student
            - lead
            - member
            - faculty
            - advisor

---

- ***Project table***
    - Attributes (or keys):
        - ProjectID
        - Title
        - Lead
        - Member1 (optional)
        - Member2 (optional)
        - Advisor
        - Status
            - has not submitted a project proposal
            - has submitted a project proposal (waiting for evaluation)
            - a project proposal evaluation; disapproved
            - a project proposal evaluation; approved (waiting for a project report)
            - has submitted a finale project report (waiting for advisor approval)
            - a finale project report approval; disapproved
            - a finale project report approval; approved

---

- ***Advisor_pending_request table***
    - Attributes (or keys):
        - ProjectID
        - to_be_advisor
        - Response
            - accepted
            - denied
        - Response_date

---

- ***Member_pending_request table***
    - Attributes (or keys):
        - ProjectID
        - to_be_member
        - Response
            - accepted
            - denied
        - Response Response_date

---

- ***Project_data table***
    - Attributes (or keys):
        - ProjectID
        - Title
        - Proposal (a PDF link)
        - Report (a PDF link)
        - Status
            - has not submitted a project proposal
            - has submitted a project proposal (waiting for evaluation)
            - a project proposal evaluation; disapproved
            - a project proposal evaluation; approved (waiting for a project report)
            - has submitted a finale project report (waiting for advisor approval)
            - a finale project report approval; disapproved
            - a finale project report approval; approved
