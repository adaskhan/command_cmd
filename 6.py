import os
import cmd


class MyCmd(cmd.Cmd):
    prompt = ">>>"

    def do_ls(self, args):
        ''' list files in current directory '''
        print(os.listdir())

    def do_cd(self, args):
        ''' change directory '''
        try:
            os.chdir(args)
        except FileNotFoundError:
            raise Exception("Directory not found")

    def do_mkdir(self, args):
        ''' create new directory '''
        os.mkdir(args)

    def do_rmdir(self, args):
        ''' remove directory '''
        os.rmdir(args)

    def do_rename(self, args):
        ''' rename file '''
        old_name, new_name = args.split()
        os.rename(old_name, new_name)

    def do_exit(self, args):
        ''' exit the program '''
        return True


if __name__ == '__main__':
    MyCmd().cmdloop()
