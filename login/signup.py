#Python sign up and login script created by Bryscar
username = input("Please create a username: \n")
password = input("Please create a password: \n")
confpass = input("Confirm password: \n")
if password != confpass:
    print("Passwords don't match, please try again. \n")
else:
    print("Successfully created account! You can now login.\n")
    attemptu = input("Username: \n")
    attemptp = input("Password: \n")
    
    if attemptu == username and attemptp == password:
        print("Welcome, " + username + "!")
        genre=[]
        print("What are your preferred Genres the Type Done...\n")
        while True:
            gen = input(">>> ").lower()
            if gen == "done":
                print("Your List of preferred movies include: \n", genre)
                break
            else:
                genre.append(gen)
        
    else:
        print("Wrong username/password, please try again.")
    
    