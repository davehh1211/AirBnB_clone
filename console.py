#!/usr/bin/python3

import shlex
import cmd
import models
from models.base_model import BaseModel
from models import storage



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

    def do_create(self, line):
        if len(line) <= 0:
            print("** class name missing **")
        elif line not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            base_obj = BaseModel()
            print(base_obj.id)
            base_obj.save()

    def help_create(self):
        """ EOF documentation """
        print("Handle the ctr+D signal to avoid errors")

    def do_show(self, line):
        args = []
        args = line.split()
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        elif objects.get(args[0]+"."+args[1]) is not None:
            print(objects.get(args[0]+"."+args[1]))
        else:
            print("** no instance found **")

    def help_show(self):
        """ EOF documentation """
        print("Handle the ctr+D signal to avoid errors")
    
    def do_destroy(self, line):
        args = line.split()
        args = line.split()
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] in objects:
            del objects[args[0]+'.'+args[1]]
        else:
            print("** no instance found **")

    def do_all(self, line):
        objs = []
        args = line.split()
        objects = storage.all()
        if len(args) <= 0 or args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            for key in objects:
                objs.append(objects[key].__str__())
            print(objs)

    def do_update(self, line):
        args = []
        args = shlex.split(line)
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif objects.get(args[0]+"."+args[1]) is None:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = objects.get(args[0]+"."+args[1])
            setattr(obj, args[2], args[3])
            obj.save()

    def emptyline(self):
        """ show the prompt when an empty line typed in
        it avoid repeats the last nonempty command entered
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
