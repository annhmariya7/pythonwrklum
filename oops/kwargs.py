def dispaly_emp(**kwargs):
    print(kwargs)

dispaly_emp(name="ebin",department="hr",salary=53664)

# **kwargs => dictionary format
# keywordarguments

def dispaly_emp(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("department"))

dispaly_emp(name="ebin",department="hr",salary=53664)

# create a function display student and print student name and course
# display_student(name="ravi",course="django")

def display_student(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("course"))

display_student(name="ravi",course="django",rolno=1000,gender="male")