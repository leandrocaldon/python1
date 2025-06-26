from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#--------------------------------------------------------------

@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde FastAPI!"}

#--------------------------------------------------------------

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"saludo": f"Hola, {nombre}!"}

#--------------------------------------------------------------

@app.post("/enviar/{dato}")
def recibir_dato(dato: str):
    return {"respuesta": f"Me has enviado: {dato}"}

#--------------------------------------------------------------

class Persona(BaseModel):
    nombre: str
    cedula: str

@app.post("/registrar")
def registrar_persona(persona: Persona):
    return {
        "nombre_recibido": persona.nombre,
        "cedula_recibida": persona.cedula
    }
    
#--------------------------------------------------------------
class number(BaseModel):
    numero1: int
    numero2: int
    numero3: int
    numero4: int
    numero5: int
    

@app.post("/calculo")
def numeros(numero: number):
    # Crear lista con los números
    lista_numeros = [
        numero.numero1,
        numero.numero2, 
        numero.numero3,
        numero.numero4,
        numero.numero5
    ]
    
    # Calcular promedio
    promedio = sum(lista_numeros) / len(lista_numeros)
    
    # Ordenar de mayor a menor
    ordenados = sorted(lista_numeros, reverse=True)
    
    # Obtener número mayor y menor
    numero_mayor = max(lista_numeros)
    numero_menor = min(lista_numeros)
    
    return {
        "numeros_ordenados": ordenados,
        "promedio": promedio,
        "numero_mayor": numero_mayor,
        "numero_menor": numero_menor
    }

#--------------------------------------------------------------