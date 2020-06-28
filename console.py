#!/usr/bin/python3

import shlex
import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ exit command """
        return True

    def help_quit(self):
        """ quit documentation """
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """ ctr+D signal handler """
        print("")
        return True

    def help_EOF(self):
        """ EOF documentation """
        print("Handle the ctr+D signal to avoid errors")

    def do_create(self, line):
        args = line.split()
        classes = ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]
        if len(args) <= 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj = eval(args[0])()
            print(obj.id)
            obj.save()

    def help_create(self):
        """ EOF documentation """
        print("Handle the ctr+D signal to avoid errors")

    def do_show(self, line):
        args = []
        args = line.split()
        objects = storage.all()
        classes = ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
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
        classes = ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] in objects:
            del objects[args[0]+'.'+args[1]]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        objs = []
        args = line.split()
        objects = storage.all()
        classes = ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]
        if len(args) <= 0 or args[0] not in classes:
            print("** class doesn't exist **")
        else:
            keys = objects.keys()
            for key in keys:
                class_name = key.split(".")
                if class_name[0] == args[0]:
                    objs.append(objects[key].__str__())
            print(objs)

    def do_update(self, line):
        args = []
        args = shlex.split(line)
        objects = storage.all()
        classes = ["BaseModel", "Amenity", "City", "Place", "Review", "State", "User"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
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
