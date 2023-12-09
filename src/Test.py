from utils.dal import *
from logic.users_logic import *
from models.user_model import *
from models.vacation_model import *
from facades.user_facade import *
from facades.vacation_facade import *


# def test_all():
#     print("---------------------------Signing up a new user: ---------------------------------")
#     print()
#     print()


print("Valid user test (Adding user Gilad Dabush successfuly to the users table):")

try:
    with UsersFacade() as facade:
        user = facade.register_user("Gilad", "Dabush", "asd@123.COM", "fd453", 2)
        print("User added successfully")
except Exception as err:
    print(err)

#     print()
#     print()


#     print("Failing to add Admin user (error: 'Can not add Admin role') :")

#     try:
#         with UsersFacade() as facade:
#             user=facade.register_user("Gilad", "Dabush", "asd@t23.COM","fd453", 1)
#     except Exception as err:
#         print(err)

#     print()
#     print()


#     print("All fields are required (error: 'All fields must be filled') :")

#     try:
#         with UsersFacade() as facade:
#             user=facade.register_user("", "Dabush", "asd@t23.COM","fd453", 2)
#     except Exception as err:
#         print(err)


#     print()
#     print()


#     print("Password must be at least 4 chars (error: 'Password must be at least 4 characters long') :")

#     try:
#         with UsersFacade() as facade:
#             user=facade.register_user("Gilad", "Dabush", "asd@t23.COM","fd4", 2)
#     except Exception as err:
#         print(err)

#     print()
#     print()


#     print("Email already exists (error: 'User with this email already exists'):")

#     try:
#         with UsersFacade() as facade:
#             user=facade.register_user("Gilad", "Dabush", "asd@123.COM","fd453", 2)
#     except Exception as err:
#         print(err)
#     print()
#     print("---------------------------------------------------------------------------------------------------------------------------------")

#     print()
#     print("------------------login user to the system:--------------")
#     print()
#     print()

#     print("Get user by email and password - successful login.")

#     with UsersFacade() as facade:

#         user=facade.login_user("asd@123.COM", "fd453")
#         if user:
#             user.display()
#         else:
#             print("User not found")
#     print()
#     print()


#     print("All fields are required! (error: 'All fields must be filled'):")
#     try:
#         with UsersFacade() as facade:

#             user=facade.login_user("", "fd453")
#             if user:
#                 user.display()
#             else:
#                 print("User not found")
#     except Exception as err:
#         print(err)

#     print()
#     print()


#     print("Invalid email! (error: 'Invalid email format'):")

#     try:
#         with UsersFacade() as facade:

#             user=facade.login_user("dfrgdfrdf.com", "fd453")
#             if user:
#                 user.display()
#             else:
#                 print("User not found")
#     except Exception as err:
#         print(err)

#     print()
#     print()

#     print("Invalid password (error: 'Password must be at least 4 characters long'):")

#     try:
#         with UsersFacade() as facade:

#             user=facade.login_user("dfrg@dfrdf.com", "f53")
#             if user:
#                 user.display()
#             else:
#                 print("User not found")
#     except Exception as err:
#         print(err)

#     print()
#     print()
#     print("--------------------------------------------- vacations-------------------------------------")
#     print()

#     print("Get all vacations ordered by start date including finished dates:")

#     with VacationsFacade() as facade:

#         result = facade.get_all_vacations()
#         for vacation in result:
#             vacation.display()

#     print()
#     print()

# print("Add new vacation to vacations table - success:")

