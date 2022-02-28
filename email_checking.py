email = input("enter email to check wheather its correct or not::")
k,j,d = 0,0,1
if(len(email)>6):
    if email[0].isalpha():
        if ("@" in email) and (email.count('@') == 1):
            if(email[-3] == '.') ^ (email[-4] == '.'):
                for i in email:
                    if(i ==' '):
                        k = 1
                    elif (i.isalpha):
                        if (i==i.isupper):
                            j = 1
                    elif(i.isdigit):
                        continue
                    elif (i == '_'or i == '.' or i == '@'):
                        continue
                    else:
                        d = 0
                if(k == 1):
                    print("wrong email 5")
                elif(j == 1):
                    print("wrong email 6")
                elif(d == 0):
                    print("wrong email 7")
                else:
                    print("right email")

            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")
else:
    print("wrong email 1")