import getpass database =
{"clcoding": "976729", "pythonclcoding": "2502"}
username = input ("Enter Your Username : ")
password = getpass getpass("Enter Your Password : ")
for i in database. keys():|
    if username == i:
       while password != database.get(i):
           password = getpass.getpass"Enter Your Password Again : ")
       break
print ("Verified")
