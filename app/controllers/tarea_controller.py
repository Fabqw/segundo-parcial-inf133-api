from flask import Blueprint, request, jsonify
from models.tarea_model import Tarea
from views.tarea_view import render_tarea_list, render_tarea_detail
from utils.decorators import jwt_required

tarea_db = Blueprint("tarea", __name__)

# Listar las todas tareas 
@tarea_db.route("/taks", methods=["GET"])
@jwt_required
def get_tareas():
    tareas = Tarea.get_all()
    return jsonify(render_tarea_list(tareas)), 200

# Mostrar una tarea por id
@tarea_db.route("/taks/<int:id>", methods=["GET"])
@jwt_required
def get_tarea(id):
    tarea = Tarea.get_by_id(id)
    if tarea:
        return jsonify(render_tarea_detail(tarea)), 200
    return jsonify({"error": "Tarea no encontrada"}), 404

# Crear una tarea
@tarea_db.route("/taks", methods=["POST"])
@jwt_required
def create_tarea():
    data = request.json
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")
    create_at = data.get("create_at")
    assigned_to = data.get("assigned_to")

    if (title and description and status and create_at and assigned_to is not None):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    tarea = Tarea(title=title, description=description, status=status, create_at=create_at, assigned_to=assigned_to)
    tarea.save()
    return jsonify(render_tarea_detail(tarea)), 201
    

# actualizar una tarea
@tarea_db.route("/taks/<int:id>", methods=["PUT"])
@jwt_required
def update_tarea(id):
    tarea = Tarea.get_by_id(id)
    if not tarea:
        return jsonify({"error": "Tarea no encontrado"}), 404

    data = request.json
    title = data.get("title")
    descripcion = data.get("description")
    status = data.get("status")
    create_at = data.get("create_at")
    assigned_to = data.get("assigned_to")

    tarea.update(title=title, description=descripcion, status=status, create_at=create_at, assigned_to=assigned_to)
    tarea.save()

    return jsonify(render_tarea_detail(tarea)), 201


