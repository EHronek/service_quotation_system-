""" from base_model import Base, Client, Quotation, User, Organization, Finance, Payment, AssetExpenditure, AssetTemporary, Deposit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

def connection(user, password, database_name):
    # Create the engine and bind it to the Base metadata
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{database_name}', pool_pre_ping=True)
    Base.metadata.create_all(engine)  # Create tables based on the Base classes
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create a test client entry
    client_test = Client(
        client_id="CLT_01", 
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
    
    # Create a test quotation entry related to the client
    quotation_test = Quotation(
        quotation_number="QT_01",
        client_id="CLT_01",
        client_name="Test client",
        contact=23455,
        client_email="testclient@email",
        application_type="Mobile Application",
        service_name="Development",
        service_description="Development of a mobile app",
        service_cost=5000,
        quotation_date=datetime(2024, 1, 1),
        status="Pending"
    )
    
    # Add the entries to the session and commit
    session.add(client_test)
    session.add(quotation_test)
    session.commit()
    
    # Optionally, close the session
    session.close()

# Run the connection function with the provided credentials and database name
connection("root", "root", "sysdb")
 """
from new_base_model import Base, Client, Quotation, User, Organization, Finance, Payment, AssetExpenditure, AssetTemporary, Deposit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

def connection(user, password, database_name):
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{database_name}', pool_pre_ping=True)
    Base.metadata.create_all(engine)  # Create tables based on the Base classes
    Session = sessionmaker(bind=engine)
    session = Session()

    client_test = Client(
        client_id="CLT_01",
        client_name="Test client",
        contact=23455,
        email="testclient@email.com",
        application_type="Mobile Application",
        project_title="test title",
        project_cost=3000,
        project_deadline=datetime(2024, 2, 23),
        project_status="Test status",
        development_status="dev status"
    )
    session.add(client_test)
    session.commit()

connection("root", "root", "sysdb")
