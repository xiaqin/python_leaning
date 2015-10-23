__author__ = 'xiaqin'

welcome = '''
    Welcome to the my system...
    1. login the system
    2. cancel and quit
'''

thanks = '''
    Thanks for using our system
    see you later
'''

info = '''
Please choose your sub items:
    1. check your count
    2. modify password
    3. enter services
    4. quit
'''

err_info = '''
    your user name or password is not correct
    times to try:%d
'''

login = False

while True :
    user_input = raw_input(welcome)
    if user_input.isdigit() == False :
        print "input is not correct"
    else:
        break
user_input = int(user_input)
if user_input == 1:
    count = 0
    while count<3:
        name = raw_input("please input your name:")
        passw = raw_input("please input your password:")
        if name=="test" and passw == "123":
            login = True
            service_choose = int(raw_input(info))
            while (service_choose >=1 and service_choose != 4):
                if service_choose == 1:
                    print("now checking your count")
                elif service_choose == 2:
                    print("modifying your passwd")
                elif service_choose == 3:
                    print("now entering sub services")
                else:
                    print("not correct")
                service_choose = int(raw_input(info))
            if service_choose == 4:
                print(thanks)
                break
        else:
            print err_info%(2-count)
            count += 1
    else:
        print(thanks)
else:
    print(thanks)