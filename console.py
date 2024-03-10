#!/usr/bin/python3
"""This contains entry point and methods of the command interpreter"""

import cmd

from models import storage

classes = storage.classes()


class HBNBCommand(cmd.Cmd):
    """
    The command interpreter class for AirBnB clone
    It inherits from the cmd module and provides methods
    for various commands
    """

    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        This method creates a new instance of the BaseModel
        and saves it to the JSON file.
        Usage: create <class name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_base_instance = classes[class_name]()  # globals()[class_name]()
        new_base_instance.save()
        new_base_instance_id = new_base_instance.id
        print(new_base_instance_id)

        # if class_name != 'BaseModel':
        #     print("** class doesnt' exist")
        #     return

        # new_base_instance = BaseModel()
        # new_base_instance_id = new_base_instance.id
        # new_base_instance.save()
        # print(new_base_instance_id)
        # print(new_base_instance.created_at)

    def do_show(self, arg):
        """
        This method prints the string representation of an instance
        based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split(" ", 1)

        if not arg:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")

        else:
            key = f"{args[0]}.{args[1]}"
            instance = storage.all().get(key)

            if not instance:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, arg):
        """
        This method deletes an instance based on class name and id
        then saves the chnages into the JSON file.
        Usage: destroy <class name> <id>
        """
        args = arg.split(" ", 1)
        if not arg:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print(" **instance id missing ** ")

        else:
            key = f"{args[0]}.{args[1]}"
            instance = storage.all().get(key)

            if not instance:
                print("** no instance found **")
            else:
                storage.delete(key)
                storage.save()
                # print(instance)

    def do_all(self, arg):
        """
        This method prints all the string representation of all instances
        Usage:
               all <class name>
               all
               <class name>.all()
        """
        class_name, method_name = arg.split(".")
        if method_name == "all()":
            if class_name in classes:
                instances = [str(obj) for obj in storage.all().values()
                             if obj.__class__.__name__ == class_name]
                print(instances)

        args = arg.split(".")
        if len(args) > 1 and args[1] == "all()":
            class_name = args[0]
            if class_name in classes:
                instances = [str(obj) for obj in storage.all().values()
                             if obj.__class__.__name__ == class_name]
                print(instances)
            else:
                print("** class doesn't exist")
        elif not arg:
            instances = [str(obj) for obj in storage.all().values()]
            print(instances)

        elif arg not in classes:
            print("** class doesn't exist")
        else:
            instances = [str(obj) for obj in storage.all().values()
                         if obj.__class__.__name__ == arg]
            print(instances)

    def default(self, arg):
        args = arg.split(".")
        if args[1] == "all()":
            if args[0] in classes:
                instances = [str(obj) for obj in storage.all().values()
                             if obj.__class__.__name__ == args[0]]
                print(instances)
            else:
                print("** class doesn't exist **")

        else:

            print(f"*** Unknown syntax: {arg}")

    def do_update(self, arg):
        """
        This method updates an instance based on the class name and id
        and saves the chnage to a JSON file.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split(" ", 1)
        if not arg:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print(" **instance id missing ** ")

        else:
            key = f"{args[0]}.{args[1]}"
            instance = storage.all().get(key)
            if not instance:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")

            else:
                setattr(instance, args[2], args[3].strip('"'))
                instance.save()

    def do_quit(self, line):

        """
        This command exits the program console
        Usage: quit
        """
        return True

    def do_EOF(self, line):

        """
        This command exits the program console
        Usage: EOF
        """
        return True

    def emptyline(self):

        """
        This does nothing when an empty line or ENTER is entered
        Usage: emptyline
        """
    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
