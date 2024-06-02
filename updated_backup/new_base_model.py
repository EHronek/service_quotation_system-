""" from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()

class Client(Base):
    '''Client class that represents a table in the database'''
    __tablename__ = "client_tb"

    client_id = Column(String(100), primary_key=True)
    client_name = Column(String(100))
    contact = Column(Integer)
    email = Column(String(100))
    application_type = Column(String(100))
    project_title = Column(String(100))
    project_cost = Column(Integer)
    project_deadline = Column(DateTime)
    project_status = Column(String(100))
    development_status = Column(String(100))

    # Establish relationship with Quotation
    quotations = relationship("Quotation", back_populates="client")
    finances = relationship("Finance", back_populates="client")


class Quotation(Base):
    __tablename__ = "quotation_tb"

    quotation_number = Column(String(100), primary_key=True)
    client_id = Column(String(100), ForeignKey('client_tb.client_id'))
    client_name = Column(String(100))
    contact = Column(Integer)
    client_email = Column(String(100))
    application_type = Column(String(100))
    service_name = Column(String(100))
    service_description = Column(String(100))
    service_cost = Column(Integer)
    quotation_date = Column(DateTime)
    status = Column(String(100))

    # Establish relationship with Client
    client = relationship("Client", back_populates="quotations")


class User(Base):
    __tablename__ = "user_tb"

    user_id = Column( String(100), primary_key=True)
    fullname = Column(String(100))
    username = Column(String(100))
    user_password = Column(String(100))
    access_level = Column(String(100))
    security_code = Column(String(100))


class Organization(Base):
    __tablename__ = "organization_tb"

    organization_id = Column(String(100), primary_key=True)
    organization_name = Column(String(100))
    organization_contact = Column(Integer)
    location = Column(String(100))
    organization_email = Column(String(100))
    email_password = Column(String(100))


class Finance(Base):
    __tablename__ = "finance_tb"

    transaction_id = Column(String(100), primary_key=True)
    client_id = Column(String(100), ForeignKey('client_tb.client_id'))
    client_name = Column(String(100))
    client_email = Column(String(100))
    amount = Column(Integer)
    payment_mode = Column(String(100))
    payment_date = Column(DateTime)

    # Establish relationship with Client
    client = relationship("Client", back_populates="finances")


class Payment(Base):
    __tablename__ = "payment_tb"

    transaction_id = Column(String(100), primary_key=True)
    expenditure_type = Column(String(100))
    paid_to = Column(String(100))
    contact = Column(Integer)
    email = Column(String(100))
    total_paid = Column( Integer)
    transaction_mode = Column(String(100))
    transaction_cost = Column(Integer)
    total_spent = Column(Integer)
    processed_date = Column(DateTime)


class AssetExpenditure(Base):
    __tablename__ = "asset_expenditure_tb"
    
    record_id = Column(Integer, primary_key=True)
    asset_name = Column(String(100))
    asset_cost = Column(Integer)
    quantity = Column(Integer)
    total_cost = Column(Integer)
    purchase_date = Column(DateTime)


class AssetTemporary(Base):
    __tablename__ = "asset_temporary_tb"

    record_id = Column(Integer, primary_key=True)
    asset_name = Column(String(100))
    asset_cost = Column(Integer)
    quantity = Column(Integer)
    total_cost = Column(Integer)
    purchase_date = Column(DateTime)


class Deposit(Base):
    __tablename__ = "deposit_tb"

    transaction_id = Column(String(100), primary_key=True)
    amount = Column(Integer)
    deposit_date = Column(DateTime)
 """
