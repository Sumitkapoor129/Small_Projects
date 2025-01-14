from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




engine = create_engine("postgresql://postgres:1234@localhost:3008/ecommerce")
session=sessionmaker(autoflush=False,autocommit=False,bind=engine)
def get_ab():
    db=session()
    try:
        yield db
    finally:
        db.close()    

