import os
from PIL import Image
from OpenGL.GL import *

class TextureManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self._cache = {}

    def load(self, filename):
        if filename in self._cache:
            return self._cache[filename]

        path = os.path.join(self.base_dir, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Texture not found: {path}")

        img = Image.open(path).convert("RGBA")
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        data = img.tobytes()

        tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.size[0], img.size[1], 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, data)

        glBindTexture(GL_TEXTURE_2D, 0)
        self._cache[filename] = tex_id
        return tex_id
