from database import CurserFromConnectionFromPool
from colorama import Fore, Style
from datetime import datetime

BOLD = '\033[1m'


class UserSignUp():
    def __init__(self, user_name, password, u_id ):
        self.user_name = user_name
        self.password = password
        self.u_id = u_id


    @classmethod
    def signup_information(cls):
        user_name = str(input(f"{BOLD}Enter a Username: {Style.RESET_ALL}"))
        password = str(input(f"{BOLD}Enter a Password: {Style.RESET_ALL}"))
        u_id = None # will picked by default via Database.
        return cls(user_name, password, id)


    def save_to_db(self): #To save the new user in the database.
        with CurserFromConnectionFromPool() as cursor:
            cursor.execute("INSERT INTO users(user_name, password) VALUES (%s, crypt(%s, gen_salt('bf')))",
                           (self.user_name, self.password))
            print("{BOLD}Successfully Signed up, you can login with --login flag.{Style.RESET_ALL}")



class UserLogin():
    """
    to login and check the user from the database.
    if the user found, user will authenticate via UserAuth() class to do actions.
    if the user not found in the database, should try again.
    """
    def __init__(self, user_name, password, u_id ):
        self.user_name = user_name
        self.password = password
        self.u_id = u_id
        self.logged_in = False


    def return_user_id(self):
        with CurserFromConnectionFromPool() as cursor:
            cursor.execute(
                            'SELECT u_id FROM users WHERE user_name =%s '
                            'AND password is NOT NULL AND password = crypt(%s ,password)',
                            (self.user_name, self.password)
                        )

            user_u_id = cursor.fetchone()[0]
            return user_u_id
        return user_u_id


    @classmethod
    def login_information(cls):
        user_name = str(input(f"{BOLD}Username: {Style.RESET_ALL}"))
        password = str(input(f"{BOLD}Password: {Style.RESET_ALL}"))
        return cls(user_name, password, None)

    def check_login(self):
        with CurserFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM users WHERE user_name =%s '
                           'AND password is NOT NULL AND password = crypt(%s ,password)',
                           (self.user_name, self.password))
            user_data = cursor.fetchone()
            if user_data is not None:
                time = datetime.now().strftime("%c")
                print(f"\n{BOLD}{Fore.GREEN}[User {self.user_name} logged in]{Style.RESET_ALL}\n{time}\n{'-'*24}")
                self.logged_in = True
                while self.logged_in:
                    UserAuth.authenticate(self)

            else:
                logged_in = False
                while not logged_in:
                    print(f"{Fore.LIGHTRED_EX}Incorrect username or password, Try Again...{Style.RESET_ALL}")
                    data = UserLogin.login_information()
                    UserLogin.check_login(data)




class UserAuth(UserLogin):
    """
    To authenticate the logged in user to can use the options.
    (Based in user ID PRIMARY KEY in the database).
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def authenticate(self):
        from contact import Contacts

        input_flag = str(input(f"{BOLD}What do you want to do?{Style.RESET_ALL}\n"
                               f"{'--add':10}to add a new contact\n"
                               f"{'--del':10}to delete a contact\n"
                               f"{'--view':10}to view a specific contact\n"
                               f"{'--viewall':10}to view all saved contacts\n"
                               f"{'exit':10}to exit the program\n"))

        user_id = self.return_user_id()  # To know the logged in user ID
        if input_flag == '--view':
            Contacts.view_contact(user_id)
        elif input_flag == '--viewall':
            Contacts.view_all(user_id)
        elif input_flag == '--add':
            datas = Contacts.enter_data(user_id)
            Contacts.save_to_db(datas)
        elif input_flag == '--del':
            none_id = True
            Contacts.delete_contact(user_id)
            if none_id: # If the contactID doesn't exists, print a message to check the ID using --view and try again.
                UserAuth.authenticate(self)
        elif input_flag =='exit':
            exit()