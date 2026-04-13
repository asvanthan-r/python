from abc import ABC, abstractmethod

class Userrepo(ABC):
    @abstractmethod
    def get_user(self):
        pass

class MySqlDatabase(Userrepo):
    def get_user(self, userid):
        print(userid)
class InMemoryData(Userrepo):
    def get_user(self, userid):
        print("memory db ", userid)
class UserService:
    def __init__(self, user_repo:Userrepo):
        self.user_repo = user_repo
    def get_user(self, userid):
        self.user_repo.get_user(userid)

repo = InMemoryData()
service = UserService(repo)
service.get_user("aa")