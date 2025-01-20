





# user_id (UUID, Primary Key)
# first_name (VARCHAR)
# last_name (VARCHAR)
# email (VARCHAR, Unique)
# password_hash (VARCHAR)
# phone_number (VARCHAR, Unique)
# created_at (TIMESTAMP)
# updated_at (TIMESTAMP)

from sqlalchemy import Column, String, DateTime, JSON

class User(Base):
    __tablename__ = 'users'
    user_id = Column(String(255), primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    phone_number = Column(String(255), unique=True)
    attributes = Column(JSON, nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'phone_number': self.phone_number,
            'attributes': self.attributes,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def add_user(self, session):
        try:
            return _add_user(self, session)
        except:
            return False, None
        
    def update_user(self, session):
        try:
            return _update_user(self, session)
        except:
            return False, None
    
    def delete_user(self, session):
        try:
            return _delete_user(self, session)
        except:
            return False, None
        
    @staticmethod
    def get_user(user_id, session):
        try:
            return _get_user(user_id, session)
        except:
            return False, None
    
    @staticmethod
    def get_all_users(session):
        try:
            return _get_all_users(session)
        except:
            return False, None
        
class UserProvider(User):

    @staticmethod
    def get_by_attribute(attribute_name, content):
        try:
            return _get_by_attribute(attribute_name, content)
        except:
            return False, None
        
def _add_user(user, session):
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        # user_dict = User.to_dict(user)
        # logger.debug(f"User added: {user_dict}")
        return True, user
    except:
        session.rollback()
        return False, None
    
def _update_user(user, session):
        try:
            session.commit()
            return True, user
        except:
            session.rollback()
            return False, None
        
def _delete_user(user, session):
    try:
        session.delete(user)
        session.commit()
        return True, user
    except:
        session.rollback()
        return False, None