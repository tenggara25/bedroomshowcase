class InputState:
    def __init__(self):
        self.keys_down = set()
        self.mouse_dx = 0.0
        self.mouse_dy = 0.0
        self.mouse_captured = True

    def reset_mouse_delta(self):
        self.mouse_dx = 0.0
        self.mouse_dy = 0.0

    def set_key(self, key, is_down: bool):
        if is_down:
            self.keys_down.add(key)
        else:
            self.keys_down.discard(key)

    def is_down(self, key):
        return key in self.keys_down
