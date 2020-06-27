#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ exit command """
        return True

    def help_quit(self):
        """ quit documentation """
        print("Quit command to exit the program")

    def do_EOF(self, line):  # cucho, este es para cuando se salga con control+d no tire error
        """ ctr+D signal handler """
        print("")
        return True

    def help_EOF(self):
        """ EOF documentation """
        print("Handle the ctr+D signal to avoid errors")

    def emptyline(self):
        """ show the prompt when an empty line typed in
        it avoid repeats the last nonempty command entered
        """
        # y esta maricada es necesaria para que no se ejecute el comando anterior cuando uno presiona enter
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
