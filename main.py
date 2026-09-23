# Python + Streamlit Project
# Motive of this project is to revise important pythons concepts
# University Management System


import streamlit as st

# config the main app page
st.set_page_config(
    page_title="University Management System",
    page_icon=":mortar_board:",
    layout="wide"
)

st.title("University Management System")

# create a empty list of colleges
if "colleges" not in st.session_state:
    st.session_state.colleges = []

menu_choice = st.sidebar.radio(
    "SELECT AN OPTION",
    (
        "Create College",
        "Add Student",
        "Add Teacher",
        "Display Students",
        "Display Teachers",
        "List of college"
    )
)

# college class is storing college name and students and teachers list


class college:
    def __init__(self, cname):
        self.cname = cname
        self.students = []
        self.teachers = []

    def add_student(self, s):
        self.students.append(s)

    def add_teacher(self, t):
        self.teachers.append(t)


class person:
    def __init__(self, name, branch):
        self.branch = branch
        self.name = name


class student(person):
    def __init__(self, roll, sname, branch):
        self.rollno = roll
        super().__init__(sname, branch)  # call parent constructor function and store sname


class teacher(person):
    def __init__(self, subject, tname, branch):
        self.subject = subject
        super().__init__(tname, branch)


# Based upon college name,college class object is find
def find_college(cname):
    for c in st.session_state.colleges:
        if c.cname == cname:
            return c
    return None


if menu_choice == "Create College":
    cname = st.text_input("Enter College Name")
    if st.button("CREATE COLLEGE"):
        clg_obj = college(cname)  # create a college object
        # storring a college class object in college list
        st.session_state.colleges.append(clg_obj)
        st.success(f"College '{cname}' created successfully!")


elif menu_choice == "Add Student":
    if not st.session_state.colleges:
        st.info("Please add the college first")
    else:
        clgname = st.selectbox(
            "Choose college", [c.cname for c in st.session_state.colleges])
        roll = st.number_input("Enter  Your rollnumber",
                               min_value=1, max_value=100)
        sname = st.text_input("Enter student name")
        branch = st.text_input("Enter your Branch")
        if st.button("ADD STUDENT"):
            if not (roll and sname and clgname and branch):
                st.error("Please fill the reamining details")
            else:
                # find the college object based upon college name
                clg_ob = find_college(clgname)
                # created student object
                stu_obj = student(roll, sname, branch)
                clg_ob.add_student(stu_obj)
                st.success("Student added successfully")

elif menu_choice == "Add Teacher":
    if not st.session_state.colleges:
        st.info("Please add the college first")
    else:
        clgname = st.selectbox(
            "Choose college", [c.cname for c in st.session_state.colleges])
        subject = st.text_input("Enter Your subject")
        tname = st.text_input("Enter teacher name")
        branch = st.text_input("Enter your Branch")
        if st.button("ADD TEACHER"):
            if not (subject and tname and clgname and branch):
                st.error("Please fill the reamining details")
            else:
                # find the college object based upon college name
                clg_ob = find_college(clgname)
                # created teacher object
                teacher_obj = teacher(subject, tname, branch)
                clg_ob.add_teacher(teacher_obj)
                st.success("Teacher added successfully")

elif menu_choice == "Display Students":
    if not st.session_state.colleges:
        st.info("Please add the college first")
    else:
        clgname = st.selectbox(
            "Choose college", [c.cname for c in st.session_state.colleges])
        clg_obj = find_college(clgname)
        st.subheader(f"List of Students : {clgname}")
        if clg_obj.students:
            for i, s in enumerate(clg_obj.students, 1):
                st.write(i, ":", s.name)
        else:
            st.warning("No student found")

elif menu_choice == "Display Teachers":
    if not st.session_state.colleges:
        st.info("Please add the college first")
    else:
        clgname = st.selectbox(
            "Choose college", [c.cname for c in st.session_state.colleges])
        clg_obj = find_college(clgname)
        st.subheader(f"List of Teachers : {clgname}")
        if clg_obj.teachers:
            for i, t in enumerate(clg_obj.teachers, 1):
                st.write(i, ":", t.name)
        else:
            st.warning("No Teacher found")

elif menu_choice == "List of college":
    st.subheader("List of college")
    if not st.session_state.colleges:
        st.info("Please add the college first")
    else:
        for i, c in enumerate(st.session_state.colleges, 1):
            st.write(f"{i} : {c.cname}")
