class jobApplication:
    appilications=[]
    def registration(slef):
        appilication={}
        while True:

    
            fname=input("enter your first name")
          

            if len(fname)==4:
             
                appilication["fname"]=fname
                break
            else:
                print(f"{fname} is lee then 3 char")
        while True:
            Sname=input('enter your second name')
            if len(Sname)==4:
                appilication["sname"]=Sname
                break
            else:
                print(f"{Sname} is lee then 3 char")

        while True:

         father_name = input("Enter your father's name: ")
         if len(father_name) >= 3:

             
            appilication["fathername"] = father_name
            break
         else:
             print(f"{father_name} is less than 3 characters. Try again.")
        while True:
            number = input("Enter your phone number: ")
            if number.isdigit() and len(number) == 10:
              appilication["phone"] = number
              break
            else:
                 print(f"{number} is invalid. Enter a 10-digit phone number.")
        while True:
            resume = input("Enter your resume path: ")
            if len(resume) >= 3:
                appilication["resume"]=resume
                break
            else:
                print("Resume path must be at least 3 characters.")
        


       
         
             
        appilication["jobs"]=None
        jobApplication.appilications.append(appilication)
        print("✅ User registered successfully!\n")
    def login(self):
        phone=input("enter your phone number")
        for user in jobApplication.appilications:
            if user["phone"]==phone:
                    
                print(f"✅ Welcome {user['fname']}! You are now logged in.\n")
                self.apply_job(user)
                return
        print("❌ Login failed. Phone number not found.\n")
    def apply_job(self,user):
        print("📋 Available Jobs:")
        jobs = ["React Developer", "Python Developer", "Frontend Engineer", "Node.js Developer"]
        for i ,job in enumerate(jobs,start=1):
            print(f"{i}:{job}")
        choice = input("Select a job number to apply: ")
        if choice.isdigit() and 1 <= int(choice) <= len(jobs):
            selected_job = jobs[int(choice) - 1]
            user["job_applied"] = selected_job
            print(f"✅ You have successfully applied for '{selected_job}'.\n")
        else:
             print("❌ Invalid job selection.\n")
    def AllUsers(self):
        if not jobApplication.appilications:
              print("No users found.")
        else:

           for i, user in enumerate(jobApplication.appilications, start=1):

                print(f"\nUser {i}:")
                for key, value in user.items():
                    print(f"{key}: {value}")


    
obj=jobApplication()
while True:
     
    print("\n=== Application Menu ===")
    print("1. Register New User")
    print("2. Login & Apply for Job")
    print("3. View All Users")
    print("4. Exit")
    choice=input("enter your choice")
    if choice=="1":
         obj.registration()
    elif choice=="2":
        obj.login()
    elif choice=="3":
        obj.AllUsers()
    elif choice=="4":
        print("Exiting... Thank you!")
      
        break;
    else:
         print("❌ Invalid choice. Try again.")



       
    
   







      



    