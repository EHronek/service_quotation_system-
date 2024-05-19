from new_base_model import Base, Client, Quotation, User, Organization, Finance, Payment, AssetExpenditure, AssetTemporary, Deposit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

def setup_db(user, password, database_name):
    # Create the engine and bind it to the Base metadata
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{database_name}', pool_pre_ping=True)
    Base.metadata.create_all(engine)  # Create tables based on the Base classes
    
    # Create a session
    Session = sessionmaker(bind=engine)
    #session = Session()
    
    """ # Create a test client entry
    client_test = Client(
        client_id="CLT_06", 
        client_name="Test client", 
        contact=23455, 
        email="testclient@email", 
        application_type="Mobile Application", 
        project_title="test title", 
        project_cost=3000, 
        project_deadline=datetime(2024, 2, 23),  # Properly formatted datetime object
        project_status="Test status", 
        development_status="dev status"
    )
    
    # Add the entry to the session and commit
    session.add(client_test)
    session.commit()
    
    # Optionally, close the session
    session.close() """

    return Session()

# Run the connection function with the provided credentials and database name
""" if __name__ == "__main__":
    session = setup_db("root", "root", "sysdb") """
