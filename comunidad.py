import csv
class Comunidad:
    def cargar_personas_desde_csv(self, archivo_csv):
        personas = []
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                personas.append({
                    'Nombre': row['Nombre'],
                    'Apellido': row['Apellido'],
                    'ID': row['ID'],
                    'Estado': row['Estado'],
                    'familia': row['familia']
                })
        self.personas = personas  # Guardamos las personas como atributo de la instancia
        return personas
    
    def numero_personas(self):
        return len(self.personas)  # Devuelve la longitud de la lista de personas de la instancia

# Bloque principal
if __name__ == "__main__":
    comunidad = Comunidad()
    archivo_csv = 'personas_para_comunidad.csv'
    personas = comunidad.cargar_personas_desde_csv(archivo_csv)
    
    for persona in personas:
        print(f"Nombre: {persona['Nombre']}, Apellido: {persona['Apellido']}, ID: {persona['ID']}, Estado: {persona['Estado']}, Familia: {persona['familia']}")
    
    cantidad_personas = comunidad.numero_personas()  # Llamamos al método sin argumentos adicionales
    print(f"Número total de personas: {cantidad_personas}")