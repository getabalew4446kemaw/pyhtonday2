my_description={"firstname":"Getabalew",
                "midlename":"Kemaw",
                "age":20,
                "lastname":"amare",
                "contact_us":{
                    "phonenumber":944463198,
                    "email":"getabalewkemaw@gmail.com"
                },
                "strit":"A.A_ataye main_road",
                "is_atudent":True,
                "city":"Debreberhan,Ethiopia",
                "campus_time":"secound year",
                "department":"software enginering",
                "skill":["HTML","css","javascript","python_beginner"],
                "sibling":("jhon"," aster","tesfa","helen"),
                "my_strength":["punctual"," professional",'ethical','hardworker'],
                "taken_course":{"python","discretemaths","database","fundamental of sw enginerring"}


}
# for keys,values in my_description.items():
#     print(f"{keys}:{values} ,end=" " ")
# print('Getabalew' in my_description)
# print(my_description.items())
# for keys in my_description:

#     if keys=="skill":
#         for i in my_description["skill"]:
#             print(type(i))
# print(len(my_description))


for keys in my_description:
    if keys=="skill":
        for i in my_description["skill"]:
            # print)
            print(i,type(i))



# my_description["skill"].append("react")
# my_description["skill"].append("numpy")
# print(my_description["skill"])

# for i in my_description:
#     print(i.keys())
# for j in my_description:
#     print(j.values())