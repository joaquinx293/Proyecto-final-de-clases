import matplotlib.pyplot as plt
from comunidad import Comunidad
from enfermedad import Enfermedad
from personas import generar_personas, escribir_csv
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio
import pygame
import csv
import matplotlib

class Ventana(Gtk.ApplicationWindow):

    def __init__(self, app):
        super().__init__(application=app, title='Gtk.TreeView Test')
        self.dias = 0
        self.musica = True

        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=20,
            margin_top=20, margin_bottom=20,
            margin_start=20, margin_end=20
        ) 

        header_bar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header_bar)
        self.set_title("Proyecto final")

        menu = Gio.Menu.new()
        self.popover = Gtk.PopoverMenu()
        self.popover.set_menu_model(menu)

        self.menu_popover = Gtk.MenuButton()
        self.menu_popover.set_popover(self.popover)
        self.menu_popover.set_icon_name("open-menu-symbolic")
        header_bar.pack_end(self.menu_popover)

        about_menu = Gio.SimpleAction.new("about", None)
        about_menu.connect("activate", self.show_about_dialog)
        self.add_action(about_menu)
        menu.append("Acerca de", "win.about")

        button_Adelantar = Gtk.Button(label="Adelantar")
        button_Adelantar.connect("clicked", self.adelantar)
        header_bar.pack_start(button_Adelantar)

        button_retroceder = Gtk.Button(label="Retroceder")
        button_retroceder.connect("clicked", self.show_retroceder)
        header_bar.pack_start(button_retroceder)

        self.button_reproducir = Gtk.Button(label="Reproducir")
        self.button_reproducir.connect("clicked", self.reproducir_musica)
        header_bar.pack_start(self.button_reproducir)

        self.button_Avance = Gtk.Button(label="Avance rapido")
        self.button_Avance.connect("clicked", self.avance)
        header_bar.pack_start(self.button_Avance)

        self.set_child(box)
        self.cargar_archivo()
       
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("/home/liveuser/Downloads/plaga.mp3")
        
        # Inicializar comunidad y enfermedad
        self.inicializar_simulacion()


    
    def inicializar_simulacion(self):
        cantidad_personas = 1000
        personas = generar_personas(cantidad_personas)
        archivo_salida = 'personas_para_comunidad.csv'
        escribir_csv(personas, archivo_salida)
        
        self.beta = 0.25
        self.gamma = 0.3
        self.promedio_pasos = 49
        self.num_ciudadanos = 1000
        self.promedio_conexion_fisica = 5
        self.num_infectados = 100
        self.probabilidad_conexion_fisica = 0.2

        self.comunidad = Comunidad(self.num_ciudadanos, self.promedio_conexion_fisica, self.probabilidad_conexion_fisica)
        self.comunidad.cargar_personas_desde_csv(archivo_salida)
        self.comunidad.crear_conexiones()
        print("Estado inicial de la comunidad:")
        self.comunidad.imprimir_estado()
        

        self.enfermedad = Enfermedad(self.beta, self.gamma, self.promedio_pasos)
        self.enfermedad.inicializar_infectados(self.comunidad, self.num_infectados)
       

    def cargar_archivo(self):
        csv_file = "/home/liveuser/Downloads/personas.csv"
        try:
            with open(csv_file, newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo CSV en {csv_file}")

    def adelantar(self, widget):
        self.dias += 1
        self.exito()
        self.simular_infeccion(self.dias)

    def show_about_dialog(self, action, param):
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self)
        self.about.set_modal(True)

        self.about.set_authors(["Joaquin Aliro Marambio Romero"])
        self.about.set_copyright("Joaquin Aliro Marambio Romero")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_version("4.0")

        description = """
        Esta aplicación permite realizar diversas acciones mediante botones:
        - Botón Adelantar: Permite simular un día.
        - Botón Retroceder: Permite retroceder un día.
        - Botón Reproducir/Pausa: Controla la reproducción de música.
        - Botón Avance rápido: Permite elegir el número de días que quieres que simule.
        """
        self.about.set_comments(description)
        self.about.show()

    def reproducir_musica(self, widget):
        if self.musica:
            pygame.mixer.music.pause()
            self.button_reproducir.set_label("Reproducir")
        else:
            pygame.mixer.music.unpause()
            self.button_reproducir.set_label("Pausa")
        self.musica = not self.musica

    def show_retroceder(self, action):
        self.exito()
    
    def avance(self, action):
        dialog = Gtk.Dialog(
            title="Avance rápido",
            transient_for=self,
            modal=True
        )

        content_area = dialog.get_content_area()
        label = Gtk.Label()
        label.set_text("Número de días que quieres avanzar:")
        content_area.append(label)
        self.entry_dias = Gtk.Entry()
        content_area.append(self.entry_dias)
       
        button_ok = Gtk.Button(label="OK")
        button_ok.connect("clicked", self.on_avance_ok_clicked, dialog)
        dialog.add_action_widget(button_ok, Gtk.ResponseType.OK)

        button_cancel = Gtk.Button(label="Cancelar")
        button_cancel.connect("clicked", lambda *args: dialog.destroy())
        dialog.add_action_widget(button_cancel, Gtk.ResponseType.CANCEL)
        dialog.show() 
        

    def on_avance_ok_clicked(self, widget, dialog):
        try:
            dias = int(self.entry_dias.get_text())
            self.dias += dias
            self.simular_infeccion(self.dias)
        except ValueError:
            print("Por favor, ingrese un número válido.")
        dialog.destroy()

    def exito(self):
        dialog = Gtk.MessageDialog(
            title="Éxito",
            transient_for=self,
            default_width=300,
            default_height=50
        )
        dialog.set_markup("Se ha realizado correctamente.")
        dialog.add_button("OK", Gtk.ResponseType.CLOSE)
        dialog.set_deletable(True)
        dialog.connect("response", lambda dialog, response_id: dialog.destroy())
        dialog.show()

    def simular_infeccion(self, dias):
        cantidad_personas =self.comunidad.numero_personas()
        print(f"\nNúmero total de personas: {cantidad_personas}")
        susceptibles, infectados, recuperados = [], [], []
        for dia in range(dias):
            self.enfermedad.propagar_enfermedad(self.comunidad)
            S, I, R = self.enfermedad.contar_sir(self.comunidad)
            susceptibles.append(S)
            infectados.append(I)
            recuperados.append(R)
            muertes = self.enfermedad.obtener_muertes()
            print(f"Susceptibles: {S}, Infectados: {I}, Recuperados: {R}, Muertes: {muertes}")
        self.mostrar_grafico(susceptibles, infectados, recuperados)

    def mostrar_grafico(self, susceptibles, infectados, recuperados):
        dias = list(range(1, len(susceptibles) + 1))
        matplotlib.use('Agg')
        plt.figure(figsize=(10, 6))
        plt.plot(dias, susceptibles, label='Susceptibles')
        plt.plot(dias, infectados, label='Infectados')
        plt.plot(dias, recuperados, label='Recuperados')
        plt.xlabel('Días')
        plt.ylabel('Número de personas')
        plt.title('Simulación de propagación de enfermedad')
        plt.legend()
        plt.grid(True)
        plt.savefig('grafico.png')
        plt.close()
        

class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        super().__init__()

    def do_activate(self):
        window = Ventana(self)
        window.present()
        pygame.mixer.music.play()

if __name__ == "__main__":
    app = Gtk4TestApp()
    app.run()
