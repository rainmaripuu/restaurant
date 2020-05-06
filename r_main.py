from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant_models import Base, Restaurant, Table, Customer

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(
    CONNECTION_STRING.format(
        user="root", password="Kevaderoomud512", host="127.0.0.1", db="default"
    )
)
Base.metadata.create_all(eng)
Session = sessionmaker(bind=eng)
s = Session()



try:
     s.add_all(
        [
            Restaurant(num_of_tables=20, location='City center'),
            Restaurant(num_of_tables=15, location='Old town'),
            Restaurant(num_of_tables=17, location='Suburbs')
        ]
     )

     s.commit()
except IntegrityError:
     s.rollback()
     print('Restaurant already created!')


try:
    s.add_all(
        [
            Table(restaurant=1, number_of_seats=4, position='Street terrace, 1'),
            Table(restaurant=1, number_of_seats=2, position='Street terrace, 2'),
            Table(restaurant=1, number_of_seats=6, position='Courtyard terrace, 1'),
            Table(restaurant=1, number_of_seats=4, position='Main hall, 1'),
            Table(restaurant=2, number_of_seats=8, position='Main hall, 1'),
            Table(restaurant=3, number_of_seats=4, position='Terrace, 1'),
            Table(restaurant=3, number_of_seats=6, position='Main hall, 1')
        ]
    )

    s.commit()
except IntegrityError:
    s.rollback()
    print('Table already created!')

