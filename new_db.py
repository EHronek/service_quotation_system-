from new_base_model import Base, Client, Quotation, User, Organization, Finance, Payment, AssetExpenditure, AssetTemporary, Deposit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

def connection(user, password, database_name):
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{database_name}', pool_pre_ping=True)
    Base.metadata.create_all(engine)  # Create tables based on the Base classes
    Session = sessionmaker(bind=engine)
    session = Session()

    """ client_test = Client(
        client_id="CLT_02",
        client_name="Test client 2",
        contact=23455,
        email="testclient2@email.com",
        application_type="Web Application",
        project_title="test title",
        project_cost=3000,
        project_deadline=datetime(2024, 2, 23),
        project_status="Test status",
        development_status="dev status"
    ) """
    #session.add(client_test)
    #session.commit()
    return session

if __name__ == "__main__":
    connection("root", "root", "sysdb")
