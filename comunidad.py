import csv
import random

class Comunidad:
    def __init__(self, num_comunidades, promedio_conexion_fisica, probabilidad_conexion_fisica):
        self.num_comunidades = num_comunidades
        self.promedio_conexion_fisica = promedio_conexion_fisica
        self.probabilidad_conexion_fisica = probabilidad_conexion_fisica
        self.personas = []
    
    def cargar_personas_desde_csv(self, archivo_csv):
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.personas.append({
                    'Nombre': row['Nombre'],
                    'Apellido': row['Apellido'],
                    'ID': row['ID'],
                    'Estado': 'Sano',  # Valor por defecto para el estado de la persona
                    'Familia': row['Familia'],
                    'Conexiones': [],
                    'Contador': 0  # Contador de pasos para la enfermedad
                })
        return self.personas
    
    def numero_personas(self):
        return len(self.personas)
    
    def crear_conexiones(self):
        # Diccionario para agrupar personas por familia
        personas_por_familia = {}
        for persona in self.personas:
            if persona['Familia'] not in personas_por_familia:
                personas_por_familia[persona['Familia']] = []
            personas_por_familia[persona['Familia']].append(persona)
        
        # Conectar personas dentro de la misma familia
        for familia, personas in personas_por_familia.items():
            num_conexiones = int(random.gauss(self.promedio_conexion_fisica, 1))
            conexiones = random.sample(personas, min(num_conexiones, len(personas)))
            for persona in personas:
                persona['Conexiones'].extend([conexion['ID'] for conexion in conexiones if conexion != persona])
        
        # Conectar personas de diferentes familias
        familias = list(personas_por_familia.keys())
        for persona in self.personas:
            num_conexiones_familiares = int(random.gauss(self.promedio_conexion_fisica / 2, 1))
            for _ in range(num_conexiones_familiares):
                otra_familia = random.choice(familias)
                if otra_familia != persona['Familia']:
                    persona_otra_familia = random.choice(personas_por_familia[otra_familia])
                    persona['Conexiones'].append(persona_otra_familia['ID'])

    def imprimir_estado(self):
        for persona in self.personas:
            print(f"Nombre: {persona['Nombre']}, Apellido: {persona['Apellido']}, ID: {persona['ID']}, Estado: {persona['Estado']}, Familia: {persona['Familia']}, Conexiones: {persona['Conexiones']}")
