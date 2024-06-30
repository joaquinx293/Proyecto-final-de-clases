
import csv
import random
import json

class Persona():
    def nombre_apellidos(self):
        with open("nombres.json") as archivo:
            datos = json.load(archivo)
            self.nombres = datos["nombres"]
            self.apellidos = datos["apellidos"]
        return random.choice(self.nombres), random.choice(self.apellidos)

def generar_personas(cantidad):
    personas = []
    id = generar_id(cantidad)
    for _ in range(cantidad):
        persona = Persona()
        nombre, apellido = persona.nombre_apellidos()
        personas.append({'Nombre': nombre, 'Apellido': apellido,'ID': id[_], 'Estado': None, 'familia':None })
    return personas

def generar_id(cantidad, longitud=20):
    ids_generados = set()
    id = []
    while len(id) < cantidad:
        nuevo_id = ''.join(random.choices('0123456789', k=longitud))
        if nuevo_id not in ids_generados:
            ids_generados.add(nuevo_id)
            id.append(nuevo_id)
    return id
def escribir_csv(personas, archivo_salida):
    with open(archivo_salida, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Nombre', 'Apellido','ID','Estado','familia']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for persona in personas:
            writer.writerow(persona)
def enfermedad(personas):
    indice_infectado = random.randint(0, len(personas) - 1)
    personas[indice_infectado]['Estado'] = 'Infectado'
    print(f'Persona infectada: {personas[indice_infectado]["Nombre"]} {personas[indice_infectado]["Apellido"]}')

def main():
    cantidad_personas = 1000
    personas = generar_personas(cantidad_personas)
    enfermedad(personas)
    archivo_salida = 'personas_para_comunidad.csv'
    escribir_csv(personas, archivo_salida)
    print(f'Se han generado {cantidad_personas} personas y se han guardado en {archivo_salida}')

if __name__ == "__main__":
    main()
