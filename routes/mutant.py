from flask import render_template, session, flash, request, json, jsonify, abort

from functions.mutant import verificar, horizontal, vertical, diagOne, diagonal, isMutant
from models import Adn
from . import routes

#este es el endpoint donde hay una landing mas linda para que no quede tan vacio
#Iba hacer un login pero no iba a perder tiempo en esto. que no estaba pedido
@routes.route('/')
def home():
    return render_template('main.html')

#endpoint mutant , donde verifica que exista el patron de letras y recien ahi verifica el adn
@routes.route("/mutant/", methods=["POST"])
def ismutant():
    if request.is_json:
        content = request.get_json()
        if (verificar(content["dna"])):
            if (isMutant(content["dna"])):
                return jsonify({'status': 200, 'response': ' MUTANT '})
            else:
                return abort(403, description="HUMAN")
        else:
            return abort(403, description="PATTERN WRONG")
    return abort(403, description="JSON ERROR")

#endpoint de las estadisticas primero toma lo dos datos desde la db y lugo calcula el ratio , si el divisor es 0 se le asig el valor de no data
@routes.route("/stats/", methods=["POST"])
def stats():
    mutants = Adn.query.filter_by(type_id=1).count()
    humans = Adn.query.filter_by(type_id=2).count()
    if humans == 0:
        ratio = "NO DATA"
    else:
        ratio = mutants / humans
    return jsonify({"count_mutant_dna": mutants, "count_human_dna": humans, "ratio": ratio})
