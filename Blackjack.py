from Controller.Controller import Controller
from View.View import UI
from Model.Game import Game

#import gui stuff here

game = Game()
view = UI()
controller = Controller(game, view)

# start gui here
# view.show()

