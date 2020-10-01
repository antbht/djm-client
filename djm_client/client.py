from cmd import Cmd

import djm_sdk.exceptions

USER_ID='0302'
SEPARATOR="==================\n\n"
SEPARATOR2="----\n\n"

def catch_backend_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except djm_sdk.exceptions.BackendError:
            print("An error occurs while connecting to backend.\nPlease ensure system is ready or you request an existing resource.\n")
    return wrapper


def catch_value_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ex:
            print(f"The given argument is not accepted. {str(ex)}\nPlease retry with a correct arg.")
    return wrapper

class MainCmdLine(Cmd):

    intro = f"\nWelcome to your digitalized wallet !\n\n{SEPARATOR}Your USER_ID is {USER_ID}.\n\n{SEPARATOR}Type help or ? to have more information about your possibilities\n"

    prompt = "wallet > "

    def __init__(self, djm_api):
        super().__init__()
        self.api = djm_api

    def do_q(self, arg):
        """ Wrapper to do_quit"""
        return self.do_quit(arg)

    def do_quit(self, arg):
        """ Exit the shell. """
        print("Goodbye !")
        return True

    def do_about(self, arg):
        """ Return infos about the shell"""
        print(f"This was implemented by Antoine BUHOT, applicant for a dejamobile Software quality manager position.\n")
        print(f"October 2020\n")

    @catch_backend_error
    def do_my_cards(self, arg):
        print("Your cards:\n")
        i=1
        for card in self.api.get_cards(USER_ID):
            print(f"{i} - {card.id} : {card.hidden_pan}")
            i += 1
    @catch_value_error
    @catch_backend_error
    def do_add_card(self, pan):

        cards = self.api.add_card(USER_ID, pan)
        print("Card added.\n")

        print("Your cards:\n")
        i=1
        for card in cards:
            print(f"{i} - {card.id} : {card.hidden_pan}")
            i += 1

    @catch_value_error
    @catch_backend_error
    def do_delete_card(self, card_id):
    
        cards = self.api.delete_card(USER_ID, card_id)
        print("Card deleted.\n")

        self.do_my_cards(None)


if __name__ == '__main__':
   app = MainCmdLine()
   app.cmdloop()