from flask import Flask,request, jsonify
from models import db, User, Character, Favorite, Episode, Location
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rick_and_morty.db'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/user')
def index():
    return 'hola'

@app.route("/users", methods=["POST"])
def create_user():
    user = User()
    user.username = request.json.get("username")
    user.password = request.json.get("password")
    
    user_name = User.query.filter_by(username = user.username).first()
   
    if user_name:
        return jsonify ({'message':'Usuario ya existe', 'user_name': user_name.serialize()}), 200    
    else:
        db.session.add(user)
        db.session.commit()

        return jsonify ({'message':'Usuario guardados', 'user' : user.serialize()}), 200
 

@app.route("/users/<int:id>", methods=["PUT", "DELETE"])
def update_user(id):
    user = User.query.get(id)
    
    if request.method == "DELETE":
        db.session.delete(user)
        db.session.commit()

        return jsonify({'message':'Eliminado', 'user' : user.serialize()}), 200
    
    if request.method == "PUT":          
        user.username = request.json.get("username")
        user.password = request.json.get("password")
                         
        db.session.commit()
            
        return jsonify({'message':'Usuario actualizado', 'user' : user.serialize()}), 200
    

        




# CHARACTER

@app.route("/characters", methods=["POST"])
def create_character():
    character = Character()
    character.name = request.json.get("name")
    character.status = request.json.get("status")
    character.species = request.json.get("species")
    character.type = request.json.get("type")
    character.gender = request.json.get("gender")
    character.origin = request.json.get("origin")
    character.location = request.json.get("location")
    character.episode = request.json.get("episode")
    

    db.session.add(character)
    db.session.commit()

    return jsonify({'message':'Personaje creado exitosamente ', 'character_name': character.serialize()}), 200



@app.route("/characters", methods=["GET"])
def get_characters():
    characters = Character.query.all()
    result = []
    for character in characters:
        result.append(character.serialize())
    return jsonify(result)


@app.route("/characters/<int:id>", methods=["PUT", "DELETE"])
def update_characters(id):
    character = Character.query.get(id)
    if character is not None:
        if request.method == "DELETE":
            db.session.delete(character)
            db.session.commit()

            return jsonify("Personaje Eliminado"), 204
        else:
            character.patronus = request.json.get("patronus")
            
            db.session.commit()
            
            return jsonify("Personaje actualizado"), 200
    
    return jsonify("Personaje no encontrado"), 418





# FAVORITES

@app.route("/favorites", methods=["POST"])
def create_favorite():
    favorite = Favorite()
    favorite.username = request.json.get("username")
    favorite.name_character = request.json.get("name_character")
    
    favorite_name = Favorite.query.filter_by(name_character = favorite.name_character).first()
    
    if favorite_name:
        return jsonify({'message':'Favorito ya existe ', 'favorite': favorite.serialize()})
    else:       
        db.session.add(favorite)
        db.session.commit()

        return jsonify({'message':'Favorito guardado', 'favorite': favorite.serialize()}), 200

@app.route("/favorites", methods=["GET"])
def get_favorites():
    favorites = Favorite.query.all()
    result = []
    for favorite in favorites:
        result.append(favorite.serialize())
    return jsonify(result)



@app.route("/favorites/<int:id>", methods=["PUT", "DELETE"])
def update_favorite(id):
    favorite = Favorite.query.get(id)
    
    if request.method == "DELETE":
        db.session.delete(favorite)
        db.session.commit()

        return jsonify({'message':'Favorito eliminado', 'favorite': favorite.serialize()}), 200
    
    if request.method == "PUT":
        favorite.name_character = request.json.get("name_character")
        db.session.commit()
        return jsonify({'message':'Favorito actualizado', 'favorite': favorite.serialize()}), 200
                       
    
 
                        
    
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()