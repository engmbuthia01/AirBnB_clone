#!/usr/bin/python3
"""
contains the entry point of the
command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    command line
    interface
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """exits the program"""
        return True

    def help_quit(self, arg):
        """quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """end of file"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
