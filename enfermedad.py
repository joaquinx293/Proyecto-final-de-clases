import random
class Enfermedad:
    def __init__(self, infeccion_probable, promedio_pasos):
        self.infeccion_probable = infeccion_probable
        self.promedio_pasos = promedio_pasos
    
    def inicializar_infectados(self, comunidad, num_infectados):
        infectados_iniciales = []
        while len(infectados_iniciales) < num_infectados:
            indice = int(random.gauss(comunidad.num_comunidades / 2, comunidad.num_comunidades / 6))
            if 0 <= indice < comunidad.num_comunidades and comunidad.personas[indice] not in infectados_iniciales:
                infectados_iniciales.append(comunidad.personas[indice])
        
        for infectado in infectados_iniciales:
            infectado['Estado'] = 'Infectado'
            infectado['Contador'] = self.promedio_pasos
    
    def propagar_enfermedad(self, comunidad):
        nuevos_infectados = []
        for persona in comunidad.personas:
            if persona['Estado'] == 'Infectado':
                for conexion_id in persona['Conexiones']:
                    if random.random() < comunidad.probabilidad_conexion_fisica:
                        for otra_persona in comunidad.personas:
                            if otra_persona['ID'] == conexion_id and otra_persona['Estado'] == 'Sano':
                                if random.random() < self.infeccion_probable:
                                    nuevos_infectados.append(otra_persona)
            persona['Contador'] -= 1
            if persona['Contador'] <= 0 and persona['Estado'] == 'Infectado':
                persona['Estado'] = 'De alta'
        
        for infectado in nuevos_infectados:
            infectado['Estado'] = 'Infectado'
            infectado['Contador'] = self.promedio_pasos
    
    def contar_infectados(self, comunidad):
        return sum(1 for persona in comunidad.personas if persona['Estado'] == 'Infectado')
