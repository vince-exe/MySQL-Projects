from errors.handle_errors import add_admin_errors, print_admin_errors

from utilities.enums import *
from utilities.utils import get_info_person, print_admins


def print_admin_menu(database, cursor):
    limit = 5
    while True:
        try:
            option = int(input("\n1)View Admins (5 at time)"
                               "\n2)Exit"
                               "\n\nInsert option (1 / 2): "))

            if option == 1:
                check = database.get_admins(cursor, limit)

                if print_admin_errors(check):
                    print_admins(check)
                    limit += 5

            elif option == 2:
                return

            else:
                print(f"\n{option} can not be an option")

        except ValueError:
            print("\nOption must be a number!!")


def super_root_menu(database, cursor, connection):
    while True:
        try:
            option = int(input("\n1)Add Admin"
                               "\n2)Delete Admin"
                               "\n3)Search Admin"
                               "\n4)Modify Admin"
                               "\n5)View Admins"
                               "\n6)Exit"
                               "\n\nInsert option (1 / 6): "))

            if option == get_value(SuperRootOptions.ADD_ADMIN):  # Add Admin
                info = get_info_person()
                if add_admin_errors(database.add_person(cursor, info, connection), info):
                    database.add_root(cursor, connection)

            elif option == get_value(SuperRootOptions.DELETE_ADMIN):  # Delete Admin
                pass

            elif option == get_value(SuperRootOptions.SEARCH_ADMIN):  # Search Admin
                pass

            elif option == get_value(SuperRootOptions.MODIFY_ADMIN):  # Modify Admin
                pass

            elif option == get_value(SuperRootOptions.VIEW_ADMINS):
                print_admin_menu(database, cursor)

            elif option == get_value(SuperRootOptions.EXIT):  # Exit
                return

            else:
                print(f'\n{option} is not an option')

        except ValueError:
            print("\nOption must be a number!!")