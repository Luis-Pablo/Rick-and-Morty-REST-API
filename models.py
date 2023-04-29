from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    

    def serialize(self):
        return {
            "username": self.username,
            "id": self.id,
            
        }

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),)
    status = db.Column(db.String(50), )
    species = db.Column(db.String(50), )
    type = db.Column(db.String(50),)
    gender = db.Column(db.String(50),)
    origin = db.Column(db.String(50),)
    location = db.Column(db.String(50),)
    episode = db.Column(db.Integer)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "type": self.type,
            "gender": self.gender,
            "origin": self.origin,
            "location": self.location,
            "episode": self.episode,
        }
        

class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    dimension = db.Column(db.String(50))
    residents = db.Column(db.String(50), db.ForeignKey('character.name'))
    
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "dimension": self.dimension,
            "residents": self.residents,
            
        }
        
class Episode(db.Model):
    __tablename__ = 'episode'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    air_date = db.Column(db.String(50), nullable=False)
    episode = db.Column(db.String(50))
    character = db.Column(db.String(50), db.ForeignKey('character.name'))
    
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "air_date": self.air_date,
            "episode": self.episode,
            "character": self.character,
            
        }
    
class Favorite(db.Model):
    __tablename__= 'favorite'
    id = db.Column (db.Integer, primary_key=True)
    username = db.Column(db.Integer, db.ForeignKey('user.id'))
    name_character = db.Column (db.String(50), db.ForeignKey('character.name'))
    
    def serialize(self):
        return {
            "username": self.username,
            "character_name": self.name_character            
        }