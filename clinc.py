import sqlite3 as sql1
import datetime as dt
from google.oauth2 import service_account
from google.cloud import bigquery


# bigquery
cre = service_account.Credentials.from_service_account_file('C:/Users/ronak/PycharmProjects/Project/snappy.json')
proj = "snappy-gantry-319622"
tbl = 'WalkInClinc'
sql = bigquery.Client(credentials=cre, project=proj)

# sqlite
connection = sql1.connect("WalkInClinic.db")

dbP, dbm, dba = ([] for i in range(3))


class inserting_data:
    # for patients
    def insertp(*args, **kwargs):
        count = len(dbP) - 1
        table = sql.get_table("{}.{}.{}".format(proj, tbl, 'Patients'))
        rows_to_insert = [{u"FName": dbP[count]["name"],
                           u"Condition": dbP[count]["condition"],
                           u"Medication": dbP[count]["medication"],
                           u"DOB": str(dbP[count]["Birth"]),
                           u"Weight": str(dbP[count]["weight"]),
                           u"CurrentDate": str(dbP[count]["Date"]),
                           }]
        errors = sql.insert_rows_json(table, rows_to_insert)
        if not errors:
            print("You Can Visit any Time After 15-30 mins")
        else:
            print(errors == [])

    # for medical staff
    def insertM(*args, **kwargs):
        count = len(dbm) - 1
        table = sql.get_table("{}.{}.{}".format(proj, tbl, 'Staff'))
        # insert Data for staff
        rows_to_insert = [{u"Title": dbm[count]["title"],
                           u"Name": dbm[count]["name"],
                           u"phone": dbm[count]["phone"],
                           u"Role": dbm[count]["role"],
                           u"Password": dbm[count]["pass"],
                           }]
        errors = sql.insert_rows_json(table, rows_to_insert)
        if not errors:
            print("Done")
        else:
            print(errors == [])


class loginSys:
    def login(uname, password):
        # database query
        querym = sql.query("""select Name , password,Role from `snappy-gantry-319622.WalkInClinc.Staff`""")
        for passchek in querym:
            if passchek['Name'] == uname and passchek['password'] == password:
                if passchek['Role'] == "Admin":
                    print("Hello Admin")
                    achoice = input("""1 create Doctor Profile
2 for Delete Doctor Profile
3 Create Receptionists Profile
4 delete Receptionists Profile""")
                    if achoice == "1":
                        book.Doctpro()
                    elif achoice == "2":
                        dname = input("Enter Doctor Name To delete from the record")
                        dele = sql.query("""
delete from `snappy-gantry-319622.WalkInClinc.Staff` where Role = 'Doctor' and Name = '{}'""".format(dname))
                        dele.result()
                    elif achoice == "3":
                        book.Recpe()
                    elif achoice == "4":
                        rname = input("Enter Receptionists Name To delete from the record")
                        dele = sql.query("""
                        delete from `snappy-gantry-319622.WalkInClinc.Staff` where Role = 'Receptionist' and Name = '{}'""".format(
                            rname))
                        dele.result()
                        pass
                elif passchek['Role'] == "Doctor":
                    print('Doctor')
                else:
                    print("Receptionist")


class book:
    def appointment(**kwargs):
        pname = input("Enter the name of patients:")
        pcon = input("""your past medical 
condition(Past 2 week):""")
        pmed = input("past medication your were taking:")
        pdobW = input("""Date of birth and Weight(in kilograms) of the patient
for example(YYYY/MM/DD,Weight):""")
        x = pdobW.split(",")
        curBook = dt.datetime.utcnow()

        dic = {"name": pname, "condition": pcon, "medication": pmed, "Birth": x[0], "weight": x[1],
               "Date": curBook.strftime("%Y/%m/%d %H:%M")}
        dbP.append(dic)
        inserting_data.insertp(1)

    def Doctpro(**kwargs):
        Dtile = input("insert title for doctor")
        Dname = input("enter name of the doctor")
        Dphone = input("enter phone number example'12344'")
        DRole = "Doctor"
        RRole = "Receptionist"
        Dpass = input("Create password for the the doctor")
        dic = {"title": Dtile, "name": Dname, "phone": Dphone, "role": DRole, "pass": Dpass}
        dbm.append(dic)
        inserting_data.insertM(1)

    def Recpe(**kwargs):
        Dtile = input("insert title for Receptionists")
        Dname = input("enter name of the Receptionists")
        Dphone = input("enter phone number example'12344'")
        RRole = "Receptionist"
        Dpass = input("Create password for the the Receptionists")
        dic = {"title": Dtile, "name": Dname, "phone": Dphone, "role": RRole, "pass": Dpass}
        dbm.append(dic)
        inserting_data.insertM(1)
