def render_tarea_list(tareas):    
    return [
        {
            "id": tarea.id,
            "title":tarea.title,
            "descripcion":tarea.description,
            "status":tarea.status,
            "create_at":tarea.create_at,
            "assigned_to":tarea.assigned_to
        }
        for tarea in tareas
    ]


def render_tarea_detail(tarea):
    return {
            "id": tarea.id,
            "title":tarea.title,
            "descripcion":tarea.description,
            "status":tarea.status,
            "create_at":tarea.create_at,
            "assigned_to":tarea.assigned_to
    }




