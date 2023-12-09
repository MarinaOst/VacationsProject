from utils.dal import *
from models.user_model import *


class UsersLogic:

    def __init__(self):
        self.dal = DAL()

    def add_user(self, user):
        sql = "INSERT INTO users(first_name, last_name, email, password, role_id) VALUES(%s, %s, %s, %s, %s)"
        last_row_id = self.dal.insert(
            sql, (user.first_name, user.last_name, user.email, user.password, user.role_id))
        return last_row_id
    




    def get_user(self, email, password):
        sql = "SELECT * FROM users WHERE email = %s and password = %s"
        result = self.dal.get_scalar(sql, (email, password))
        if result is None: return None
        user = UserModel.dictionary_to_user(result)
        return user
        
    

    def add_user_like(self, user_id, vacation_id):
        sql = "INSERT INTO likes(user_id, vacation_id) VALUES(%s, %s)"
        result = self.dal.insert(sql, (user_id, vacation_id))
        return result

    def delete_like(self, user_id, vacation_id):
        sql = "DELETE FROM likes WHERE user_id=%s and vacation_id=%s"
        result = self.dal.delete(sql, (user_id, vacation_id))
        return result

    def close(self):
        self.dal.close()
