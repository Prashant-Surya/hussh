import os

class User(object):
    def create_user(self, username, password):
        raise NotImplementedError
    def delete_user(self, username):
        raise NotImplementedError

class LinuxUser(User):
    def create_user(self, username, password):
        command = "sudo useradd -m -p {password} {username}".format(
            username, password)
        os.system(command)
    def delete_user(self, username):
        command = "sudo userdel -r {username}".format(username)
        os.system(command)