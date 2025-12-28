import uuid
import bcrypt
from db.conn import SessionLocal
from db.tables import RestoClient

class Password:
    @staticmethod
    def encrypt_pass(new_pass:str):
        salt = bcrypt.gensalt()
        hashed_pass = bcrypt.hashpw(new_pass.encode('utf-8'), salt)
        return hashed_pass.decode('utf-8')
    
    @staticmethod
    def verify_pass(raw_pass:str, hash_pass:str) -> bool:
        return bcrypt.checkpw(raw_pass.encode('utf-8'), hash_pass.encode('utf-8'))

def check_user_exists(email = None, phone = None) -> bool | dict[str, str]:
    if not email and not phone:
        return {
            "message":"error while verifying user, either email or phone is required"
        }
    
    with SessionLocal() as session:
        if email:
            user = session.query(RestoClient).filter_by(email=email).first()
        elif phone:
            user = session.query(RestoClient).filter_by(phone=phone).first()
    
    return True if user else False

def new_client(first_name:str, last_name:str, email:str, phone:str, password:str):
    first_name = first_name.strip()
    last_name = last_name.strip()
    email = email.strip()
    phone = phone.strip()

    if check_user_exists(email=email, phone=phone):
        return {"message": "User already exists"}

    hashed_password = Password.encrypt_pass(password)
    
    new_user = RestoClient(
        restoId=0,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        password=hashed_password
    )
    
    with SessionLocal() as session:
        try:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user
        except Exception as e:
            session.rollback()
            return {"message": f"Error creating user: {str(e)}"}

if __name__ == "__main__":
    try:
        user = new_client(first_name="rishabh",last_name="test01",email="rishabh@test01.com",phone="234567890",password="rishabhtest01")
        print(user)
    except Exception as e:
        print(e)