# try:
#     with VacationsFacade() as facade:
#         last_vacation_id = facade.add_vacation(None, 7, "Unforgettable Japan food experience.", "2024-12-02", "2024-12-31", 5400, "japan_food_vacation.jpg")
#         print("Vacation added successfully")
# except Exception as err:
#     print(err)


    # print("All fields are required: ( Error: 'All fields must be filled')")

    # try:
    #     with VacationsFacade() as facade:
    #         vacation=facade.add_vacation(None, 7, "", "2024-05-11", "2024-06-11", 5400, "japan_food_vacation.jpg")
    # except Exception as err:
    #     print(err)

    # print()
    # print()

    # print("Illegal price: ( Error:'Price is illegal')")

    # try:
    #     with VacationsFacade() as facade:
    #         vacation=facade.add_vacation(None, 7, "Unforgettable Japan food experience.", "2024-05-11", "2024-06-11", -2, "japan_food_vacation.jpg")
    # except Exception as err:
    #     print(err)
    # print()
    # print()

    # print("Start date later than end date: ( Error:'Vacation start date can't be later than the end date')")

    # try:
    #     with VacationsFacade() as facade:
    #         vacation=facade.add_vacation(None, 7, "Unforgettable Japan food experience.", "2024-05-11", "2024-04-11", -2, "japan_food_vacation.jpg")
    # except Exception as err:
    #     print(err)
    # print()
    # print()

    # print("Trying to insert past date: ( Error:'You can not pick past date')")

    # try:
    #     with VacationsFacade() as facade:
    #         vacation=facade.add_vacation(None, 7, "Unforgettable Japan food experience.", "2023-03-11", "2023-04-11", 2500, "japan_food_vacation.jpg")
    # except Exception as err:
    #     print(err)
    # print()
    # print()

    # print("--------------------------------------------UPDATE VACATION----------------------------------------")
    # print()

    # print("Update vacation - success:")

    # try:
    #     with VacationsFacade() as facade:
    #         vacation=facade.update_vacation(5, "The best Egypt food experience.", "2024-08-16", "2024-09-10", 4800, "egypt_food_vacation_new.jpg",5)
    #         print("Vacation was updated successfully")
    # except Exception as err:
    #     print(err)
    # print()
    # print()

    # print("Update vacation - all fields are required: (Error: 'All fields must be filled')")

    # try:
    #     with VacationsFacade() as facade:
    #         vacation=facade.update_vacation(5, "", "2024-08-16", "2024-09-10", 4700, "egypt_food_vacation_new.jpg", 5)
    # except Exception as err:
    #     print(err)

    # print()
    # print()

    # print("Update vacation - Illegal price: (Error: 'Price is illegal')")

    # try:
    #     with VacationsFacade() as facade:
    #         vacation=facade.update_vacation(5, "The best Egypt food experience.", "2024-08-16", "2024-09-10", 12000, "egypt_food_vacation_new.jpg", 5)
    # except Exception as err:
    #     print(err)
    # print()
    # print()

    # print("Start date later than end date: ( Error:'Vacation start date can't be later than the end date')")

    # try:
    #     with VacationsFacade() as facade:
    #         vacation=facade.update_vacation(5, "The best Egypt food experience.", "2024-10-16", "2024-09-10", 12000, "egypt_food_vacation_new.jpg", 5)
    # except Exception as err:
    #     print(err)

    # print()
    # print()

    # print("-------------------------------------------------DELETE VACATION--------------------------------------------------------")

    # print("Delete vacation - SUCCESS:")
    # try:
    #     with VacationsFacade() as facade:

    #         delete=facade.delete_vacation(8, 1)
    #         print("Vacation has been deleted")
    # except Exception as err:
    #     print(err)
    # print()
    # print()

    # print("Add like to likes table:")

    # try:
    #     with UsersFacade() as facade:

    #         facade.add_user_like(user_id=2, vacation_id=9)
    #         print("The like was added successfully")
    # except Exception as err:
    #     print(err)
    # print()
    # print()


    # print("Delete like from likes table:")

    # print()
    # print("Admin can not unlike a vacation. Error:'Only users can unlike vacations'")

    # try:
    #     with UsersFacade() as facade:

    #         facade.delete_like(user_id=2, vacation_id=9)
    #         print("The like was deleted successfully")
    # except Exception as err:
    #     print(err)

    # print()
    # print()

    # print("Only user can unlike a vacation- success")

    # try:
    #     with UsersFacade() as facade:

    #         facade.delete_like(user_id=2, vacation_id=9)
    #         print("The like was deleted successfully")
    # except Exception as err:
    #     print(err)