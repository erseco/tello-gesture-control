from djitellopy import Tello

class TelloKeyboardController:
    def __init__(self, tello: Tello):
        self.tello = tello
    
    def control(self, key):

        Upkey = 2490368
        DownKey = 2621440
        LeftKey = 2424832
        RightKey = 2555904    


        if key == ord('w') or key == Upkey:
            self.tello.move_forward(30)
        elif key == ord('s') or key == DownKey:
            self.tello.move_back(30)
        elif key == ord('a') or key == LeftKey:
            self.tello.move_left(30)
        elif key == ord('d') or key == RightKey:
            self.tello.move_right(30)
        elif key == ord('e'):
            self.tello.rotate_clockwise(30)
        elif key == ord('q'):
            self.tello.rotate_counter_clockwise(30)
        elif key == ord('r'):
            self.tello.move_up(30)
        elif key == ord('f'):
            self.tello.move_down(30)



