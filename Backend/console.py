#!/usr/bin/env python3

import cmd
# from models.basemodel import BaseModel
from models import User, Admin

obdict = {
    'user': User,
    'admin': Admin
}

class Console(cmd.Cmd):
    def do_greet(self, line):
        args = self.lister(line)
        print(f'hello {args}')
    
    def do_EOF(self, line):
        return True


    def do_create(self, line):
        """create an obj"""
        args = self.lister(line)
        if len(args) < 1 or args[0] not in obdict:
            print('admin or user')
            return
        if len(args) < 4 :
            print('ongeza args bana')
        cls, name, age , username = args
        obj = obdict[cls](name, age, username)
        obj.save()
        print(obj)
        
        
    
    @staticmethod
    def lister(line: str) -> list:
        """slit line to list args"""
        return line.split(' ')



if __name__ == '__main__':
    Console().cmdloop()
