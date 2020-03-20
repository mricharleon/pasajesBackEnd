from pasajes.models.page import Page


class RepositorioPasaje:
    
    @classmethod
    def all_pasajes(cls, request):
        query_pasajes = request.dbsession.query(Page).filter_by().all()

        return query_pasajes

    @classmethod
    def pasaje_by_id(cls, request, pasaje_id):
        query_pasaje = request.dbsession.query(Page).filter(Page.id == pasaje_id).first()

        return query_pasaje

    # @classmethod
    # def car_by_id(cls, car_id):
    #     session = DbSessionFactory.create_session()

    #     car = session.query(Car).filter(Car.id == car_id).first()

    #     session.close()

    #     return car

    # @classmethod
    # def add_car(cls, car: Car):
    #     session = DbSessionFactory.create_session()

    #     db_car = Car()
    #     db_car.last_seen = car.last_seen
    #     db_car.brand = car.brand
    #     db_car.image = car.image if car.image else random.choice(cls.__fake_image_url)
    #     db_car.damage = car.damage
    #     db_car.year = int(car.year)
    #     db_car.price = int(car.price)
    #     db_car.name = car.name

    #     session.add(db_car)
    #     session.commit()

    #     return db_car

    # @classmethod
    # def update_car(cls, car):

    #     session = DbSessionFactory.create_session()

    #     db_car = session.query(Car).filter(Car.id == car.id).first()
    #     db_car.last_seen = car.last_seen
    #     db_car.brand = car.brand
    #     db_car.image = car.image if car.image else random.choice(cls.__fake_image_url)
    #     db_car.damage = car.damage
    #     db_car.year = car.year
    #     db_car.price = car.price
    #     db_car.name = car.name

    #     session.commit()

    #     return db_car

    # @classmethod
    # def delete_car(cls, car_id):
    #     session = DbSessionFactory.create_session()
    #     db_car = session.query(Car).filter(Car.id == car_id).first()
    #     if not db_car:
    #         return

    #     session.delete(db_car)
    #     session.commit()

    # @classmethod
    # def find_user_by_api_key(cls, api_key: str) -> User:

    #     session = DbSessionFactory.create_session()
    #     user = session.query(User).filter(User.api_key == api_key).first()
    #     session.close()

    #     return user

    # @classmethod
    # def create_user(cls, username):

    #     session = DbSessionFactory.create_session()

    #     user = User(name=username)
    #     session.add(user)

    #     session.commit()

    #     return user
