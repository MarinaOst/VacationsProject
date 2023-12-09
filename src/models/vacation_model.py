class VacationModel:
    def __init__(self, vacation_id, country_id, vacation_description, vacation_start_date, vacation_end_date, price, vacation_pic_file_name):
        self.vacation_id = vacation_id
        self.country_id = country_id
        self.vacation_description = vacation_description
        self.vacation_start_date = vacation_start_date
        self.vacation_end_date = vacation_end_date
        self.price = price
        self.vacation_pic_file_name = vacation_pic_file_name

    def display(self):
        print(f"ID: {self.vacation_id}, Description: {self.vacation_description}, Start date: {self.vacation_start_date}, End date:{self.vacation_end_date}, Price: {self.price}")

    @staticmethod
    def dictionary_to_vacation(dictionary):
        vacation_id = dictionary["vacation_id"]
        country_id = dictionary["country_id"]
        vacation_description = dictionary["vacation_description"]
        vacation_start_date = dictionary["vacation_start_date"]
        vacation_end_date = dictionary["vacation_end_date"]
        price = dictionary["price"]
        vacation_pic_file_name = dictionary["vacation_pic_file_name"]
        vacation = VacationModel(vacation_id, country_id, vacation_description,
                                 vacation_start_date, vacation_end_date, price, vacation_pic_file_name)
        return vacation

    @staticmethod
    def dictionaries_to_vacations(list_of_dictionaries):
        vacations = []
        for item in list_of_dictionaries:
            vacation = VacationModel.dictionary_to_vacation(item)
            vacations.append(vacation)
        return vacations
