import sqlite3
def main():
    db = sqlite3.connect('Catches.db')

    nat = db.cursor()

    # Create table
    nat.execute('create table catches(ID INTEGER PRIMARY KEY   AUTOINCREMENT , Holder text, Country text, Number_of_catches int)')
    with db:
        # insert data into the table
        nat.execute('insert into catches (Holder, Country, Number_of_catches ) values("Ian Stewart", "Canada", 94 )')
        nat.execute('insert into catches (Holder, Country, Number_of_catches ) values("Aaron Gregg", "Canada", 88)')
        nat.execute('insert into catches (Holder, Country, Number_of_catches ) values("Chad Taylor", "USA", 78)')

    # Printing the table
    for row in nat.execute('select * from catches'):
        print (row)

    loop = True
    while loop:
        menu ()
        choice = input("Enter a choice")
        if choice =='1': # printing the table 
            for row in nat.execute('select * from catches'):
                print (row)

        elif choice =='2': # Add a row to the table
            Holder = input("Enter the holder name")
            Country = input("Enter the Country")
            CatcheNum = validation("Enter the number of catches")

            nat.execute('insert into catches (Holder, Country, Number_of_catches ) values(?,?,?)', (Holder, Country, CatcheNum))
            db.commit()

        elif choice == '3': # Printing a record
            IdUser = validation("Enter the ID of the holder you seek:")
            for row in nat.execute('select * from catches WHERE ID = ? ', (IdUser,)):
                print (row)

        elif choice == '4': # updating the holder name
            IdUser = validation("Enter the ID of the holder you seek:")
            newHolder = input("Enter the new holder")
            for row in nat.execute('UPDATE catches SET Holder = ? where ID = ?', (newHolder, IdUser,)):
                print("The row has been updated")

        elif choice == '5': # updating the country
            IdUser = validation ("Enter the ID of the holder you seek:")
            newCountry = input("Enter the new country")
            for row in nat.execute('UPDATE catches SET Country = ? where ID = ?', (newCountry, IdUser,)):
                print("The row has been updated")

        elif choice == '6': # updating the number of catches
            IdUser = validation ("Enter the ID of the holder you seek:")
            newCatches = validation ("Enter the new catches")
            for row in nat.execute('UPDATE catches SET Number_of_catches = ? where ID = ?', (newCatches, IdUser,)):
                print("The row has been updated")

        elif choice == '7': # deleting a row
            IdUser = validation("Enter the ID of the holder you seek:")
            for row in nat.execute('DELETE from catches where ID = ?', (IdUser,)):
                print (" The row has been deleted")

        elif choice =='8': # closing  out the app
            break

    with db:
        nat.execute('drop table catches')
    db.close


def menu (): # function to load the menu
    print ('''
                1. to print table
                2. to add row
                3. to search for a record
                4. to update holder
                5. to update Country
                6. to update catches number
                7. to delete row
                8. quit''')

# function to check the user input
def validation (message):# copy from http://www.101computing.net/number-only/
    while True:
        try:
            id = int(input(message))
        except ValueError:
            print('Please enter an integer number')
            continue
        else:
            return id
            break

main()
