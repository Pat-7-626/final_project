# The roles

___

- An admin
    - Can see and update all information in the database
        - Can update Person table
        - Can update Login table
        - Can update Project table
        - Can update Advisor_pending_request table
        - Can update Member_pending_request table 

    #### if val[1] = 'admin':

    Input what a user wants to do
  - If seeing a table: display that table
  - If seeing a project status: display the project dictionary that is in Project table
  - If seeing members pending requests of a project: display that project dictionary in Member_pending_request table
  - If seeing an advisor pending request of a project: display that project dictionary in Advisor_pending_request table
  - If updating a dictionary in a table: call a function that allows to update a dictionary in a table
  - If updating a value associated with a key in a table: call a function that allows to update a value associated with a key in a table

___

- A lead student (*)
    - Can see a project status
    - Can create, see, and modify a project (creating a project is in student part, before becoming a lead student)
        - Project table needs to be updated
    - Can find and send invitational messages to potential members
        - Member_pending_request table needs to be updated
    - Can find and send invitational messages to potential advisors; can only send one invitation at one time and only after finding all the members
        - Member_pending_request table needs to be updated

    #### if val[1] = 'lead':

    Input what a user wants to do
  - If seeing a project status: display the project dictionary in Project table
  - If modifying a project status: call a function that allows to update a dictionary in Project table or to update a value associated with a key in Project table
  - If finding all potential members: display all students that aren't members of some projects yet.
  - If finding all potential advisors: display all faculties.
  - If sending invitational messages to potential members: call a function that allows to update a value associated with a key in Advisor_pending_request table
  - If sending invitational messages to potential advisors: call a function that allows to update a value associated with a key in Member_pending_request table (conditions: sent one request at one time -> checking Advisor_pending_request table, must not have any pending -> check in Member_pending_request table)

___

- A member student (**)
    - Can see and modify a project
        - Project table needs to be updated
    
    #### if val[1] = 'member':

    Input what a user wants to do
    - If seeing a project status: display the project dictionary in Project table
    - If modifying a project status: call a function that allows to update a dictionary in Project table or to update a value associated with a key in Project table

___

- an advisor (***)
    - Can see details of a project
        - Can see a project status
    - Get a project proposal from the group project
    - Can approve the proposal
    - Get a finished project report from the group project
    - Can approve the project
        - Project table needs to be updated
    - Can see other invitations to be an advisor from other lead students
    - Can accept or deny the invitations from lead students
        - Advisor_pending_request table needs to be updated
        - if accepting; also become an advisor for another project
            - Project table needs to be updated
    - Evaluate projects (in Proposal.md)
    
    #### if val[1] = 'advisor':

    Input what a user wants to do
    - If seeing a project status: display the project dictionary in Project table
    - If approving a project proposal: call a function that allows to update a value associated with a key in Project table
    - If approving a project report: call a function that allows to update a value associated with a key in Project table
    - If seeing invitations: display the invitation from Advisor_pending_request table
    - If accepting invitations: call a function that allows to update a value associated with a key in Project table and Advisor_pending_request table
    - If denying invitations: call a function that allows to update a value associated with a key in Advisor_pending_request table 
    - ***Evaluate projects***

___

- A student
    - Can see invitations to be a member from lead students
    - Can accept or deny the invitations
        - Member_pending_request table needs to be updated
        - if accepting; become a member student
          - Project table needs to be updated
          - Can do all things a member student can do (**)
    - Can create a project and become a lead student; must deny all requests first
        - Login table needs to be updated
        - Project table needs to be updated
        - Can do all things a lead student can do (*)
    
    #### if val[1] = 'student':

    Input what a user wants to do
    - If seeing invitations: display the invitation from Member_pending_request table
    - If accepting invitations: call a function that allows to update a value associated with a key in Project table, Login table and Member_pending_request table
    - If denying invitations: call a function that allows to update a value associated with a key in Member_pending_request table
    - If creating a project: call a function that allows to update a dictionary in Project table, Advisor_pending_request table, and Member_pending_request table (becoming a lead student; call a function that allows to update a value associated with a key in Login table, then go into Lead class) (conditions: must deny all request first -> check in Member_pending_request table)

___

- a faculty
    - Can see details of a project
        - Can see a project status
    - Evaluate projects (in Proposal.md)
    - Can see invitations to be an advisor 
    - Can accept or deny the invitations from lead students
        - Advisor_pending_request table needs to be updated
        - if accepting; become an advisor
            - Project table needs to be updated
            - Can do all things an advisor can do (***)

    #### if val[1] = 'faculty':

    Input what a user wants to do
    - If seeing a project status: display the project dictionary in Project table
    - If seeing invitations: display the invitation from Advisor_pending_request table
    - If accepting invitations: call a function that allows to update a value associated with a key in Project table, Login table and Advisor_pending_request table (becoming an advisor; call a function that allows to update a value associated with a key in Login table, then go into advisor class)
    - If denying invitations: call a function that allows to update a value associated with a key in Advisor_pending_request table 
    - ***Evaluate projects***