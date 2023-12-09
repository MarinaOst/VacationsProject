from logic.vacations_logic import *
from datetime import datetime
from logic.users_logic import *


class VacationsFacade:

    # try:

    def __init__(self):
        self.logic = VacationsLogic()

    def get_all_vacations(self):
        return self.logic.get_all_vacations()

    def add_vacation(self, vacation_id, country_id, vacation_description, vacation_start_date, vacation_end_date, price, vacation_pic_file_name):
        current_date = datetime.now().date()
        converted_date = datetime.strptime(
            vacation_start_date, "%Y-%m-%d").date()
        if not country_id or not vacation_description or not vacation_start_date or not vacation_end_date or not price or not vacation_pic_file_name:
            raise ValueError("All fields must be filled")
        elif vacation_start_date > vacation_end_date:
            raise ValueError(
                "Vacation start date can't be later than the end date")
        elif price < 0 or price > 10000:
            raise ValueError("Price is illegal")
        elif converted_date < current_date:
            raise ValueError("You can not pick past date")
        elif UserModel.role_id !=1:
            raise ValueError("Only Admins can add vacations")
        else:
            last_row_id = self.logic.add_vacation(vacation_id, country_id, vacation_description,
                                             vacation_start_date, vacation_end_date, price, vacation_pic_file_name)
            return last_row_id

    def update_vacation(self, country_id, vacation_description, vacation_start_date, vacation_end_date, price, vacation_pic_file_name, vacation_id):
        if not country_id or not vacation_description or not vacation_start_date or not vacation_end_date or not price:
            raise ValueError("All fields must be filled")
        elif vacation_start_date > vacation_end_date:
            raise ValueError(
                "Vacation start date can't be later than the end date")
        elif price < 0 or price > 10000:
            raise ValueError("Price is illegal")
        else:
            result = self.logic.update_vacation(
                country_id, vacation_description, vacation_start_date, vacation_end_date, price, vacation_pic_file_name, vacation_id)
            return result

    def delete_vacation(self, vacation_id):
        result = self.logic.delete_vacation(vacation_id)
        return result

    def close(self):
        self.logic.close()

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()

# except:
