import clinc as c

while True:
    main = input("""
    Welcome to the Walk in Clinic
    Here you can register your appointment
    NOTE: For appoint Register Your account.
1 Login 
2 Book Appointment 
""")
    # Doctor and staff.
    if int(main) == 1:
        UName = input("Enter your UserName:")
        Upass = input("Enter your Password:")
        c.loginSys.login(UName, Upass)

    # Booking
    else:
        c.book.appointment()



