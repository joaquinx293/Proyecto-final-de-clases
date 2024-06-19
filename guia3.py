import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio
import pygame

class Gtk4TestTest(Gtk.ApplicationWindow):

    def __init__(self, app):
        super().__init__(application=app, title='Gtk.TreeView Test')

        self.musica = False  # Estado de reproducción de la música

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

        # Inicializar Pygame y Pygame.mixer para la reproducción de audio
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("/home/liveuser/Downloads/plaga.mp3")  # Ruta de tu canción

    def adelantar(self, widget):
        self.exito()
       

    def show_about_dialog(self, action, param):
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self)
        self.about.set_modal(True)

        self.about.set_authors(["Joaquin Aliro Marambio Romero"])
        self.about.set_copyright("Joaquin Aliro Marambio Romero")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_version("4.0")
        self.about.set_logo_icon_name("org.example.example")
        description = """
        Esta aplicación permite realizar diversas acciones mediante botones:
        - Botón Adelantar: Permite simular un dia .
        - Botón Retroceder: Permite retroceder un dia.
        - Botón Reproducir/Pausa: Controla la reproducción de música.
        - Botòn Avance rapido: Permite elegir el numero de dias que quieres que simule.
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
            button_ok.connect("clicked", self.on_avance_ok_clicked)
            dialog.add_action_widget(button_ok, Gtk.ResponseType.OK)

            button_cancel = Gtk.Button(label="Cancelar")
            button_cancel.connect("clicked", lambda *args: dialog.destroy())
            dialog.add_action_widget(button_cancel, Gtk.ResponseType.CANCEL)

            dialog.show()

    def on_avance_ok_clicked(self, widget):
        dias = self.entry_dias.get_text()
        print(f"Número de días ingresado: {dias}")

        # Aquí puedes añadir la lógica para avanzar los días según la entrada del usuario

        dialog = widget.get_parent()
        dialog.response(Gtk.ResponseType.OK)

       
    def exito(self):
            dialog = Gtk.MessageDialog(
                title="Exito",
                transient_for=self,
                default_width=300,
                default_height=50
            )
            dialog.set_markup("Se ha Realizado Corectamente")
            dialog.add_button("OKEY", Gtk.ResponseType.CLOSE)
            dialog.set_deletable(True)
            dialog.connect("response", lambda dialog, response_id: dialog.destroy())
            dialog.show()


class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        super().__init__()

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()
        # Iniciar la reproducción automática al iniciar la aplicación
        pygame.mixer.music.play()

def main():
    app = Gtk4TestApp()
    app.run()

if __name__ == '__main__':
    main()



