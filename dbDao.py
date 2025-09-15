from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import bcrypt

class AuthennticationDAO:
    def __init__(self):
        mongourl = "mongodb+srv://sbcreations:sbcreations@cluster0.ao6t0sl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        mongodb = AsyncIOMotorClient(mongourl)
        client = mongodb['pockerbank']
        self.userCollection = client['users']
        self.tasksCollection = client["daybank"]
    
    def encryptPwd(self,password):
        salt = bcrypt.gensalt()
        encpwd = bcrypt.hashpw(password.encode('utf-8'),salt=salt)
        return encpwd.decode('utf-8')

    def verifyPwd(self,pwd,hashedpwd):
        verify = bcrypt.checkpw(pwd.encode('utf-8'),hashedpwd.encode('utf-8'))
        return verify

    async def register(self,userRegiData):
        try:
            res = await self.userCollection.find_one({'userid':userRegiData['userid']})
            if res:
                print(f"User with id {userRegiData['userid']} already exist")
                return (f"User with id {userRegiData['userid']} already exist")
            userRegiData['password'] = self.encryptPwd(userRegiData['password'])
            res = await self.userCollection.insert_one(userRegiData)
            if res['acknowledged']:
                res = {
                    "name":userRegiData['name'],
                    "userid":userRegiData['userid']}
                print(f"Registration success {res}")
                return res
        except Exception as e:
            print(f"Registration error: {e}")

    async def login(self,userLoginData):
        try:
            res = await self.userCollection.find_one({'userid':userLoginData['userid']})
            ver = self.verifyPwd(userLoginData['password'],res['password'])
            if ver:
                res = {
                    "success":True,
                    "name":res['name'],
                    "userid":res['userid']}
                print(f"login success {res}")
                return res
        except Exception as e:
            print(f"login error: {e}")


async def main():
    auth = AuthennticationDAO()
    await auth.register(userRegiData={
        "name":"test1",
        "phoneno":"7894561230",
        "userid":"test789",
        "password":"123456",
        "role":"admin"
    })

    await auth.login({
        "userid":"test789",
        "password":"123456"
    })


# if __name__ == "__main__":
#     asyncio.run(main())