""" 
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()

class Client(Base):
    '''Client class that represents a table in the database'''
    __tablename__ = "client_tb"

    client_id = Column(String(50), primary_key=True)
    client_name = Column(String(128))
    contact = Column(Integer)
    email = Column(String(128))
    application_type = Column(String(128))
    project_title = Column(String(128))
    project_cost = Column(Integer)
    project_deadline = Column(DateTime)
    project_status = Column(String(128))
    development_status = Column(String(128))

    # Establish relationships with other tables
    quotations = relationship("Quotation", back_populates="client")
    finances = relationship("Finance", back_populates="client")


class Quotation(Base):
    __tablename__ = "quotation_tb"

    quotation_number = Column(String(50), primary_key=True)
    client_id = Column(String(50), ForeignKey('client_tb.client_id'))
    client_name = Column(String(128))
    contact = Column(Integer)
    client_email = Column(String(128))
    application_type = Column(String(128))
    service_name = Column(String(128))
    service_description = Column(String(255))
    service_cost = Column(Integer)
    quotation_date = Column(DateTime)
    status = Column(String(128))

    # Establish relationship with Client
    client = relationship("Client", back_populates="quotations")


class Finance(Base):
    __tablename__ = "finance_tb"

    transaction_id = Column(String(50), primary_key=True)
    client_id = Column(String(50), ForeignKey('client_tb.client_id'))
    client_name = Column(String(128))
    client_email = Column(String(128))
    amount = Column(Integer)
    payment_mode = Column(String(50))
    payment_date = Column(DateTime)

    # Establish relationship with Client
    client = relationship("Client", back_populates="finances")


class User(Base):
    __tablename__ = "user_tb"

    user_id = Column(String(50), primary_key=True)
    fullname = Column(String(128))
    username = Column(String(128))
    user_password = Column(String(128))
    access_level = Column(String(50))
    security_code = Column(String(50))


class Organization(Base):
    __tablename__ = "organization_tb"

    organization_id = Column(String(50), primary_key=True, autoincrement=True)
    organization_name = Column(String(128))
    organization_contact = Column(Integer)
    location = Column(String(128))
    organization_email = Column(String(128))
    email_password = Column(String(128))


class Payment(Base):
    __tablename__ = "payment_tb"

    transaction_id = Column(String(50), primary_key=True)
    expenditure_type = Column(String(50))
    paid_to = Column(String(128))
    contact = Column(Integer)
    email = Column(String(128))
    total_paid = Column(Integer)
    transaction_mode = Column(String(50))
    transaction_cost = Column(Integer)
    total_spent = Column(Integer)
    processed_date = Column(DateTime)


class AssetExpenditure(Base):
    __tablename__ = "asset_expenditure_tb"

    record_id = Column(Integer, primary_key=True, autoincrement=True)
    asset_name = Column(String(128))
    asset_cost = Column(Integer)
    quantity = Column(Integer)
    total_cost = Column(Integer)
    purchase_date = Column(DateTime)


class AssetTemporary(Base):
    __tablename__ = "asset_temporary_tb"

    record_id = Column(Integer, primary_key=True, autoincrement=True)
    asset_name = Column(String(128))
    asset_cost = Column(Integer)
    quantity = Column(Integer)
    total_cost = Column(Integer)
    purchase_date = Column(DateTime)


class Deposit(Base):
    __tablename__ = "deposit_tb"

    transaction_id = Column(String(50), primary_key=True)
    amount = Column(Integer)
    deposit_date = Column(DateTime)


class Employee(Base):
    __tablename__ = "employee_tb"

    employee_id = Column(Integer, primary_key=True)
    employee_name = Column(String(100))
    employee_contact = Column(Integer)
    employee_email = Column(String(128))
    employee_role = Column(String(100))

 """



