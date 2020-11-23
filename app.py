from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bootstrap import Bootstrap

# Init app
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost:5432/transportesjr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# set default button sytle and size, will be overwritten by macro parameters
app.config['BOOTSTRAP_BTN_STYLE'] = 'primary'
app.config['BOOTSTRAP_BTN_SIZE'] = 'sm'
bootstrap = Bootstrap(app)

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# settings
app.secret_key = "mySecretKey"


class VehiculoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'placa', 'marca', 'linea', 'modelo', 'color', 'numero_ejes', 'tipo_motor', 'numero_motor',
                  'tipo_diferencial', 'tipo_caja')


# Init schema
vehiculo_schema = VehiculoSchema()
vehiculos_schema = VehiculoSchema(many=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/servicios")
def servicios():
    return render_template("servicios.html")


@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")


@app.route("/acceder")
def acceder():
    return render_template("acceder.html")


@app.route("/crearCuenta")
def crearCuenta():
    return render_template("crearCuenta.html")


# Crear vehiculo
@app.route("/vehiculo", methods=["POST"])
def add_vehiculo():
    from model import Tractocamion
    numero_matricula = request.json["numero_matricula"]
    marca = request.json["marca"]
    modelo = request.json["modelo"]
    color = request.json["color"]
    numero_ejes = request.json["numero_ejes"]
    tipo_motor = request.json["tipo_motor"]
    numero_motor = request.json["numero_motor"]
    tipo_diferencial = request.json["tipo_diferencial"]
    tipo_caja = request.json["tipo_caja"]

    new_vehiculo = Tractocamion(numero_matricula=numero_matricula, marca=marca, modelo=modelo, color=color,
                                numero_ejes=numero_ejes, tipo_motor=tipo_motor, numero_motor=numero_motor,
                                tipo_diferencial=tipo_diferencial, tipo_caja=tipo_caja)

    db.session.add(new_vehiculo)
    db.session.commit()

    return vehiculo_schema.jsonify(new_vehiculo)


# Get all vehiculos
@app.route("/vehiculo", methods=["GET"])
def get_vehiuculos():
    from model import Tractocamion
    all_vehiculos = Tractocamion.query.all()
    result = vehiculos_schema.dump(all_vehiculos)
    return render_template("tractocamion.html", vehiculos=all_vehiculos)


# Get one vehiculo
@app.route("/vehiculo/<id>", methods=["GET"])
def get_vehiculo(id):
    from model import Tractocamion
    vehiculo = Tractocamion.query.get(id)

    return render_template("tractocamion.html", vehiculo=vehiculo)


# Update a vehiculo
@app.route("/vehiculo/<id>", methods=["PUT"])
def update_vehiuculo(id):
    from model import Tractocamion
    vehiculo = Tractocamion.query.get(id)

    numero_matricula = request.json["numero_matricula"]
    marca = request.json["marca"]
    modelo = request.json["modelo"]
    color = request.json["color"]
    numero_ejes = request.json["numero_ejes"]
    tipo_motor = request.json["tipo_motor"]
    numero_motor = request.json["numero_motor"]
    tipo_diferencial = request.json["tipo_diferencial"]
    tipo_caja = request.json["tipo_caja"]

    vehiculo.placa = numero_matricula
    vehiculo.marca = marca
    vehiculo.modelo = modelo
    vehiculo.color = color
    vehiculo.numero_ejes = numero_ejes
    vehiculo.tipo_motor = tipo_motor
    vehiculo.numero_motor = numero_motor
    vehiculo.tipo_diferencial = tipo_diferencial
    vehiculo.tipo_caja = tipo_caja

    db.session.commit()
    return vehiculo_schema.jsonify(vehiculo)


# Delete a vehiculo
@app.route("/vehiculo/<id>", methods=["DELETE"])
def delete_vehiculo(id):
    from model import Tractocamion
    vehiculo = Tractocamion.query.get(id)
    db.session.delete(vehiculo)
    db.session.commit()

    return vehiculo_schema.jsonify(vehiculo)


if __name__ == '__main__':
    app.run(port=9000, debug=False)
