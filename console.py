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
        args = arg.split()
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
                del storage.all()[key]
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
        if not arg:
            instances = [str(obj) for obj in storage.all().values()]
            print(instances)
        elif "." in arg:
            class_name, method_name = arg.split(".")
            if method_name == "all()":
                if class_name in classes:
                    instances = [
                        str(obj)
                        for obj in storage.all().values()
                        if obj.__class__.__name__ == class_name
                    ]
                    print(instances)
                else:
                    print("** class doesn't exist **")
            else:
                print("** Unknown syntax: {}".format(arg))

        elif arg in classes:
            instances = [
                str(obj)
                for obj in storage.all().values()
                if obj.__class__.__name__ == arg
            ]
            print(instances)
        else:
            print("** class doesn't exist **")

    def default(self, arg):
        """
        Called when the command prefix is not recognized.
        It handles the syntax:
            `<class_name>.all()` to retrieve all instances of a class.
            `<class_name>.count()` to retrieve the number
            of instances of a class.
            `<class_name>.show(<id>)` to retrieve an instance based on its ID.
        """
        args = arg.split(".")
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print(f"*** Unknown syntax: {arg}")
            return

        method_name = args[1].split("(")[0]
        if method_name == "all":
            instances = [
                str(obj) for obj in storage.all().values()
                if obj.__class__.__name__ == class_name
            ]
            print(instances)
        elif method_name == "count":
            count = sum(
                1 for obj in storage.all().values()
                if obj.__class__.__name__ == class_name
            )
            print(count)
        elif method_name == "show":
            obj_id = args[1].split("(")[1].split(")")[0]
            key = f"{class_name}.{obj_id}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        elif method_name == "destroy":
            obj_id = args[1].split("(")[1].split(")")[0]
            key = f"{class_name}.{obj_id}"
            if key in storage.all():
                storage.all().pop(key)
            else:
                print("** no instance found **")
        elif method_name == "update":
            args_list = args[1].split("(")[1].split(")")[0].split(", ")
            obj_id = args_list[0]
            key = f"{class_name}.{obj_id}"
            if key in storage.all():
                obj = storage.all()[key]
                if len(args_list) == 2:
                    try:
                        attr_dict = eval(args_list[1])
                    except (NameError, SyntaxError):
                        print("** Invalid syntax **")
                        return
                    for attr_name, attr_value in attr_dict.items():
                        setattr(obj, attr_name, attr_value)
                elif len(args_list) == 3:
                    attr_name, attr_value = args_list[1], args_list[2]
                    setattr(obj, attr_name, attr_value)
            else:
                print("** no instance found **")

        else:
            print(f"*** Unknown syntax: {arg}")

    def do_update(self, arg):
        """
        This method updates an instance based on the class name and id
        and saves the chnage to a JSON file.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
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
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                instance_class = instance.__class__
                attribute_types = {
                    attr: type(getattr(instance_class, attr))
                    for attr in dir(instance_class)
                    if not callable(getattr(instance_class, attr))
                       and not attr.startswith("__")
                }
                attr_type = attribute_types.get(args[2], str)
                try:
                    attr_type(args[3].strip('"'))
                except ValueError:
                    print("** value is invalid **")
                else:
                    setattr(instance, args[2], args[3].strip('"'))
                    instance.save()

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class.
        Usage: <class name>.count()
        """
        args = arg.split(" ")
        if not arg[0]:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            instances = [obj for obj in storage.all()
                         if obj.startswith(args[0] + '.')]
            print(len(instances))

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
