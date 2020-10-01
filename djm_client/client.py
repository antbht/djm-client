from cmd import Cmd

USER_ID='0302'
SEPARATOR="==================\n\n"
SEPARATOR2="----\n\n"

class MainCmdLine(Cmd):

   intro = f"\nWelcome to your digitalized wallet !\n\n{SEPARATOR}Your USER_ID is {USER_ID}.\n\n{SEPARATOR}Type help or ? to have more information about your possibilities\n"

   prompt = "wallet > "

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


if __name__ == '__main__':
   app = MainCmdLine()
   app.cmdloop()