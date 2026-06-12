set = {"python", "c++", "java", "python","java"}

print(set)


tuple = ("bhopal", "indore", "jaipur", "mumbai", "pune")

occur = 0

for i in range( len(tuple)):
    if tuple(i) == "indore":
        occure += 1
        print("city occr at index :",i, "and occure times is : ", occur)
