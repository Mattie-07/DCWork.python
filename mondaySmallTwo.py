# 2. Nested dictionaries
# Given the following dictionary:

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

ramit = {
    'name' : 'Ramit',
    'email': 'ramit@gmail.com',
    'interests' : ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'Jasmine@yahoo.com',
            'interests' : ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'Jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}


email = ramit["email"]
emailName = email
print(f"Ramti's email is {email}")

interest = ramit["interests"][0]
print(f"Ramit's first interest is {interest}")


# friend = ramit["friends"]
# jazEmail = friend[0]
# jaz = jazEmail["email"]
# print(jaz)


friend = ramit["friends"][0]["email"]
print(f"Jasmine's email is {friend}")


janInterest = ramit["friends"][1]["interests"][0]
print(f"Jasmine's first interest is {janInterest}")

# jan =  friend[1]
# moviesJan = jan["interests"][0]
# print(moviesJan)


# Write a python expression that gets the email address of Ramit.
# Write a python expression that gets the first of Ramit's interests.
# Write a python expression that gets the email address of Jasmine.
# Write a python expression that gets the second of Jan's two interests