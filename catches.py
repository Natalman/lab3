import sqlite3
def main():
    db = sqlite3.connect('Catches.db')

    nat = db.cursor()

    nat.execute('create table catches( Chainsaw_Juggling_Record_Holder text, Country text, Number_of_catches int)')
    with db:
        nat.execute('insert into catches values("Ian Stewart", "Canada", 94 )')
        nat.execute('insert into catches values("Aaron Gregg", "Canada", 88)')
        nat.execute('insert into catches values("Chad Taylor", "USA", 78)')


    for row in nat.execute('select * from catches'):
        print (row)

    print ('''
                1. to print table
                2. to add row
                3. to update row
                4. to delete row
                5. quit''')
    choice = input("Enter a choice")

    if choice =='1':
        for row in nat.execute('select * from catches'):
            print (row)

    elif choice =='2':
        Holder = input("Enter the holder name")
        Country = input("Enter the Country")
        CatcheNum = int(input("Enter the number of catches"))

        nat.execute('insert into catches values(?,?,?)', (Holder, Country, CatcheNum))
        db.commit()

    with db:
        nat.execute('drop table catches')
    db.close
main()
