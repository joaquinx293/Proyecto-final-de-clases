import random

class Enfermedad:
    def __init__(self, beta, gamma, promedio_pasos):
        self.beta = beta
        self.gamma = gamma
        self.promedio_pasos = promedio_pasos
        self.contador_muertes = 0  
    
    def inicializar_infectados(self, comunidad, num_infectados):
        infectados_iniciales = random.sample(comunidad.personas, num_infectados)
        
        for infectado in infectados_iniciales:
            infectado['Estado'] = 'Infectado'
            infectado['Contador'] = self.promedio_pasos
    
    def propagar_enfermedad(self, comunidad):
        nuevos_infectados = []
        nuevos_recuperados = []
        
        S, I, R = self.contar_sir(comunidad)
        N = S + I + R
        
        for persona in comunidad.personas:
            if persona['Estado'] == 'Infectado':
                for conexion_id in persona['Conexiones'] + persona['ConexionesFamiliares']:
                    if random.random() < comunidad.probabilidad_conexion_fisica:
                        otra_persona = next((p for p in comunidad.personas if p['ID'] == conexion_id), None)
                        if otra_persona and otra_persona['Estado'] == 'Sano':
                            if random.random() < (self.beta * I / N):
                                nuevos_infectados.append(otra_persona)

                persona['Contador'] -= 1
                if persona['Contador'] <= 0:
                    if random.random() < self.gamma:
                        persona['Estado'] = 'Recuperado'
                        nuevos_recuperados.append(persona)
                    else:
                        persona['Estado'] = 'Muerto'
                        self.contador_muertes += 1  

        for infectado in nuevos_infectados:
            infectado['Estado'] = 'Infectado'
            infectado['Contador'] = self.promedio_pasos

    def contar_sir(self, comunidad):
        S = sum(1 for persona in comunidad.personas if persona['Estado'] == 'Sano')
        I = sum(1 for persona in comunidad.personas if persona['Estado'] == 'Infectado')
        R = sum(1 for persona in comunidad.personas if persona['Estado'] == 'Recuperado')
        return S, I, R

    def obtener_muertes(self):
        return self.contador_muertes
