
import numpy as np
import random

class Enfermedad:
    def __init__(self, beta, gamma, promedio_pasos):
        self.beta = beta
        self.gamma = gamma
        self.promedio_pasos = promedio_pasos
        self.contador_muertes = 0  
        self.lista_muertes = []  
    
    def inicializar_infectados(self, comunidad, num_infectados):
        infectados_iniciales = np.random.choice(comunidad.personas, num_infectados, replace=False)
        
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
                conexiones_totales = persona['Conexiones'] + persona['ConexionesFamiliares']
                num_conexiones = min(int(np.random.normal(comunidad.promedio_conexion_fisica, 1)), len(conexiones_totales))
                if num_conexiones > 0:
                    conexiones = np.random.choice(conexiones_totales, num_conexiones, replace=False)
                    for conexion_id in conexiones:
                        if np.random.random() < comunidad.probabilidad_conexion_fisica:
                            otra_persona = next((p for p in comunidad.personas if p['ID'] == conexion_id), None)
                            if otra_persona and otra_persona['Estado'] == 'Sano':
                                if np.random.random() < (self.beta * I / N):
                                    nuevos_infectados.append(otra_persona)

                persona['Contador'] -= 1
                if persona['Contador'] <= 0:
                    if np.random.random() < self.gamma:
                        persona['Estado'] = 'Recuperado'
                        nuevos_recuperados.append(persona)
                    else:
                        persona['Estado'] = 'Muerto'
                        self.contador_muertes += 1  
                        self.lista_muertes.append(persona)  

        for infectado in nuevos_infectados:
            infectado['Estado'] = 'Infectado'
            infectado['Contador'] = self.promedio_pasos
        
        comunidad.personas = [persona for persona in comunidad.personas if persona['Estado'] != 'Muerto']

    def contar_sir(self, comunidad):
        S = sum(1 for persona in comunidad.personas if persona['Estado'] == 'Sano')
        I = sum(1 for persona in comunidad.personas if persona['Estado'] == 'Infectado')
        R = sum(1 for persona in comunidad.personas if persona['Estado'] == 'Recuperado')
        return S, I, R

    def obtener_muertes(self):
        return self.contador_muertes

    def obtener_lista_muertes(self):
        return self.lista_muertes
