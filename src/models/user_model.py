class UserModel:
    def __init__(self, id, first_name, last_name, email, password, role_id):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_id = role_id

    def display(self):
        print(f"ID: {self.id}, First name: {self.first_name}, Last name: {self.last_name}, Email: {self.email}, Role: {self.role_id}")

    @staticmethod
    def dictionary_to_user(dictionary):
        id = dictionary["user_id"]
        first_name = dictionary["first_name"]
        last_name = dictionary["last_name"]
        email = dictionary["email"]
        password = dictionary["password"]
        role_id = dictionary["role_id"]
        user = UserModel(id, first_name, last_name, email, password, role_id)
        return user

    @staticmethod
    def dictionaries_to_users(list_of_dictionaries):
        users = []
        for item in list_of_dictionaries:
            user = UserModel.dictionary_to_user(item)
            users.append(user)
            return users
