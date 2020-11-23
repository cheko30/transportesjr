from app import db


class Vehiculo(db.Model):
    __tablename__ = "vehiculo"

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(7), unique=True, nullable=False)
    marca = db.Column(db.String(256), nullable=True)
    modelo = db.Column(db.String(256), nullable=True)
    color = db.Column(db.String(256), nullable=True)
    # numero_ejes = db.Column(db.Integer, nullable=True)
    tipo_motor = db.Column(db.String(256), nullable=True)
    numero_motor = db.Column(db.String(256), nullable=True)
    # tipo_diferencial = db.Column(db.String(256), nullable=True)
    tipo_caja = db.Column(db.String(256), nullable=True)

    def __init__(self, numero_matricula, marca, modelo, color, tipo_motor, numero_motor, tipo_caja):
        self.placa = numero_matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        # self.numero_ejes = numero_ejes
        self.tipo_motor = tipo_motor
        self.numero_motor = numero_motor
        # self.tipo_diferencial = tipo_diferencial
        self.tipo_caja = tipo_caja


class Tractocamion(Vehiculo):
    """Constructor clase Tractocamion"""

    def __init__(self, numero_matricula, marca, modelo, color, tipo_motor, numero_motor, tipo_caja,
                 numero_ejes, tipo_diferencial):
        """Constructor clase Vehiculo"""
        Vehiculo.__init__(self, numero_matricula, marca, modelo, color, tipo_motor, numero_motor, tipo_caja)

        self.numero_ejes = numero_ejes
        self.tipo_diferencial = tipo_diferencial
