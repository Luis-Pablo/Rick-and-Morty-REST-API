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

            return jsonify({'message':'Personaje eliminado', 'character': character.serialize()}), 200
        else:            
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
            
            return jsonify({'message':'Personaje actualizado', 'character': character.serialize()}), 200
    
    return jsonify("Personaje no encontrado"), 418


# LOCATION


@app.route("/location", methods=["POST"])
def create_location():
    location = Location()
    location.name = request.json.get("name")
    location.type = request.json.get("type")
    location.dimension = request.json.get("dimension")
    location.residents = request.json.get("residents")

    db.session.add(location)
    db.session.commit()

    return jsonify({'message':'Ubicación creada exitosamente ', 'location': location.serialize()}), 200



@app.route("/location", methods=["GET"])
def get_location():
    locations = Location.query.all()
    result = []
    for location in locations:
        result.append(location.serialize())
    return jsonify(result)


@app.route("/location/<int:id>", methods=["PUT", "DELETE"])
def update_location(id):
    location = Location.query.get(id)
    if location is not None:
        if request.method == "DELETE":
            db.session.delete(location)
            db.session.commit()

            return jsonify({'message':'Ubicación eliminada', 'location': location.serialize()}), 200
        else:            
            location.name = request.json.get("name")
            location.type = request.json.get("type")
            location.dimension = request.json.get("dimension")
            location.residents = request.json.get("residents")
        
            

            db.session.add(location)
            db.session.commit()

            
            return jsonify({'message':'Ubicación actualizada', 'location': location.serialize()}), 200
    
    return jsonify("location no encontrada"), 418







# EPISODES



@app.route("/episodes", methods=["POST"])
def create_episodes():
    episodes = Episode()
    episodes.name = request.json.get("name")
    episodes.air_date = request.json.get("air_date")
    episodes.episode = request.json.get("episode")
    episodes.character = request.json.get("character")

    db.session.add(episodes)
    db.session.commit()

    return jsonify({'message':'Episodio creado exitosamente ', 'episodes': episodes.serialize()}), 200



@app.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    result = []
    for episode in episodes:
        result.append(episode.serialize())
    return jsonify(result)


@app.route("/episodes/<int:id>", methods=["PUT", "DELETE"])
def update_episodes(id):
    episodes = Episode.query.get(id)
    if episodes is not None:
        if request.method == "DELETE":
            db.session.delete(episodes)
            db.session.commit()

            return jsonify({'message':'Episodio eliminado', 'episodes': episodes.serialize()}), 200
        else:            
            episodes.name = request.json.get("name")
            episodes.air_date = request.json.get("air_date")
            episodes.episode = request.json.get("episode")
            episodes.character = request.json.get("character")
        
            

            db.session.add(episodes)
            db.session.commit()

            
            return jsonify({'message':'Episodio actualizado', 'episodes': episodes.serialize()}), 200
    
    return jsonify("Episodio no encontrado"), 418



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