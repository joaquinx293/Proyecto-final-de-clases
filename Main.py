
from comunidad import Comunidad
from enfermedad import Enfermedad
from personas import generar_personas, escribir_csv

def simular_infeccion(comunidad, enfermedad, dias):
    for dia in range(dias):
        print(f"\nDía {dia + 1}:")
        enfermedad.propagar_enfermedad(comunidad)
        S, I, R = enfermedad.contar_sir(comunidad)
        muertes = enfermedad.obtener_muertes()
        print(f"Susceptibles: {S}, Infectados: {I}, Recuperados: {R}, Muertes: {muertes}")

if __name__ == "__main__":
    cantidad_personas = 1000
    personas = generar_personas(cantidad_personas)
    archivo_salida = 'personas_para_comunidad.csv'
    escribir_csv(personas, archivo_salida)
    
    beta = 0.9
    gamma = 0.1
    promedio_pasos = 10
    
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
    
    # Simulación de la infección durante 30 días
    dias_simulacion = 100
    simular_infeccion(comunidad, enfermedad, dias_simulacion)
    
    cantidad_personas = comunidad.numero_personas()
    print(f"\nNúmero total de personas: {cantidad_personas}")
