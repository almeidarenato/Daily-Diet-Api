from flask import Flask, request, jsonify
from database import db
from models.user import User
from models.meal import Meal

app = Flask(__name__)
app.config['SECRET_KEY'] = "developers_paradise"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:admin123@127.0.0.1:3306/diet-api"

db.init_app(app)


@app.route("/meals",methods=['POST'])
def create_meal():
    data = request.json
    name = data.get("nome")
    description = data.get("descricao")
    date_time = data.get("data_hora")
    inside_diet = data.get("dentro_da_dieta")
    user_id = int(data.get("usuario"))

    if name and description and date_time and user_id:
        user = User.query.filter_by(id=user_id).first()
        if user:
            meal = Meal(name=name,description=description,date_time=date_time,inside_diet=inside_diet,user_id=user.id)
            db.session.add(meal)
            db.session.commit()
            return jsonify({"message": "Refeição cadastrada com sucesso"}), 200
    return jsonify({"message":"Dados invalidos"}), 401

@app.route("/meals/<int:id_meal>",methods=['PUT'])
def update_meal(id_meal):
    data = request.json
    name = data.get("nome")
    description = data.get("descricao")
    date_time = data.get("data_hora")
    inside_diet = data.get("dentro_da_dieta")
    user_id = int(data.get("usuario"))
    if id_meal :
        meal = Meal.query.get(id_meal) 
        user = User.query.get(user_id)
        if user is None :
            return jsonify({"message": f"Usuário {user_id} não encontrado" })
        if meal is None: 
            return jsonify({"message": f"Refeição {id_meal} não encontrada" })
        if  name and description and date_time:
            meal.name = name
            meal.description = description
            meal.date_time = date_time
            meal.inside_diet = inside_diet
            meal.user_id = user_id 
            db.session.commit()
            return jsonify({"message":f"Refeição {id_meal} atualizada com sucesso "}), 200
        return jsonify({"message": "Dados incompletos"}), 404
    
    return jsonify({"message":"Dados invalidos"}), 401

@app.route("/meals/<int:id_meal>",methods=['DELETE'])
def delete_meal(id_meal):
    meal = Meal.query.get(id_meal)
    if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message":f"Refeição {id_meal} deletada com sucesso"}),200
    return jsonify({"message":f"Refeição {id_meal} não encontrada" }), 404

@app.route("/meals/<int:user_id>",methods=['GET'])
def get_user_meals(user_id):
    meals = Meal.query.filter(user_id==user_id).all()
    if meals:
        meal_data = [{"id": meal.id,
                    "nome": meal.name,
                    "descrição": meal.description,
                    "data_hora": meal.date_time,
                    "dentro_dieta": meal.inside_diet,
                    "id_usuario": meal.user_id,
                    "usuario": meal.user.username} for meal in meals]
        return jsonify({"message":meal_data}), 200
    return jsonify({"message": "Refeição não encontrada"}),404

@app.route("/meal/<int:id_meal>",methods=['GET'])
def get_meal(id_meal):
    meal = Meal.query.get(id_meal)
    if meal:
        return jsonify({"meal":{
            "nome": meal.name,
                    "descrição": meal.description,
                    "data_hora": meal.date_time,
                    "dentro_dieta": meal.inside_diet,
                    "id_usuario": meal.user_id,
                    "usuario": meal.user.username
        }}), 200
    return jsonify({"message": "Refeição não econtrada"}),404

if __name__ == '__main__':
    app.run(debug=True)