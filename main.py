import clinc as c
# from google.oauth2 import service_account
# from google.cloud import bigquery
#
# cre = service_account.Credentials.from_service_account_file('C:/Users/ronak/PycharmProjects/Project/snappy.json')
# proj = "snappy-gantry-319622"
# sql = bigquery.Client(credentials=cre, project=proj)
# ans = sql.query("""select * from `snappy-gantry-319622.WalkInClinc.Patients`""")

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



