import string
import random
def reg_user():
    users_container = []
    def create_account():
        def new_user():
            #Enter user data, Collect firstname, lastname and email
            firstname = input("Enter your First Name Here: \n")
            lastname = input("Enter your Last Name Here: \n")
            email = input("Enter your Email Here: \n")
            user_id = ''.join([random.choice(string.ascii_letters + string.digits) for x in range(4)])

            #random password generation
            random_pword = ''.join([random.choice(string.ascii_letters + string.digits) for x in range(5)])
            password = firstname[0:2] + lastname[-2:] + random_pword
            print("Your password is " + password)

            #If user rejects generated password:
            new_pword = input("Are you satisfied with this password? yes/no?  \n").lower()
            if new_pword == "no":
                new_password = input("Enter your password here. Password should be more than 7 characters: \n")
                while len(new_password) < 7:
                    new_password = input("Your password should be more than seven characters. Enter your password again: \n")
                else:
                    print("Password saved!")
            elif new_pword == "yes":
                print("Password saved!")
            else:
                print()

            #storing User details
            user_details = {"id": user_id, "First_Name": firstname, "Last_Name": lastname, "Email": email, "Password": password}
            if new_pword == "no":
                user_details["Password"] = new_password
            users_container.append(user_details)

        new_user()
        #add new user account
        new_account = input("Do you want to register a new user? yes/no? \n").lower()
        if new_account == "yes":
            create_account()

        elif new_account == "no":
            print("Thanks for signing up!")
        else:
            print("")
        print()

    create_account()
    #print user list here
    print(users_container)


reg_user()