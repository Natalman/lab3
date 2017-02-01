from sqlalchemy import create_engine

def main():

    engine = create_engine('sqlite:///catches2db', echo=True)
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    from sqlalchemy import Column, Integer, String

    class Catches(Base):

        __tablename__ = 'catches'

        id = Column(Integer, primary_key=True)
        Holder = Column (String)
        Country = Column (String)
        NumOfCatches = Column (Integer)

        def __repr__(self):
            return 'catches: id = {} Holder = {} Country = {} NumOfCatches = {}'.format(self.id, self.Holder, self.Country, self.NumOfCatches)

    Base.metadata.create_all(engine)

    catches1 = Catches (Holder = 'Ian Stewart', Country = 'Canada', NumOfCatches = 94)
    catches2 = Catches (Holder = 'Aaron Gregg', Country = 'Canada', NumOfCatches = 88)
    catches3 = Catches (Holder = 'Chad Taylor', Country = 'USA', NumOfCatches = 78)

    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker (bind = engine)

    save_session = Session()

    save_session.add_all([ catches1, catches2, catches3 ])
    print (save_session.new)
    print (save_session.dirty)

    save_session.commit()
    save_session.close()


    loop = True

    while loop:
        menu()
        choice = input("Enter your choice:")
        search_session = Session()
        delete_session = Session()

        if choice == '1':
            for catches in search_session.query(Catches):
                print(catches)


        if choice == '2':
            holder = input("Enter the name of the holder: ")
            country = input("Enter the country of the holder: ")
            CatchesNum = int(input("Enter the number of catches"))


            newCatches = Catches(Holder = holder, Country = country, NumOfCatches = CatchesNum)
            save_session.add(newCatches)
            save_session.commit()
            print("New catches has been added")


        if choice == '3':
            UserID = int(input("Enter the Id of the user you seek:"))
            print (search_session.query(Catches).filter_by(id = UserID).one())


        if choice == '4':
            UserID = int(input("Enter the Id of the user you seek:"))
            newHolder = input("Enter the name of the new holder: ")
            for catches in search_session.query(Catches).filter_by(id = UserID):
                catches.Holder = newHolder
                search_session.commit()


        if choice == '5':
            UserID = int(input("Enter the Id of the user you seek:"))
            newCountry = input("Enter the Country of the holder to update")
            for catches in search_session.query(Catches).filter_by(id = UserID):
                catches.Country = newCountry
                search_session.commit()


        if choice == '6':
            UserID = int(input("Enter the Id of the user you seek:"))
            newCatchesNum = int(input("Enter the number of catches to update:"))
            for catches in search_session.query(Catches).filter_by(id = UserID):
                catches.NumOfCatches = newCatchesNum
                search_session.commit()

        if choice == '7':
            UserID = int(input("Enter the ID of the user you seek:"))
            for catches in delete_session.query(Catches).filter_by(id = UserID):
                delete_session.delete(catches)
                delete_session.commit()

        delete_session.close()
        search_session.close()


        if choice == '8':
            break

def menu ():
    print ('''
                1. to print table
                2. to add row
                3. to search for a record
                4. to update holder
                5. to update Country
                6. to update catches number
                7. to delete row
                8. quit''')

main()
