from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()

class Client(Base):
    """Client class that represents a table in the database"""
    __tablename__ = "client_tb"

    client_id = Column('client_id', String, primary_key=True)
    client_name = Column("client_name", String)
    contact = Column("contact", Integer)
    email = Column("email", String)
    application_type = Column("application_type", String)
    project_title = Column("project_title", String)
    project_cost = Column("project_cost", Integer)
    project_deadline = Column("project_deadline", DateTime)
    project_status = Column("project_status", String)
    development_status = Column("development_status", String)

    # Establish relationship with Quotation
    quotations = relationship("Quotation", back_populates="client")
    finances = relationship("Finance", back_populates="client")


class Quotation(Base):
    __tablename__ = "quotation_tb"

    quotation_number = Column("quotation_number", String, primary_key=True)
    client_id = Column(String, ForeignKey('client_tb.client_id'))
    client_name = Column("client_name", String)
    contact = Column("contact", Integer)
    client_email = Column("client_email", String)
    application_type = Column("application_type", String)
    service_name = Column("service_name", String)
    service_description = Column("service_description", String)
    service_cost = Column("service_cost", Integer)
    quotation_date = Column("quotation_date", DateTime)
    status = Column("status", String)

    # Establish relationship with Client
    client = relationship("Client", back_populates="quotations")


class User(Base):
    __tablename__ = "user_tb"

    user_id = Column("user_id", String, primary_key=True)
    fullname = Column("fullname", String)
    username = Column("username", String)
    user_password = Column("user_password", String)
    access_level = Column("access_level", String)
    security_code = Column("security_code", String)


class Organization(Base):
    __tablename__ = "organization_tb"

    organization_id = Column("organization_id", String, primary_key=True)
    organization_name = Column("organization_name", String)
    organization_contact = Column("organization_contact", Integer)
    location = Column("location", String)
    organization_email = Column("organization_email", String)
    email_password = Column("email_password", String)


class Finance(Base):
    __tablename__ = "finance_tb"

    transaction_id = Column("transaction_id", String, primary_key=True)
    client_id = Column(String, ForeignKey('client_tb.client_id'))
    client_name = Column("client_name", String)
    client_email = Column("client_email", String)
    amount = Column("amount", Integer)
    payment_mode = Column("payment_mode", String)
    payment_date = Column("payment_date", DateTime)

    # Establish relationship with Client
    client = relationship("Client", back_populates="finances")


class Payment(Base):
    __tablename__ = "payment_tb"

    transaction_id = Column("transaction_id", String, primary_key=True)
    expenditure_type = Column("expenditure_type", String)
    paid_to = Column("paid_to", String)
    contact = Column("contact", Integer)
    email = Column("email", String)
    total_paid = Column("total_paid", Integer)
    transaction_mode = Column("transaction_mode", String)
    transaction_cost = Column("transaction_cost", Integer)
    total_spent = Column("total_spent", Integer)
    processed_date = Column("processed_date", DateTime)


class AssetExpenditure(Base):
    __tablename__ = "asset_expenditure_tb"
    
    record_id = Column("record_id", Integer, primary_key=True)
    asset_name = Column("asset_name", String)
    asset_cost = Column("asset_cost", Integer)
    quantity = Column("quantity", Integer)
    total_cost = Column("total_cost", Integer)
    purchase_date = Column("purchase_date", DateTime)


class AssetTemporary(Base):
    __tablename__ = "asset_temporary_tb"

    record_id = Column('record_id', Integer, primary_key=True)
    asset_name = Column('asset_name', String)
    asset_cost = Column('asset_cost', Integer)
    quantity = Column('quantity', Integer)
    total_cost = Column('total_cost', Integer)
    purchase_date = Column('purchase_date', DateTime)


class Deposit(Base):
    __tablename__ = "deposit_tb"

    transaction_id = Column('transaction_id', String, primary_key=True)
    amount = Column('amount', Integer)
    deposit_date = Column('deposit_date', DateTime)
