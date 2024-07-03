from comunidad import Comunidad
from enfermedad import Enfermedad
from personas import generar_personas, escribir_csv

if __name__ == "__main__":
    cantidad_personas = 1000
    personas = generar_personas(cantidad_personas)
    archivo_salida = 'personas_para_comunidad.csv'
    escribir_csv(personas, archivo_salida)
    beta = 0.1
    gamma = 0.7
    promedio_pasos = 20
    
    enfermedad = Enfermedad(beta, gamma, promedio_pasos)
    num_ciudadanos = 1000
    promedio_conexion_fisica = 5
    num_infectados = 10  
    probabilidad_conexion_fisica = 0.2
    comunidad = Comunidad(num_ciudadanos, promedio_conexion_fisica, probabilidad_conexion_fisica)
    archivo_csv = 'personas_para_comunidad.csv'
    comunidad.cargar_personas_desde_csv(archivo_csv)
    comunidad.crear_conexiones()
    enfermedad.inicializar_infectados(comunidad, num_infectados)
    
    print("Estado inicial de la comunidad:")
    comunidad.imprimir_estado()
    for paso in range(promedio_pasos):
        print(f"\nPaso {paso + 1}:")
        enfermedad.propagar_enfermedad(comunidad)
        #comunidad.imprimir_estado()
        S, I, R = enfermedad.contar_sir(comunidad)
        muertes = enfermedad.obtener_muertes()
        print(f"Susceptibles: {S}, Infectados: {I}, Recuperados: {R}, Muertes: {muertes}")
    cantidad_personas = comunidad.numero_personas()
    print(f"\nNúmero total de personas: {cantidad_personas}")

    # crear elimar lista pasos actual mas 5 llega ese paso 