""" from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Sequence, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Example for PostgreSQL
client_id_seq = Sequence('client_id_seq', start=1, increment=1)
quotation_id_seq = Sequence('quotation_id_seq', start=1, increment=1)
user_id_seq = Sequence('user_id_seq', start=1, increment=1)
organization_id_seq = Sequence('organization_id_seq', start=1, increment=1)
finance_id_seq = Sequence('finance_id_seq', start=1, increment=1)
payment_id_seq = Sequence('payment_id_seq', start=1, increment=1)
asset_expenditure_id_seq = Sequence('asset_expenditure_id_seq', start=1, increment=1)
asset_temporary_id_seq = Sequence('asset_temporary_id_seq', start=1, increment=1)
deposit_id_seq = Sequence('deposit_id_seq', start=1, increment=1)
employee_id_seq = Sequence('employee_id_seq', start=1, increment=1)


Base = declarative_base()

class Client(Base):
    '''Client class that represents a table in the database'''
    __tablename__ = "client_tb"

    client_id = Column(Integer, client_id_seq, primary_key=True, server_default=client_id_seq.next_value())
    client_name = Column(String(128))
    contact = Column(Integer)
    email = Column(String(128))
    application_type = Column(String(128))
    project_title = Column(String(128))
    project_cost = Column(Integer)
    project_deadline = Column(DateTime)
    project_status = Column(String(128))
    development_status = Column(String(128))

    # Establish relationships with other tables
    quotations = relationship("Quotation", back_populates="client")
    finances = relationship("Finance", back_populates="client")


class Quotation(Base):
    __tablename__ = "quotation_tb"

    quotation_number = Column(Integer, quotation_id_seq, primary_key=True, server_default=quotation_id_seq.next_value())
    client_id = Column(Integer, ForeignKey('client_tb.client_id'))
    client_name = Column(String(128))
    contact = Column(Integer)
    client_email = Column(String(128))
    application_type = Column(String(128))
    service_name = Column(String(128))
    service_description = Column(String(255))
    service_cost = Column(Integer)
    quotation_date = Column(DateTime)
    status = Column(String(128))

    # Establish relationship with Client
    client = relationship("Client", back_populates="quotations")


class Finance(Base):
    __tablename__ = "finance_tb"

    transaction_id = Column(Integer, finance_id_seq, primary_key=True, server_default=finance_id_seq.next_value())
    client_id = Column(Integer, ForeignKey('client_tb.client_id'))
    client_name = Column(String(128))
    client_email = Column(String(128))
    amount = Column(Integer)
    payment_mode = Column(String(50))
    payment_date = Column(DateTime)

    # Establish relationship with Client
    client = relationship("Client", back_populates="finances")


class User(Base):
    __tablename__ = "user_tb"

    user_id = Column(Integer, user_id_seq, primary_key=True, server_default=user_id_seq.next_value())
    fullname = Column(String(128))
    username = Column(String(128))
    user_password = Column(String(128))
    access_level = Column(String(50))
    security_code = Column(String(50))


class Organization(Base):
    __tablename__ = "organization_tb"

    organization_id = Column(Integer, organization_id_seq, primary_key=True, server_default=organization_id_seq.next_value())
    organization_name = Column(String(128))
    organization_contact = Column(Integer)
    location = Column(String(128))
    organization_email = Column(String(128))
    email_password = Column(String(128))


class Payment(Base):
    __tablename__ = "payment_tb"

    transaction_id = Column(Integer, payment_id_seq, primary_key=True, server_default=payment_id_seq.next_value())
    expenditure_type = Column(String(50))
    paid_to = Column(String(128))
    contact = Column(Integer)
    email = Column(String(128))
    total_paid = Column(Integer)
    transaction_mode = Column(String(50))
    transaction_cost = Column(Integer)
    total_spent = Column(Integer)
    processed_date = Column(DateTime)


class AssetExpenditure(Base):
    __tablename__ = "asset_expenditure_tb"

    record_id = Column(Integer, asset_expenditure_id_seq, primary_key=True, server_default=asset_expenditure_id_seq.next_value())
    asset_name = Column(String(128))
    asset_cost = Column(Integer)
    quantity = Column(Integer)
    total_cost = Column(Integer)
    purchase_date = Column(DateTime)


class AssetTemporary(Base):
    __tablename__ = "asset_temporary_tb"

    record_id = Column(Integer, asset_temporary_id_seq, primary_key=True, server_default=asset_temporary_id_seq.next_value())
    asset_name = Column(String(128))
    asset_cost = Column(Integer)
    quantity = Column(Integer)
    total_cost = Column(Integer)
    purchase_date = Column(DateTime)


class Deposit(Base):
    __tablename__ = "deposit_tb"

    transaction_id = Column(Integer, deposit_id_seq, primary_key=True, server_default=deposit_id_seq.next_value())
    amount = Column(Integer)
    deposit_date = Column(DateTime)


class Employee(Base):
    __tablename__ = "employee_tb"

    employee_id = Column(Integer, employee_id_seq, primary_key=True, server_default=employee_id_seq.next_value())
    employee_name = Column(String(100))
    employee_contact = Column(Integer)
    employee_email = Column(String(128))
    employee_role = Column(String(100))
 """





