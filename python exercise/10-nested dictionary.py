student = {
    "name" : "Prashanth",
    "class":8,
    "course":"cse",
    "age":18
}
print(student)
print(student["name"])

school = {
    "classes" : 8,
    "total number of students" : 55,
    "average age of the students" : 18,
    "marks" :{
        "highest in python " :58,
        "highest in english " : 58,
        "highest in kannada" : 100
    }
}
print(school)
print(school["marks"]["highest in kannada"])
print(school["total number of students"])

school["course"] = "cse"
print(school)

school["marks"]["mathematics"] = 55
print(school)
print(school["marks"]["mathematics"])
school["classes"] = 12
print(school)
del school["classes"]
print(school)



college ={
    "student 1" :{
        "name" : "prashanth",
        "branch" : "Cse",
        "marks" :{
            "english" : 58,
            "mathematics" : 55,
            "computer" : 66,
        }
    },
    "student 2" : {
        "name" : "rahul",
        "branch" : "EEE",
        "marks" :{
            "english" : 85,
            "mathematics" : 66,
            "computer" : 63
        }
    },
    "student 3" : {
        "name" : "rishi",
        "Branch" : "ECE",
        "marks" : {
            "english" : 28,
            "mathematics" : 35,
            "Computer" : 50
        }
    }
}
print(college)

print(college["student 1"]["marks"])