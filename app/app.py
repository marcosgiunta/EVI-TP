from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)
conexion = MySQL(app)


@app.route('/tareas', methods=['GET'])
def listar_tareas():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM tareas"
        cursor.execute(sql)
        datos = cursor.fetchall()
        tareas = []
        for fila in datos:
            tarea = {
                'id': fila[0],
                'titulo': fila[1],
                'descripcion': fila[2],
                'estado': fila[3]
            }
            tareas.append(tarea)
        return jsonify({'tareas': tareas, 'mensaje': "Tareas listadas correctamente"})  
    except Exception as e:
        return jsonify({'mensaje': "Error al listar tareas", 'error': str(e)})
    

@app.route('/tareas/<estado>', methods=['GET'])
def listar_tareas_por_estado(estado):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM tareas WHERE estado = '{0}'".format(estado)
        cursor.execute(sql)
        datos = cursor.fetchall()
        if datos is not None:
            tareas = []
            for fila in datos:
                tarea = {
                    'id': fila[0],
                    'titulo': fila[1],
                    'descripcion': fila[2],
                    'estado': fila[3]  
                }
                tareas.append(tarea)
            return jsonify({'tareas': tareas, 'mensaje': "Tareas listadas correctamente"})
        else:
            return jsonify({'mensaje': "No existen tareas con ese estado"})
    except Exception as e:
        return jsonify({'mensaje': "Error al listar tareas", 'error': str(e)})


@app.route('/tarea/<int:id>', methods=['GET'])
def leer_tarea(id):
    try:
        cursor = conexion.connection.cursor()  
        sql = "SELECT * FROM tareas WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos is not None:  
            tarea = {
                'id': datos[0],
                'titulo': datos[1],
                'descripcion': datos[2],
                'estado': datos[3]
            }
            return jsonify({'tarea': tarea, 'mensaje': "Tarea encontrada correctamente"})
        else:
            return jsonify({'mensaje': "Tarea no encontrada"})
    except Exception as e:
        return jsonify({'mensaje': "Error al leer tarea", 'error': str(e)})


@app.route('/tarea', methods=['POST'])
def crear_tarea():
    try:
        cursor = conexion.connection.cursor()

        titulo = request.json['titulo']
        descripcion = request.json.get('descripcion', 'Sin descripcion')

        sql = "INSERT INTO tareas (titulo, descripcion) VALUES (%s, %s)"
        cursor.execute(sql, (titulo, descripcion))
        conexion.connection.commit()

        nuevo_id = cursor.lastrowid 

        return jsonify({
            'mensaje': "Tarea creada correctamente",
            'id': nuevo_id
        }), 201

    except Exception as e:
        return jsonify({
            'mensaje': "Error al crear tarea",
            'error': str(e)
        }), 500



@app.route('/tarea/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    try:  
        cursor = conexion.connection.cursor()
        sql_verificar = "SELECT * FROM tareas WHERE id = '{0}'".format(id)
        cursor.execute(sql_verificar)
        datos = cursor.fetchone()
        if datos is not None:
            sql = "DELETE FROM tareas WHERE id = '{0}'".format(id)
            cursor.execute(sql)
            conexion.connection.commit()
            return jsonify({'mensaje': "Tarea eliminada correctamente"})
        else:
            return jsonify({'mensaje': "El id de la tarea no existe"})
    except Exception as e:
        return jsonify({'mensaje': "Error al eliminar tarea", 'error': str(e)})


@app.route('/tarea/<int:id>', methods=['PUT'])
def modificar_tarea(id):
    try:
        cursor = conexion.connection.cursor()
        sql_verificar = "SELECT * FROM tareas WHERE id = '{0}'".format(id)
        cursor.execute(sql_verificar)
        datos = cursor.fetchone()
        if datos is not None:
            sql = "UPDATE tareas SET titulo = '{0}', descripcion = '{1}', estado = '{2}' WHERE id = '{3}'".format(
                request.json['titulo'], request.json['descripcion'], request.json['estado'], id)
            cursor.execute(sql)
            conexion.connection.commit()
            return jsonify({'mensaje': "Tarea modificada correctamente"})
        else:
            return jsonify({'mensaje': "El id de la tarea no existe"})
    except Exception as e:
        return jsonify({'mensaje': "Error al modificar tarea", 'error': str(e)})

@app.route('/tarea/<int:id>/estado', methods=['PUT'])
def modificar_estado_tarea(id):
    try:
        nuevo_estado = request.json['estado']  
        estados_validos = ['ToDo', 'Doing', 'Done']
        if nuevo_estado not in estados_validos:
            return jsonify({'mensaje': "Estado no válido. Usa: ToDo, Doing o Done"})
        
        cursor = conexion.connection.cursor()
        sql_verificar = "SELECT * FROM tareas WHERE id = '{0}'".format(id)
        cursor.execute(sql_verificar)
        datos = cursor.fetchone()
        
        if datos is not None:
            sql = "UPDATE tareas SET estado = '{0}' WHERE id = '{1}'".format(nuevo_estado, id)
            cursor.execute(sql)
            conexion.connection.commit()
            return jsonify({'mensaje': "Tarea modificada correctamente"})
        else:
            return jsonify({'mensaje': "El id de la tarea no existe"})
    except Exception as e:
        return jsonify({'mensaje': "Error al modificar tarea", 'error': str(e)})

def pagina_no_encontrada(error):
    return "<h1>La página que buscas no existe</h1>", 404


if __name__ == '__main__':  
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='0.0.0.0', port=5000, debug=True)



