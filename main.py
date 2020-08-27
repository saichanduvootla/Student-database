from Operations import DBHelper

def main():
    db = DBHelper()

    while  True:
        print('******* WELCOME ***********')
        print()
        print('enter 1 to insert student:')
        print('enter 2 to display student:')
        print('enter 3 to delete student:')
        print('enter 4 to update student:')
        print("enter 5 to exit database:")
        print()
        try:
            choice = int(input())
            if (choice ==1):
                id = int(input('enter the new student id :'))
                name = input('enter the new student name :')
                phn = input('enter new student phone :')
                print()
                db.insert_data(id , name, phn)
                
            elif choice == 2:
                db.fetch_data()
            elif choice == 3:
                del_id = int(input('enter the student Id which you want to delete :'))
                print()
                db.delete_data(del_id)
            elif choice == 4:
                id = int(input('enter student id to update:'))
                name = input('enter the new student name:')
                phn = input('enter new student phone:')
                print()
                db.update_data(id , name, phn)
                
            elif choice == 5:
                break
            else:
                print('Invalid input !! Try again ')
                print()
        except Exception as e:
            print(e)
            print('Invalid input !! Try again')
            print()
if __name__ =="__main__":
    main()
            
