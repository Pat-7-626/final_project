# Evaluation Step

---

***The Step***

* A lead student submits a project proposal
* a project proposal is evaluated by a group of faculties
    - If disapproved: inform a lead student about disapproval from faculties
    - If approved: inform a lead student about approval from faculties

---

#### A lead student user submits a project proposal
- input a project proposal (a PDF link)
- call a function that allows to update a value associated with a key in a Project_data table; update Proposal and Status

---

#### A faculty user evaluates a project proposal
- display a project proposal from Project_data table (a PDF link)
- if disapproved; disapproved += 1
- if approved; approved += 1 

Note: disapproved and approved are collected in Proposal class that is going to be created

---

#### When every faculty users has evaluated a certain project proposal
- if disapproved < approved; a project proposal approved; call a function that allows to update a value associated with a key in a Project_data table; update Status
- if disapproved >= approved; a project proposal disapproved; call a function that allows to update a value associated with a key in a Project_data table; update Status

---

#### edit after consoling with the teacher
change from making every faculty evaluate to only 3 of each project