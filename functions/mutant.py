import re

from flask import json

from models import Adn, db


def verificar(str):
    pattern = '^[ACGT]*$'
    flag = False
    for pat in str:
        if (re.match(pattern, pat)):
            flag = True
        else:
            return False
    return flag


def vertical(matrix):
    result = 0
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            try:
                if (matrix[i][j] == matrix[i + 1][j]) & (matrix[i + 1][j] == matrix[i + 2][j]) & (
                        matrix[i + 2][j] == matrix[i + 3][j]):
                    result += 1
            except IndexError:
                pass
    return result


def horizontal(matrix):
    result = 0
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            try:
                if (matrix[i][j] == matrix[i][j + 1]) & (matrix[i][j + 1] == matrix[i][j + 2]) & (
                        matrix[i][j + 2] == matrix[i][j + 3]):
                    result += 1
            except IndexError:
                pass
    return result


def diagonal(matrix):
    result = 0
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            try:
                if (matrix[i][j] == matrix[i + 1][j + 1]) & (matrix[i + 1][j + 1] == matrix[i + 2][j + 2]) & (
                        matrix[i + 2][j + 2] == matrix[i + 3][j + 3]):
                    result += 1
            except IndexError:
                pass
    return result


def diagOne(matrix):
    result = 0
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            try:
                if (matrix[i - 1][j + 1] == matrix[i - 2][j + 2]) & (matrix[i - 2][j + 2] == matrix[i - 3][j + 3]) & (
                        matrix[i - 3][j + 3] == matrix[i][j]):
                    result += 1
            except IndexError:
                pass
    return result


def isMutant(matrix):
    result = horizontal(matrix)
    if horizontal(matrix) < 2:
        result += vertical(matrix)
    if result < 2:
        result += diagonal(matrix)
    if result < 2:
        result += diagOne(matrix)
    if result < 2:
        saveAdn(matrix, 2)
        return False
    saveAdn(matrix, 1)
    return True


def saveAdn(data, type):
    if (exist(data)):
        adn = Adn()
        adn.adn = json.dumps(data)
        adn.type_id = type
        db.session.add(adn)
        db.session.commit()
        db.session.flush()
        return True
    else:
        return False


def exist(data):
    dbdata=Adn.query.filter_by(adn=json.dumps(data)).first()
    if (dbdata == None):
        return True
    else:
        return False
