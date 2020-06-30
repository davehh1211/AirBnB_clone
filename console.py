#!/usr/bin/python3
"""Console module
"""
import shlex
import cmd
import models
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This console  that contains the entry
    point of the command interpreter:

    Args:
        cmd ([commandline]): [it receives the command]

    Returns:
        [True, False]: [depends on the outcome]
    """

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
        """create and instance and saves to json file"""
        args = line.split()
        classes = ["BaseModel", "Amenity", "City",
                   "Place", "Review", "State", "User"]
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
        """shows an instance based on the class name and id
        """
        args = []
        args = line.split()
        objects = storage.all()
        classes = ["BaseModel", "Amenity", "City",
                   "Place", "Review", "State", "User"]
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
        """Deletes an instance based on the class name and id
        """
        args = line.split()
        args = line.split()
        objects = storage.all()
        classes = ["BaseModel", "Amenity", "City",
                   "Place", "Review", "State", "User"]
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
        """Prints all string representation of
        all instances based or not on the class name.
        """
        objs = []
        args = line.split()
        objects = storage.all()
        classes = ["BaseModel", "Amenity", "City",
                   "Place", "Review", "State", "User"]
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
        """Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file)
        """
        args = []
        args = shlex.split(line)
        objects = storage.all()
        classes = ["BaseModel", "Amenity", "City",
                   "Place", "Review", "State", "User"]
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

    def precmd(self, line):
        """ search the command and executes it
        """
        if re.search(r'\(', line) is None:
            return line
        if re.search(r'\)', line) is None:
            return line
        line = line.replace('(', " ")
        line = line.replace(')', " ")
        if re.search(r'\.', line):
            line = line.replace('.', " ")
            line = line.split(" ")
            tmp = line[0]
            line[0] = line[1]
            line[1] = tmp
            line = " ".join(line)
        if re.search(r'\,', line):
            line = line.replace(", ", " ")
        if re.search(r'\,', line):
            line = line.replace(",", " ")
        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
