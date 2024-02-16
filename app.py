from flask import Flask, request, jsonify
from database import db
from models.user import User
from models.meal import Meal

app = Flask(__name__)
app.config['SECRET_KEY'] = "developers_paradise"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:admin123@127.0.0.1:3306/diet-api"

db.init_app(app)

@app.route("/test",methods=['GET'])
def test():
    return jsonify({"message": "Testing my app"}),200

if __name__ == '__main__':
    app.run(debug=True)