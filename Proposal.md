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
- call a function that allows to update a value associated with a key in Project and Project_data table; update Proposal and Status
- call a function that allows to update a dictionary in Proposal_data table

---

#### A faculty user evaluates a project proposal
- display a project proposal from Project_data table (a PDF link)
- if disapproved; pass
- if approved; number += 1 
- call a function that allows to update a value associated with a key in Proposal_data table

Note: disapproved and approved are collected in Proposal_data table

---

#### When every faculty users has evaluated a certain project proposal
- if number >= 2; a project proposal approved; call a function that allows to update a value associated with a key in Project and Project_data table; update Status, in a Proposal_data table; update result
- else; a project proposal disapproved; call a function that allows to update a value associated with a key in Project and Project_data table; update Status, in a Proposal_data table; update result

---