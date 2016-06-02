from system.core.model import *
import re  

class Model(Model):
    def __init__(self):
        super(Model, self).__init__()
    def register(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')
        errors = []
        if len(info['name']) < 2 :
            errors.append("Name can not be blank")
        if len(info['alias']) < 2 or not info['alias'].isalpha():
            errors.append("Invalid alias. (Letters only, at least 2 characters.)")
        if len(info['email']) < 1 or not EMAIL_REGEX.match(info['email']):
            errors.append ("Invalid Email Address!")
        if len(info['birthday']) < 1:
            errors.append("Enter your Date of birth")        
        if len(info['password']) < 8 :
            errors.append("Password should be more than 8 characters")
        if info['password'] != info['confirm_password']:
            errors.append('Password and confirm password must match!')
        if PASSWORD_REGEX.match(info['confirm_password']):
            errors.append("Password requires to have at least 1 uppercase letter and 1 numeric value ")   
        if errors:
            return {"status":False, "errors":errors}            
        else: 
            query = "INSERT INTO users (name, alias, email, password, birthday, created_at, updated_at) VALUES (:name, :alias, :email,  :pw_hash,:birthday, NOW(), NOW())" 
            data = {'name' : info['name'],'alias' : info['alias'],'email' : info['email'],'pw_hash' : self.bcrypt.generate_password_hash(info['password']),'birthday' : info['birthday']}
            self.db.query_db(query, data)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return {"status": True, "user": users[0]}
    def login(self,info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')
        errors = []
        if len(info['email']) < 1 or not EMAIL_REGEX.match(info['email']):
            errors.append ("Invalid Email Address!")    
        if len(info['password']) < 8 :
            errors.append("Password should be more than 8 characters")
        if errors:
            return {"status":False, "errors":errors}            
        else:  
            query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            data = {'email' : info['email']}
            users = self.db.query_db(query,data) 
            return {"status": True, "user": users[0]}
    def poked_me(self,id):
        query = "SELECT name, COUNT(poster_id) AS total, user_id FROM users LEFT JOIN pokes ON pokes.poster_id = users.id WHERE user_id = :id GROUP BY name ORDER BY total desc;"
        data = {
            'id': id
        }
        return self.db.query_db(query, data)
    def total_poked(self, id):
        query = "SELECT COUNT(DISTINCT(poster_id)) AS total FROM pokes LEFT JOIN users ON users.id = pokes.user_id WHERE users.id = :id"
        data = {
            'id': id
        }
        return self.db.query_db(query, data)

    def show_poked(self):
        query = "SELECT users.id as id, name, alias, email ,COUNT(poster_id) AS total FROM users LEFT JOIN pokes ON pokes.user_id = users.id GROUP BY name"
        return self.db.query_db(query)
    def poke_user(self, user_id, poster_id):
        query = "INSERT INTO pokes ( user_id, poster_id) VALUES ( :user_id, :poster_id)"
        data = {
            'user_id': user_id,
            'poster_id': poster_id
        }
        return self.db.query_db(query, data)


