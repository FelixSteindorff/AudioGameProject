from game import Game
import accessible_output2.outputs.auto

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
    