""" 
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define a sequence for integer primary keys
client_id_seq = Sequence('client_id_seq')
quotation_number_seq = Sequence('quotation_number_seq')
transaction_id_seq = Sequence('transaction_id_seq')
user_id_seq = Sequence('user_id_seq')
organization_id_seq = Sequence('organization_id_seq')
payment_id_seq = Sequence('payment_id_seq')
asset_expenditure_id_seq = Sequence('asset_expenditure_id_seq')
asset_temporary_id_seq = Sequence('asset_temporary_id_seq')
employee_id_seq = Sequence('employee_id_seq')

class Client(Base):
    '''Client class that represents a table in the database'''
    __tablename__ = "client_tb"

    client_id = Column(Integer, client_id_seq, primary_key=True, server_default=client_id_seq.next_value())
    client_name = Column(String(100))
    contact = Column(Integer)
    email = Column(String(100))
    application_type = Column(String(100))
    project_title = Column(String(100))
    project_cost = Column(Integer)
    project_deadline = Column(DateTime)
    project_status = Column(String(100))
    development_status = Column(String(100))

    quotations = relationship("Quotation", back_populates="client")
    finances = relationship("Finance", back_populates="client")

class Quotation(Base):
    __tablename__ = "quotation_tb"

    quotation_number = Column(Integer, quotation_number_seq, primary_key=True, server_default=quotation_number_seq.next_value())
    client_id = Column(Integer, ForeignKey('client_tb.client_id'))
    client_name = Column(String(100))
    contact = Column(Integer)
    client_email = Column(String(100))
    application_type = Column(String(100))
    service_name = Column(String(100))
    service_description = Column(String(100))
    service_cost = Column(Integer)
    quotation_date = Column(DateTime)
    status = Column(String(100))

    client = relationship("Client", back_populates="quotations")

class Finance(Base):
    __tablename__ = "finance_tb"

    transaction_id = Column(Integer, transaction_id_seq, primary_key=True, server_default=transaction_id_seq.next_value())
    client_id = Column(Integer, ForeignKey('client_tb.client_id'))
    client_name = Column(String(100))
    client_email = Column(String(100))
    amount = Column(Integer)
    payment_mode = Column(String(100))
    payment_date = Column(DateTime)

    client = relationship("Client", back_populates="finances")

class User(Base):
    __tablename__ = "user_tb"

    user_id = Column(Integer, user_id_seq, primary_key=True, server_default=user_id_seq.next_value())
    fullname = Column(String(100))
    username = Column(String(100))
    user_password = Column(String(100))
    access_level = Column(String(100))
    security_code = Column(String(100))

class Organization(Base):
    __tablename__ = "organization_tb"

    organization_id = Column(Integer, organization_id_seq, primary_key=True, server_default=organization_id_seq.next_value())
    organization_name = Column(String(100))
    organization_contact = Column(Integer)
    location = Column(String(100))
    organization_email = Column(String(100))
    email_password = Column(String(100))

class Payment(Base):
    __tablename__ = "payment_tb"

    transaction_id = Column(Integer, payment_id_seq, primary_key=True, server_default=payment_id_seq.next_value())
    expenditure_type = Column(String(100))
    paid_to = Column(String(100))
    contact = Column(Integer)
    email = Column(String(100))
    total_paid = Column(Integer)
    transaction_mode = Column(String(100))
    transaction_cost = Column(Integer)
    total_spent = Column(Integer)
    processed_date = Column(DateTime)

class AssetExpenditure(Base):
    __tablename__ = "asset_expenditure_tb"

    record_id = Column(Integer, asset_expenditure_id_seq, primary_key=True, server_default=asset_expenditure_id_seq.next_value())
    asset_name = Column(String(100))
    asset_cost = Column(Integer)
    quantity = Column(Integer)
    total_cost = Column(Integer)
    purchase_date = Column(DateTime)

class AssetTemporary(Base):
    __tablename__ = "asset_temporary_tb"

    record_id = Column(Integer, asset_temporary_id_seq, primary_key=True, server_default=asset_temporary_id_seq.next_value())
    asset_name = Column(String(100))
    asset_cost = Column(Integer)
    quantity = Column(Integer)
    total_cost = Column(Integer)
    purchase_date = Column(DateTime)

class Deposit(Base):
    __tablename__ = "deposit_tb"

    transaction_id = Column(Integer, transaction_id_seq, primary_key=True, server_default=transaction_id_seq.next_value())
    amount = Column(Integer)
    deposit_date = Column(DateTime)

class Employee(Base):
    __tablename__ = "employee_tb"

    employee_id = Column(Integer, employee_id_seq, primary_key=True, server_default=employee_id_seq.next_value())
    employee_name = Column(String(100))
    employee_contact = Column(Integer)
    employee_email = Column(String(128))
    employee_role = Column(String(100)) """

