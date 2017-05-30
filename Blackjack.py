from Controller.Controller import Controller
from View.View import UI
from Model.Game import Game


game = Game()
# GUI or command line?
view = UI()
controller = Controller(game, view)

# start gui here
# view.show()

