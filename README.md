# RLXMOOC Template Course

This repository is a template course for the RLXMOOC grading platform.

## How to use it?
### 1. Create an empty github repository for your course
This empty repository is going to contain all the laboratories 
and classes of the course in jupyter notebooks

### 2. Clone this repository in your computer
You can clone this repository with a

    git clone https://github.com/rramosp/rlxmooc.git

* **Notice that** it is important to have this repository in a private 
location because this repository contains the graders 
that will grade your students submissions

### 3. Set up the [init.py file](teacher/init.py)
In the [teacher/init.py file](teacher/init.py) you have 
to set 
* The course id
    * In the `course_id` variable you have to set your
    personalized course id
    * **For example**  20201.test
* Your repository name
    * In the `github_repo` variable you have to set the 
    `github_username/repo_name` data
    * **For example** `egutierrezc93/20201.test`
* The RLXMOOC grader platform endpoint url
    * In the `endpoint` variable you have to set the
    endpoint url that the RLXMOOC administrator give 
    to you 

### 4. Set up your course labs evaluation methodology
The [teacher/course_spec.json file](teacher/course_spec.json) 
is a sample file for your course labs evaluation and
naming customization
* Using the same structure you could add as many labs 
as you want

You must also set the course id with the same course id
set in the [teacher/init.py file](teacher/init.py)
* **For example**  20201.test

### 5. Create your course labs and content
#### Labs

To create the labs there is the [teacher/LAB 01 - SUBMISSION
EXAMPLE.ipynb](teacher/LAB%2001%20-%20SUBMISSION%20EXAMPLE.ipynb)
which is a file that is aimed to guide you through the creation
of your Labs.

##### Labels
Here is important to notice that there are labels in some
of the notebook cells, this labels have different functions

* **\## TEACHER**: this label indicates that this notebook
cell and its output is only visible in the teacher notebook, and will be
deleted for the student version of the notebook
* **\## TEACHER DEFINEGRADER:** this label indicates that
this cell is where the teacher defines the grader function,
this cell and its output will be deleted for the student version of the
notebook
* **\## TEACHER SETGRADER:** this label indicates that this
cell is the one that set the grader in the RLXMOOC platform.
This cell and its output will be deleted for the student version of the
notebook
* **\## KEEPOUTPUT:** this label indicates that the cell content
will be deleted but the output of the cell will remain in the
student version of the notebook

### 6. Deploy your course
To deploy your course there is the [teacher/00 - DEPLOY 
COURSE.ipynb](teacher/00%20-%20DEPLOY%20COURSE.ipynb)
which is a file that is aimed to guide you through the
deploy of your course in RLXMOOC platform.

This notebook is divided by sessions,

* **1.A Create teacher and student users:** in this
session the users of the RLXMOOC platform are created
and logged in.
* **1.B Setup course and graders in server:** in this
session you deploy the course how it is set in the 
[teacher/course_spec.json file](teacher/course_spec.json)
and in this session also the teacher graders are
deployed to the server automatically executing all the
cells with the `## TEACHER SETGRADER` label
* **1.C Create course session and enrol test student:**
in this session you create the course session and enrol
your students
* **1.D Recompute grades for all students:** It's
ocassionally required to recompute all the student
grades.
* **1.E Reinvite students if required:** in this session
you send an email invitation to the students enrolled in
the course
* **1.F setup student notebooks and repo:** in this
session the student repository is created with the
notebooks of the teacher and is sent to the 
[student/github directory](student/github)

### 7. Update the README.md file
we highly recommend that you update your 
[teacher/README.md](teacher/README.md) 
file to guide your students through the course

### 8. Upload your students repository
Now that you have created and deployed your course,
is time to upload the students repository, you can
do it by a commit and a push to the empty repository
you created in the first step

    cd student/github/
    git init
    git commit -m "first commit"
    git remote add origin https://github.com/**github_username**/**repo_name**.git
    git push -u origin master

Finally share the github repository to your students

### 9. Repeat the steps 4 to 8 for any update
For any update please repeat the 4 to 8 steps