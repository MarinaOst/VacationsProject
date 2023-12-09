from utils.dal import *
from models.vacation_model import *


class VacationsLogic:

    def __init__(self):
        self.dal = DAL()

    def get_all_vacations(self):
        sql = "SELECT * FROM vacations ORDER BY vacation_start_date"
        result = self.dal.get_table(sql)
        vacations = VacationModel.dictionaries_to_vacations(result)
        return vacations

    def add_vacation(self, vacation_id, country_id, vacation_description, vacation_start_date, vacation_end_date, price, vacation_pic_file_name):
        sql = "INSERT INTO vacations(vacation_id, country_id, vacation_description, vacation_start_date, vacation_end_date, price, vacation_pic_file_name) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        last_row_id = self.dal.insert(sql, (vacation_id, country_id, vacation_description,
                                 vacation_start_date, vacation_end_date, price, vacation_pic_file_name))
        return last_row_id

    def update_vacation(self, vacation_id, country_id, vacation_description, vacation_start_date, vacation_end_date, price, vacation_pic_file_name):
        sql = "UPDATE vacations SET country_id = %s, vacation_description = %s, vacation_start_date=%s,vacation_end_date=%s, price = %s, vacation_pic_file_name = %s   WHERE vacation_id= %s"
        result = self.dal.update(sql, (vacation_id, country_id, vacation_description,
                                 vacation_start_date, vacation_end_date, price, vacation_pic_file_name))
        return result

    def delete_vacation(self, vacation_id):
        sql = "DELETE from vacations WHERE vacation_id = %s"
        result = self.dal.delete(sql, (vacation_id,))
        return result

    def close(self):
        self.dal.close()