""" # Example: Creating the database engine and tables
engine = create_engine('mysql+pymysql://username:password@localhost/db_name')
Base.metadata.create_all(engine)

# Example: Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# Example: Adding a new client
new_client = Client(client_name='John Doe', contact=1234567890, email='john.doe@example.com')
session.add(new_client)
session.commit()
 """




from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()

class Client(Base):
    """Client class that represents a table in the database"""
    __tablename__ = "client_tb"

    client_id = Column(String(50), primary_key=True)
    client_name = Column(String(128))
    contact = Column(Integer)
    email = Column(String(128))
    registration_date = Column(DateTime)
    application_type = Column(String(128))
    project_title = Column(String(128))
    project_cost = Column(Integer)
    project_start_date = Column(DateTime)
    project_deadline = Column(DateTime)
    project_status = Column(String(128))
    development_status = Column(String(128))

    # Establish relationships with other tables
    #quotations = relationship("Quotation", back_populates="client")
    finances = relationship("Finance", back_populates="client")


class Quotation(Base):
    __tablename__ = "quotation_tb"

    quotation_number = Column(String(50), primary_key=True)
    #client_id = Column(String(50), ForeignKey('client_tb.client_id'))
    client_name = Column(String(128))
    contact = Column(Integer)
    client_email = Column(String(128))
    application_type = Column(String(128))
    service_name = Column(String(128))
    service_description = Column(String(255))
    service_cost = Column(Integer)
    quotation_date = Column(DateTime)
    status = Column(String(128))

    # Establish relationship with Client
    #client = relationship("Client", back_populates="quotations")


class Finance(Base):
    __tablename__ = "finance_tb"

    transaction_id = Column(String(50), primary_key=True)
    client_id = Column(String(50), ForeignKey('client_tb.client_id'))
    client_name = Column(String(128))
    client_email = Column(String(128))
    amount = Column(Integer)
    payment_mode = Column(String(50))
    payment_date = Column(DateTime)

    # Establish relationship with Client
    client = relationship("Client", back_populates="finances")


class User(Base):
    __tablename__ = "user_tb"

    user_id = Column(String(50), primary_key=True)
    fullname = Column(String(128))
    username = Column(String(128))
    user_password = Column(String(128))
    access_level = Column(String(50))
    security_code = Column(String(50))


class Organization(Base):
    __tablename__ = "organization_tb"

    organization_id = Column(String(50), primary_key=True)
    organization_name = Column(String(128))
    organization_contact = Column(Integer)
    location = Column(String(128))
    organization_email = Column(String(128))
    email_password = Column(String(128))



class Payment(Base):
    __tablename__ = "payment_tb"

    transaction_id = Column(String(50), primary_key=True)
    expenditure_type = Column(String(50))
    paid_to = Column(String(128))
    contact = Column(Integer)
    email = Column(String(128))
    total_paid = Column(Integer)
    transaction_mode = Column(String(50))
    transaction_cost = Column(Integer)
    total_spent = Column(Integer)
    processed_date = Column(DateTime)


class AssetExpenditure(Base):
    __tablename__ = "asset_expenditure_tb"

    record_id = Column(Integer, primary_key=True, autoincrement=True)
    asset_name = Column(String(128))
    asset_cost = Column(Integer)
    quantity = Column(Integer)
    total_cost = Column(Integer)
    purchase_date = Column(DateTime)


class AssetTemporary(Base):
    __tablename__ = "asset_temporary_tb"

    record_id = Column(Integer, primary_key=True, autoincrement=True)
    asset_name = Column(String(128))
    asset_cost = Column(Integer)
    quantity = Column(Integer)
    total_cost = Column(Integer)
    purchase_date = Column(DateTime)


class Deposit(Base):
    __tablename__ = "deposit_tb"

    transaction_id = Column(String(50), primary_key=True)
    amount = Column(Integer)
    deposit_date = Column(DateTime)

class Employee(Base):
    __tablename__ = "employee_tb"

    employee_id = Column(String(50), primary_key=True)
    employee_name = Column(String(100))
    employee_contact = Column(Integer)
    employee_email = Column(String(100))
    employee_role = Column(String(100))
