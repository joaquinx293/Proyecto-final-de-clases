import csv
import random

class Persona():
    def nombre_apellidos(self):
        # Lista de nombres y apellidos simplificados
        nombres = ["Aarón", "Abner", "Abril", "Adela", "Adrián", "Agustín", "Alan", "Alberto", "Alejandra", 
    "Alejandro", "Alessandra", "Alex", "Alexander", "Alexis", "Alfonso", "Alfredo", "Alicia", 
    "Aline", "Alma", "Alonso", "Álvaro", "Amalia", "Amparo", "Ana", "Anabel", "Anabella", 
    "Andrea", "Andrés", "Ángel", "Angélica", "Aníbal", "Antonio", "Ariadna", "Ariel", "Armando", 
    "Arturo", "Asunción", "Aurora", "Beatriz", "Benjamín", "Bernardo", "Blanca", "Braulio", 
    "Brenda", "Bruno", "Camila", "Carlos", "Carmen", "Carolina", "Casandra", "Catalina", "Celia", 
    "César", "Cecilia", "Claudia", "Clemente", "Concepción", "Conrado", "Cristian", "Cristina", 
    "Daniel", "Daniela", "David", "Delia", "Diego", "Diana", "Digna", "Dolores", "Domingo", 
    "Edgar", "Edith", "Eduardo", "Elena", "Elías", "Elisa", "Elizabeth", "Emilia", "Emilio", 
    "Emmanuel", "Enrique", "Ernesto", "Esteban", "Estefanía", "Eugenia", "Eusebio", "Eva", 
    "Evelio", "Fabián", "Fabricio", "Facundo", "Fátima", "Federico", "Felipe", "Fernanda", 
    "Fernando", "Fidel", "Flor", "Flora", "Florencia", "Francisco", "Gabriel", "Gabriela", 
    "Genaro", "Gerardo", "Germán", "Gilberto", "Gloria", "Gonzalo", "Graciela", "Gregorio", 
    "Guillermo", "Gustavo", "Héctor", "Helena", "Hernán", "Hugo", "Humberto", "Ignacio", "Inés", 
    "Irene", "Isaac", "Isabel", "Isidora", "Iván", "Jacinto", "Jaime", "Javier", "Jeremías", 
    "Jerónimo", "Jesús", "Jimena", "Joaquín", "Jorge", "José", "Josefa", "Josefina", "Juan", 
    "Juana", "Julia", "Julián", "Julieta", "Justo", "Karina", "Laura", "Lautaro", "Leonel", 
    "Leonardo", "Leticia", "Lorenzo", "Lucas", "Lucía", "Luciano", "Luisa", "Luis", "Lourdes", 
    "Luz", "Magdalena", "Manuel", "Marcelino", "Marcela", "Marcelo", "Marco", "Marcos", "María", 
    "Mariano", "Mario", "Marta", "Martín", "Matías", "Mauricio", "Maximiliano", "Melisa", 
    "Mercedes", "Micaela", "Miguel", "Mónica", "Natalia", "Nicolás", "Nidia", "Noelia", "Nora", 
    "Norma", "Octavio", "Olivia", "Omar", "Oriana", "Oscar", "Osvaldo", "Pablo", "Pamela", 
    "Paola", "Patricia", "Patricio", "Paula", "Pedro", "Pilar", "Priscila", "Rafael", "Ramiro", 
    "Raquel", "Raúl", "Rebeca", "Renata", "Ricardo", "Rigoberto", "Rita", "Roberto", "Rocío", 
    "Rodrigo", "Rosa", "Rosario", "Rubén", "Salvador", "Samuel", "Sandra", "Santiago", "Sara", 
    "Sebastián", "Sergio", "Silvia", "Simón", "Sofía", "Sonia", "Susana", "Tadeo", "Tamara", 
    "Teodoro", "Teresa", "Tomás", "Ulises", "Valentín", "Valeria", "Vanessa", "Verónica", 
    "Vicente", "Victor", "Victoria", "Víctor", "Virginia", "Viviana", "Walter", "Wilfredo", 
    "Ximena", "Yadira", "Yolanda", "Yvonne", "Zaida", "Zaira", "Zoé", "Aaron", "Abigail", 
    "Agustin", "Alanis", "Alberta", "Alexa", "Alfonso", "Alicia", "Alina", "Amanda", "Amelia", 
    "Anaís", "Anahí", "Analia", "Anastasia", "Andrea", "Anibal", "Antonio", "Ariana", "Armando", 
    "Arthur", "Aurora", "Avelina", "Axel", "Azucena", "Belén", "Benicio", "Bernardo", "Bianca", 
    "Bricia", "Bruno", "Camilo", "Candelaria", "Caridad", "Carlos", "Carmela", "Celeste", 
    "Cielo", "Clara", "Clemente", "Constanza", "Cosme", "Cristal", "Cristóbal", "Dante", 
    "Darío", "Débora", "Delfina", "Demetrio", "Denis", "Dionisio", "Dorian", "Dulce", "Eduardo", 
    "Elena", "Elvira", "Emilio", "Encarnación", "Esperanza", "Estefanía", "Estela", "Ezequiel", 
    "Fabiola", "Faustino", "Fermín", "Fernando", "Flavio", "Florentino", "Fortunato", 
    "Francisco", "Frida", "Gabriela", "Gaspar", "Genoveva", "Gerardo", "Gilberto", "Gloria", 
    "Gonzalo", "Gregorio", "Guadalupe", "Guillermo", "Hernán", "Hortensia", "Humberto", 
    "Ignacio", "Iker", "Inocencia", "Irma", "Isabel", "Ismael", "Ivonne", "Jacqueline", "Javier", 
    "Jesusa", "Joel", "Jorge", "Josefina", "Josué", "Juan", "Juana", "Julián", "Julieta", 
    "Justina", "Karla", "Kevin", "Lázaro", "Laura", "Leandro", "Leonardo", "Lidia", "Lorenzo", 
    "Lourdes", "Luz", "Magdalena", "Manuel", "Marcelino", "Marcela", "Marcelo", "Marco", 
    "Marcos", "María", "Mariano", "Mario", "Marta", "Martín", "Matías", "Mauricio", 
    "Maximiliano", "Melisa", "Mercedes", "Micaela", "Miguel", "Mónica", "Natalia", "Nicolás", 
    "Nidia", "Noelia", "Nora", "Norma", "Octavio", "Olivia", "Omar", "Oriana", "Oscar", 
    "Osvaldo", "Pablo", "Pamela", "Paola", "Patricia", "Patricio", "Paula", "Pedro", "Pilar", 
    "Priscila", "Rafael", "Ramiro", "Raquel", "Raúl", "Rebeca", "Renata", "Ricardo", 
    "Rigoberto", "Rita", "Roberto", "Rocío", "Rodrigo", "Rosa", "Rosario", "Rubén", "Salvador", 
    "Samuel", "Sandra", "Santiago", "Sara", "Sebastián", "Sergio", "Silvia", "Simón", "Sofía", 
    "Sonia", "Susana", "Tadeo", "Tamara", "Teodoro", "Teresa", "Tomás", "Ulises", "Valentín", 
    "Valeria", "Vanessa", "Verónica", "Vicente", "Victor", "Victoria", "Víctor", "Virginia", 
    "Viviana", "Walter", "Wilfredo", "Ximena", "Yadira", "Yolanda", "Yvonne", "Zaida", "Zaira", 
    "Zoé"]
        apellidos = ["García", "Fernández", "González", "Rodríguez", "López", "Martínez", "Sánchez", "Pérez", 
    "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno", "Muñoz", "Álvarez", 
    "Romero", "Alonso", "Gutiérrez", "Navarro", "Torres", "Domínguez", "Vázquez", "Ramos", 
    "Gil", "Ramírez", "Serrano", "Blanco", "Molina", "Morales", "Suárez", "Ortega", "Delgado", 
    "Castro", "Ortiz", "Rubio", "Marín", "Sanz", "Nieto", "Medina", "Vega", "Soler", "Parra", 
    "Redondo", "Izquierdo", "Miranda", "Garrido", "Peña", "Vargas", "Herrera", "Rojas", "Leal", 
    "Peña", "Montoya", "Lara", "Castro", "Orozco", "Vega", "Estrada", "Mora", "Padilla", "Soto", 
    "Peña", "Caballero", "Ponce", "Calderón", "Caro", "Fuentes", "León", "Núñez", "Navarro", 
    "Reyes", "Castro", "Román", "Márquez", "Duarte", "Rivas", "Pineda", "Espinoza", "Franco", 
    "Barrios", "Carrasco", "Velasco", "Ayala", "Cáceres", "Salazar", "Moya", "Pacheco", 
    "Santana", "Cabrera", "Campos", "Guzmán", "Gallego", "Solís", "Estévez", "Villar", "Abad", 
    "Aguayo", "Alcalá", "Amador", "Amor", "Aparicio", "Araújo", "Arroyo", "Asensio", "Ballester", 
    "Ballesteros", "Barrios", "Bautista", "Becerra", "Beltrán", "Bernal", "Berrocal", "Bleda", 
    "Blasco", "Blázquez", "Borja", "Borrero", "Bravo", "Buitrago", "Bustamante", "Cabezas", 
    "Cabral", "Cadenas", "Calvo", "Camacho", "Cañizares", "Cárdenas", "Carranza", "Carrión", 
    "Casado", "Casares", "Casillas", "Castellano", "Castañeda", "Castillo", "Ceja", "Cepeda", 
    "Cerrato", "Cervantes", "Chacón", "Chamorro", "Chaparro", "Cifuentes", "Clemente", "Collado", 
    "Colmenares", "Conde", "Contreras", "Correa", "Córdova", "Cornejo", "Coronel", "Cortés", 
    "Coto", "Covarrubias", "Crespo", "Cruz", "Cuéllar", "Cuenca", "Dávalos", "Delgado", "Díez", 
    "Domínguez", "Dueñas", "Durán", "Echeverría", "Elizondo", "Esparza", "Espinosa", "Esquivel", 
    "Fabregat", "Fajardo", "Falcón", "Farfán", "Farré", "Ferrer", "Ferrera", "Flores", "Fonseca", 
    "Font", "Forteza", "Fuentes", "Galán", "Galindo", "Gálvez", "Gamboa", "Gámez", "Garay", 
    "Garcés", "Garnica", "Garza", "Gaspar", "Giner", "Godoy", "Gordillo", "Gracia", "Grande", 
    "Grau", "Guerra", "Guerrero", "Gutiérrez", "Guzmán", "Heredia", "Hidalgo", "Hoyos", "Huerta", 
    "Ibáñez", "Ibarra", "Iglesias", "Inguanzo", "Izquierdo", "Jácome", "Jáuregui", "Jerez", 
    "Jiménez", "Jordán", "Joya", "Juárez", "Lamas", "Lara", "Larios", "Laso", "Lemus", "León", 
    "Lerma", "Limón", "Lizarraga", "Llamas", "Llerena", "Lobo", "Lomas", "Londoño", "Lozano", 
    "Luque", "Macías", "Madrid", "Maldonado", "Manzano", "Márquez", "Marrero", "Martín", 
    "Martínez", "Marín", "Mata", "Mateos", "Medina", "Mejía", "Melgar", "Meneses", "Mendoza", 
    "Menéndez", "Merino", "Mesa", "Molina", "Montero", "Montes", "Montiel", "Mora", "Morales", 
    "Morán", "Moreno", "Muñoz", "Murillo", "Nájera", "Naranjo", "Navarro", "Navas", "Noguera", 
    "Noriega", "Núñez", "Oliva", "Olivares", "Olivera", "Olmos", "Ordóñez", "Ortiz", "Osorio", 
    "Pacheco", "Padrón", "Paredes", "Parra", "Pastrana", "Pavón", "Pedraza", "Peinado", "Peña", 
    "Peralta", "Pereira", "Peris", "Pérez", "Picazo", "Pina", "Pineda", "Pizarro", "Ponce", 
    "Pons", "Pozo", "Prado", "Prats", "Prieto", "Puerta", "Quezada", "Quintero", "Quirós", 
    "Ramírez", "Ramos", "Reina", "Rendón", "Requena", "Reyes", "Ríos", "Rivas", "Rivera", 
    "Robles", "Roca", "Rodríguez", "Roig", "Romero", "Rosales", "Rosas", "Rubio", "Ruiz", 
    "Salazar", "Salinas", "Salmerón", "Salvador", "Salvatierra", "Sánchez", "Sancho", "Santana", 
    "Santos", "Sanz", "Sarmiento", "Segovia", "Segura", "Sepúlveda", "Serrano", "Sierra", 
    "Silva", "Simón", "Solano", "Soler", "Soto", "Suárez", "Tapia", "Téllez", "Terán", "Teruel", 
    "Tejada", "Toledo", "Torres", "Trejo", "Trillo", "Trujillo", "Urbano", "Ureña", "Uribe", 
    "Urrutia", "Valencia", "Valero", "Valle", "Vallejo", "Valls", "Valverde", "Varela", "Vargas", 
    "Vázquez", "Vega", "Velasco", "Velázquez", "Ventura", "Vera", "Verdú", "Verdugo", "Vergara", 
    "Viana", "Vicente", "Vidal", "Viera", "Villa", "Villalba", "Villanueva", "Villegas", 
    "Vinuesa", "Viñas", "Vivas", "Vizcaíno", "Yáñez", "Zambrano", "Zapata", "Zaragoza", "Zárate", 
    "Zúñiga"]
        return random.choice(nombres), random.choice(apellidos)

def generar_personas(cantidad):
    personas = []
    id = generar_id(cantidad)
    for _ in range(cantidad):
        persona = Persona()
        nombre, apellido = persona.nombre_apellidos()
        personas.append({'Nombre': nombre, 'Apellido': apellido,'ID': id[_] })
    return personas

def generar_id(cantidad, longitud=10):
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
        fieldnames = ['Nombre', 'Apellido','ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for persona in personas:
            writer.writerow(persona)

def main():
    cantidad_personas = 500
    personas = generar_personas(cantidad_personas)
    archivo_salida = 'personas.csv'
    escribir_csv(personas, archivo_salida)
    print(f'Se han generado {cantidad_personas} personas y se han guardado en {archivo_salida}')

if __name__ == "__main__":
    main()
