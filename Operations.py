import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user = 'root',
                                     password='chandu123',
                                     database = 'studentdb')
        query = 'create table if not exists student_info(stdid int  primary key,Name varchar(50) , phone varchar(13))'
        cur = self.con.cursor()
        cur.execute(query)

    def insert_data(self,stdid,Name,phone):
        query =  "insert into student_info values ({},'{}','{}')".format(stdid , Name , phone)
        cur= self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('The details are successfully saved in the database')
        print()


    def fetch_data(self):
        query = 'select * from student_info'
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("student id:", row[0])
            print("student Name", row[1])
            print("student phone", row[2])
            print()
            print()

    def delete_data(self, stdid):
        query ='delete from student_info where stdid= {}'.format(stdid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def update_data(self , stdid, Name , phone):
        query = 'update student_info set Name ="{}" ,phone = "{}"  where stdid={} '.format(Name , phone , stdid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()  
        
