
students = {
    "Rahul": {"age": 20, "marks": 85},
    "Priya": {"age": 21, "marks": 90},
    "Rohan": {"age": 19, "marks": 78}
}

students["Amit"] = {"age": 22, "marks": 88}
students["Rahul"]["marks"] = 95
del students["Rohan"]
if "Priya" in students:
    print("Priya exists in dictionary")
else:
    print("Priya not found")