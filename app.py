import user, click, os
from database import Database
from colorama import Fore, Style
from LOGO import x, github
BOLD = '\033[1m'

os.system('cls' if os.name == 'nt' else 'clear')
@click.command()
@click.option('--signup', is_flag=True, help='to sign up as a user ')
@click.option('--login', is_flag=True, help='to login the account')
@click.option('--add', is_flag=True, help="to add a new contact")
@click.option('--view', is_flag=True, help='to view specific contact ')
@click.option('--viewall', is_flag=True, help='to view all contacts')
@click.option('--delete', is_flag=True, help='to delete a contact')
# @click.password_option()
def cli(login, add, view, viewall, delete, signup):
    Database.initialise(database="cotactbook",
                        user="postgres",
                        password="147r258r",
                        host="localhost",
                        port="5432"
                        ) #create a database connection

    message = f"{BOLD}{Fore.BLACK}You should Login to add/view contacts...{Style.RESET_ALL}\n" \
              f"{BOLD}{'--login':10}{Style.RESET_ALL} To Login as existing user\n" \
              f"{BOLD}{'--signup':10}{Style.RESET_ALL} To Signup as a new user\n"
    if login:
        data = user.UserLogin.login_information()
        user.UserLogin.check_login(data)
    if signup:
        data = user.UserSignUp.signup_information()
        user.UserSignUp.save_to_db(data)
    else:
        print(message)

if __name__ == '__main__':
    cli()