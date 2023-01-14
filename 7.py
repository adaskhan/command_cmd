import os
import cmd

roles = {
    "admin": ["ls", "cd", "mkdir", "rmdir", "rename", "exit"],
    "regular": ["ls", "cd", "exit"]
}


class MyCmd(cmd.Cmd):
    prompt = ">>>"

    current_user_role = "admin"

    def do_ls(self, args):
        ''' list files in current directory '''
        if "ls" in roles[self.current_user_role]:
            print(os.listdir())
        else:
            print("Permission denied")

    def do_cd(self, args):
        ''' change directory '''
        if "cd" in roles[self.current_user_role]:
            try:
                os.chdir(args)
            except FileNotFoundError:
                raise Exception("Directory not found")
        else:
            print("Permission denied")

    def do_mkdir(self, args):
        ''' create new directory '''
        if "mkdir" in roles[self.current_user_role]:
            os.mkdir(args)
        else:
            print("Permission denied")

    def do_rmdir(self, args):
        ''' remove directory '''
        if "rmdir" in roles[self.current_user_role]:
            os.rmdir(args)
        else:
            print("Permission denied")

    def do_rename(self, args):
        ''' rename file '''
        if "rename" in roles[self.current_user_role]:
            old_name, new_name = args.split()
            os.rename(old_name, new_name)
        else:
            print("Permission denied")

    def do_exit(self, args):
        ''' exit the program '''
        if "exit" in roles[self.current_user_role]:
            return True
        else:
            print("Permission denied")


if __name__ == '__main__':
    MyCmd.current_user_role = "admin"
    MyCmd().cmdloop()
