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
    

    return render(request,'index.html')

def integrantes(request):

    return render(request,'integrantes.html')

def crear_docente(request):

    return render(request,'crear_docente.html')
    
def listar_docentes(request):

    return render(request,'listar_docente.html')

def crear_curso(request):

    return render(request,'crear_curso.html')

def listar_cursos(request):

    return render(request,'listar_cursos.html')


# Create your views here.
