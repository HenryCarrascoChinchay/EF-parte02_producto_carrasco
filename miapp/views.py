from django.shortcuts import render, HttpResponse, redirect



# Create your views here.

layout = """
    <h1> Proyecto Web (LP3) | Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/integrantes"> Integrantes</a>
        </li>
        <li>
            <a href="/crear_docentes"> Crear Docente</a>
        </li>
            <a href="/listar_docentes"> Listar Docentes</a>
        </li>    
        </li>
            <a href="/crear_curso"> Crear Curso</a>
        </li>
        </li>
            <a href="/listar_cursos"> Listar Cursos </a>
        </li>
    </ul>
    <hr/>
"""
def index(request):
    

    return render(request)

# Create your views here.
