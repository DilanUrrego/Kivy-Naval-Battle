from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Cada aplicación Kivy es una clase descendiente de la clase kivy.app.App
class KivyNavalBattle(App):
    
    def build(self):
        self.Tablero = BoxLayout( orientation="vertical")

        for n_row in range(3):
            row = BoxLayout( orientation="horizontal")
            self.Tablero.add_widget( row )
            for n_column in range(3):
                casilla = Button(text= str(n_column) + "-" + str(n_row), font_size=80)
                # Conectar el evento press de cada boton, con el callback
                # Todos los botones van a usar un mismo callback
                # Pero se diferencian por el segundo parametro sender
                casilla.bind( on_press=self.seleccionar_casilla )
                row.add_widget(casilla)

        return self.Tablero
    
    # Callback que se llama cuando hagan click en cualquier boton
    # El boton que genera el evento es el segundo parametro "sender"
    def seleccionar_casilla( self, sender ):
        print( "Casilla seleccionada: " + sender.text )
    
# Para ejecutar la aplicación, se debe llamar al método run() de
# la clase principal descendiente de kivy.app.App
if __name__ == "__main__":
    KivyNavalBattle().run()