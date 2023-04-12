from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLITE Series
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# PostgreSQL Series
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:N0meacuerd0@localhost/TodoApplicationDatabase"

# MYSQL Series
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:N0meacuerd0@127.0.0.1:3306/todoapp"

# SQLITE
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# MYSQL and PostgreSQL Series
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
