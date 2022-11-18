from djitellopy import Tello

class TelloKeyboardController:
    def __init__(self, tello: Tello):
        self.tello = tello
    
    def control(self, key):

        Key_UP = 0
        Key_DOWN = 1
        Key_LEFT = 2
        Key_RIGHT = 3
        Key_PLUS = 43
        Key_MINUS = 45


        if key == ord('w') or key == Key_UP:
            self.tello.move_forward(30)
        elif key == ord('s') or key == Key_DOWN:
            self.tello.move_back(30)
        elif key == ord('a') or key == Key_LEFT:
            self.tello.move_left(30)
        elif key == ord('d') or key == Key_RIGHT:
            self.tello.move_right(30)
        elif key == ord('e'):
            self.tello.rotate_clockwise(30)
        elif key == ord('q'):
            self.tello.rotate_counter_clockwise(30)
        elif key == ord('r') or key == Key_PLUS:
            self.tello.move_up(30)
        elif key == ord('f') or key == Key_MINUS:
            self.tello.move_down(30)



