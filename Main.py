from personas import generar_personas, escribir_csv
from comunidad import Comunidad
from enfermedad import Enfermedad

if __name__ == "__main__":
    cantidad_personas = 1000
    personas = generar_personas(cantidad_personas)
    archivo_salida = 'personas_para_comunidad.csv'
    escribir_csv(personas, archivo_salida)
    print(f'Se han generado {cantidad_personas} personas y se han guardado en {archivo_salida}')
    
   
    infeccion_probable = 0.1
    Dias = 100
    
    enfermedad = Enfermedad(infeccion_probable, Dias)
    
    
    num_comunidades = 100
    promedio_conexion_fisica = 5
    num_infectados = 10  
    probabilidad_conexion_fisica = 0.2
    
    
    comunidad = Comunidad(num_comunidades, promedio_conexion_fisica, probabilidad_conexion_fisica)
    archivo_csv = 'personas_para_comunidad.csv'
    comunidad.cargar_personas_desde_csv(archivo_csv)
    comunidad.crear_conexiones()
    enfermedad.inicializar_infectados(comunidad, num_infectados)
    
    print("\nEstado inicial de la comunidad:")
    comunidad.imprimir_estado()
    
    # Simulación de la propagación de la enfermedad por varios pasos
    for paso in range(Dias):
        print(f"\nDias {paso + 1}:")
        enfermedad.propagar_enfermedad(comunidad)
        comunidad.imprimir_estado()
        num_infectados = enfermedad.contar_infectados(comunidad)
        print(f"Cantidad de infectados: {num_infectados}")
    
    cantidad_personas = comunidad.numero_personas()
    print(f"\nNúmero total de personas: {cantidad_personas}")