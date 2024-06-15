import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio

import pygame
#APPID = 'com.fabio.duran.treeview'


class Gtk4TestTest(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(
            self, application=app, title='Gtk.TreeView Test',
        )
        pygame.init()
        pygame.mixer.init()

        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=20,
            margin_top=20, margin_bottom=20,
            margin_start=20, margin_end=20
        ) 
        # Menu
        header_bar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header_bar)
        self.set_title("Proyecto final")

        # Listado del menu
        menu = Gio.Menu.new()

        # Create a popover
        self.popover = Gtk.PopoverMenu()
        self.popover.set_menu_model(menu)

    
        # crea un menu
        self.menu_popover = Gtk.MenuButton()
        self.menu_popover.set_popover(self.popover)
        self.menu_popover.set_icon_name("open-menu-symbolic")

        # agrega headerbar el menu popover
        header_bar.pack_end(self.menu_popover)

        # Add an about dialog 
        about_menu = Gio.SimpleAction.new("about", None)
        about_menu.connect("activate", self.show_about_dialog)
        self.add_action(about_menu)
        menu.append("Acerca de", "win.about")

        button_Adelantar = Gtk.Button(label="Retroceder")
        button_Adelantar.connect("clicked", self.adelantar)
        header_bar.pack_start(button_Adelantar)

        button_retroceder = Gtk.Button(label="Adelantar")
        button_retroceder.connect("clicked", self.show_retroceder)
        header_bar.pack_start(button_retroceder)

        button_reproducir = Gtk.Button(label="Reproducir")
        button_reproducir.connect("clicked", self.show_reproducir)
        header_bar.pack_start(button_reproducir)
        self.set_child(box)
    
    def adelantar(self, widget):
        dialog = Gtk.FileChooserDialog(title = "Adelantar",
                                       parent = self,
                                       action = Gtk.FileChooserAction.SAVE,
                                       )
       

    def show_about_dialog(self, action, param):
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self)
        self.about.set_modal(self)

        self.about.set_authors(["Joaquin Aliro Marambio Romero "])
        self.about.set_copyright("Joaquin Aliro Marambio Romero")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_version("4.0")
        self.about.set_logo_icon_name("org.example.example")
        self.about.set_visible(True)
        pass
    def show_reproducir(self, widget):
          # Cargar y reproducir una canción usando Pygame
        pygame.mixer.music.load("/home/liveuser/Downloads/plaga.mp3")  # Reemplaza con la ruta de tu canción
        pygame.mixer.music.play()


 
    def show_retroceder(self, action):
        dialog = Gtk.MessageDialog(
            title="Exito",
            transient_for=self,
            default_width=300,
            default_height=50
        )
        dialog.set_markup("Se ha limpiado correctamente")
        dialog.add_button("OKEY", Gtk.ResponseType.CLOSE)
        dialog.set_deletable(True)
        dialog.connect("response", lambda dialog, response_id: dialog.destroy())
        dialog.show()
        
    def show_adelantar(self):
       print("hola mundo")

   
        

class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()

