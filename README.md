
---

## file
  - persons.csv
      - class: Table (persons in project_manage.py)
      - purpose: contain ID, fist, last, type
  - login.csv
      - class: Table (logins in project_manage.py)
      - purpose: contain ID, username, password, role
  - project.csv
      - class: Table (project in project_manage.py)
      - purpose: contain ProjectID, Title, Lead, Member1, Member2, Advisor, Status
  - project_data.csv
      - class: Table (project_data in project_manage.py)
      - purpose: contain ProjectID, Title, Proposal, Report, Status
  - advisor_pending_request.csv
      - class: Table (advisor_pending_request in project_manage.py)
      - purpose: contain ProjectID, to_be_advisor, Response, Response_date
  - member_pending_request.csv
      - class: Table (member_pending_request in project_manage.py)
      - purpose: contain ProjectID to_be_member, Response, Response_date
  - proposal_data.csv
      - class: Table (proposal_data in project_manage.py)
      - purpose: contain ProjectID ,eva_1, review_1, eva_2, review_2, eva_3, review_3, result, proposal, faculty_1, faculty_2, faculty_3
  - database.py
      - class: -
      - purpose: contain defining DB class, Table class, and function associating to csv files
  - project_manage.py
      - class: DB (my_database), Table (persons, logins, project, project_data, advisor_pending_request, member_pending_request, proposal_data), User (defined, all roles)
      - purpose: contain the main code part to make a finale project program

---

## How to compile and run your project?
Answer: press run, then input username and password


Missing features and outstanding bugs: none

---

                    Role                    |                    action                    |                    method                    |                    class                    |                    completion %                    



                   admin                    |               See information                |           format_table,format_solo,          |               all Tables,admin              |                        100 %                    
                                                                                                           continue_or_not                                                                      

                   admin                    |              Update information              |         check_id,print_dict,new_data         |               all Tables,admin              |                        100 %
                                                                                                    new_dictionary,continue_or_not
                                                                                                          filter,aggregate

                   admin                    |                     Exit                     |         continue_or_not,input_number         |                    admin                    |                        100 %                   

                  student                   |                See invitations               |          filter,select,display_list          |        member_pending_request,student       |                        100 %                 
                                                                                                          continue_or_not        

                  student                   |           Accept or deny invitations         |          filter,update_three,update          |      member_pending_request,project,        |                        100 %                 
                                                                                                          continue_or_not                                 logins,student
 
                  student                   |                Create a project              |     filter,random.randint,select,update      |       member_pending_request,logins,        |                        100 %                 
                                                                                                       insert,continue_or_not                      project,project_data,student

                  student                   |                     Exit                     |              continue_or_not                 |                   student                   |                        100 %                   

                  member                    |     See the details of the project status    |           display,continue_or_not            |               project,member                |                        100 %                   

                  member                    |      See the details of the project data     |           display,continue_or_not            |             project_data,member             |                        100 %                  

                  member                    |     See the details of the proposal data     |           display,continue_or_not            |             proposal_data,member            |                        100 %                  

                  member                    |                     Exit                     |             continue_or_not                  |                   member                    |                        100 %                   

                  lead                      |     See the details of the project status    |           display,continue_or_not            |                project,lead                 |                        100 %                   

                  lead                      |      See the details of the project data     |           display,continue_or_not            |              project_data,lead              |                        100 %                  

                  lead                      |     See the details of the proposal data     |           display,continue_or_not            |             proposal_data,lead              |                        100 %                  

                  lead                      |           Modify the project title           |           update,continue_or_not             |          project,project_data,lead          |                        100 %                 

                  lead                      |   Modify and/or submit the project proposal  |        update,insert,continue_or_not         |   project,project_data,proposal_data,lead   |                        100 %                 

                  lead                      |   Modify and/or submit the  project report   |            update,continue_or_not            |          project,project_data,lead          |                        100 %              

                  lead                      |         Find all non-member students         |            display_list,all_name             |               login,User,lead               |                        100 %              
                                                                                                           continue_or_not                    

                  lead                      |             Find all faculties               |            display_list,all_name             |               login,User,lead               |                        100 %              
                                                                                                          continue_or_not                     

                  lead                      |       Send invitational messages to          |           filter,aggregate,insert            |               project,logins                |                        100 %              
                                                          potential members                               continue_or_not                           member_pending_request,lead

                  lead                      |       Send invitational messages to          |           filter,aggregate,insert            |               project,logins                |                        100 %              
                                                          potential advisors                              continue_or_not                          advisor_pending_request,lead

                  lead                      |                     Exit                     |             continue_or_not                  |                   lead                      |                        100 %                   

                faculty                     |       See details of project status          |         format_solo,continue_or_not          |              project,faculty                |                        100 %                   

                faculty                     |        See details of project data           |         format_solo,continue_or_not          |            project_data,faculty             |                        100 %                   

                faculty                     |        See details of proposal data          |         format_solo,continue_or_not          |           proposal_data,faculty             |                        100 %                   

                faculty                     |                See invitations               |          filter,select,display_list          |       advisor_pending_request,faculty       |                        100 %                 
                                                                                                          continue_or_not        

                faculty                     |           Accept or deny invitations         |          filter,update_three,update          |      advisor_pending_request,project,       |                        100 %                 
                                                                                                          continue_or_not                                 logins,faculty
 
                faculty                     |          Evaluate project proposals          |    filter,format_solo,update_two,update      |     proposal_data,project,project_data,     |                        100 %                   
                                                                                                          continue_or_not                                   faculty

                faculty                     |                     Exit                     |             continue_or_not                  |                 faculty                     |                        100 %                   

                advisor                     |       See details of project status          |         format_solo,continue_or_not          |              project,advisor                |                        100 %                   

                advisor                     |        See details of project data           |         format_solo,continue_or_not          |            project_data,advisor             |                        100 %                   

                advisor                     |        See details of proposal data          |         format_solo,continue_or_not          |           proposal_data,advisor             |                        100 %                   

                advisor                     |       See the details of the project         |       display,filter,continue_or_not         |              project,advisor                |                        100 %                   
                                                     status serving as an advisor

                advisor                     |       See the details of the project         |       display,filter,continue_or_not         |            project_data,advisor             |                        100 %                   
                                                      data serving as an advisor

                advisor                     |      See the details of the proposal         |       display,filter,continue_or_not         |           proposal_data,advisor             |                        100 %                   
                                                      data serving as an advisor

                advisor                     |          Evaluate project proposals          |    filter,format_solo,update_two,update      |     proposal_data,project,project_data,     |                        100 %                   
                                                                                                          continue_or_not                                   advisor

                advisor                     |       Approve or deny a final project        |      print_dict,update,continue_or_not       |         project_data,project,advisor        |                        100 %                   
                                                           report approval

---