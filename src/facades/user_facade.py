from logic.users_logic import *
import re


class UsersFacade:

    def __init__(self):
        self.logic = UsersLogic()

    def is_valid_email(self, email):
        pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        return pattern.match(email)

    # Log in to the system:

    def login_user(self, email, password):
        if not email or not password:
            raise ValueError("All fields must be filled")
        elif not self.is_valid_email(email):
            raise ValueError("Invalid email format")
        elif len(password) < 4:
            raise ValueError("Password must be at least 4 characters long")
        else:
            result = self.logic.get_user(email, password)
            return result

    # Sign up to the system:

    
    def register_user(self,  first_name, last_name, email, password, role_id):

        if role_id == 1:
            raise ValueError("Can not add Admin role")
        existing_user = self.logic.get_user(email, password)
        if existing_user:
            raise ValueError("User with this email already exists")
        elif not first_name or not last_name or not email or not password or not role_id:
            raise ValueError("All fields must be filled")
        elif not self.is_valid_email(email):
            raise ValueError("Invalid email format")
        elif len(password) < 4:
            raise ValueError("Password must be at least 4 characters long")
        else:
            last_row_id = self.logic.add_user(
                 first_name, last_name, email, password, role_id)
            return last_row_id

    def add_user_like(self, user_id, vacation_id):
        result = self.logic.add_user_like(user_id, vacation_id)
        return result

        

    def delete_like(self, user_id, vacation_id):
        result = self.logic.delete_like(user_id, vacation_id)
        return result


    def close(self):
        self.logic.close()

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()
