from OpenGL.GL import *

def draw_textured_quad(size_x=1.0, size_z=1.0, uv_scale=1.0):
    hx = size_x / 2.0
    hz = size_z / 2.0
    glBegin(GL_QUADS)
    glNormal3f(0.0, 1.0, 0.0)
    glTexCoord2f(0.0, 0.0);        glVertex3f(-hx, 0.0, -hz)
    glTexCoord2f(uv_scale, 0.0);   glVertex3f( hx, 0.0, -hz)
    glTexCoord2f(uv_scale, uv_scale); glVertex3f( hx, 0.0,  hz)
    glTexCoord2f(0.0, uv_scale);   glVertex3f(-hx, 0.0,  hz)
    glEnd()

def draw_cube(w=1.0, h=1.0, d=1.0):
    hx, hy, hz = w/2.0, h/2.0, d/2.0

    glBegin(GL_QUADS)
    # Front (+Z)
    glNormal3f(0,0,1)
    glTexCoord2f(0,0); glVertex3f(-hx,-hy, hz)
    glTexCoord2f(1,0); glVertex3f( hx,-hy, hz)
    glTexCoord2f(1,1); glVertex3f( hx, hy, hz)
    glTexCoord2f(0,1); glVertex3f(-hx, hy, hz)

    # Back (-Z)
    glNormal3f(0,0,-1)
    glTexCoord2f(0,0); glVertex3f( hx,-hy,-hz)
    glTexCoord2f(1,0); glVertex3f(-hx,-hy,-hz)
    glTexCoord2f(1,1); glVertex3f(-hx, hy,-hz)
    glTexCoord2f(0,1); glVertex3f( hx, hy,-hz)

    # Right (+X)
    glNormal3f(1,0,0)
    glTexCoord2f(0,0); glVertex3f( hx,-hy, hz)
    glTexCoord2f(1,0); glVertex3f( hx,-hy,-hz)
    glTexCoord2f(1,1); glVertex3f( hx, hy,-hz)
    glTexCoord2f(0,1); glVertex3f( hx, hy, hz)

    # Left (-X)
    glNormal3f(-1,0,0)
    glTexCoord2f(0,0); glVertex3f(-hx,-hy,-hz)
    glTexCoord2f(1,0); glVertex3f(-hx,-hy, hz)
    glTexCoord2f(1,1); glVertex3f(-hx, hy, hz)
    glTexCoord2f(0,1); glVertex3f(-hx, hy,-hz)

    # Top (+Y)
    glNormal3f(0,1,0)
    glTexCoord2f(0,0); glVertex3f(-hx, hy, hz)
    glTexCoord2f(1,0); glVertex3f( hx, hy, hz)
    glTexCoord2f(1,1); glVertex3f( hx, hy,-hz)
    glTexCoord2f(0,1); glVertex3f(-hx, hy,-hz)

    # Bottom (-Y)
    glNormal3f(0,-1,0)
    glTexCoord2f(0,0); glVertex3f(-hx,-hy,-hz)
    glTexCoord2f(1,0); glVertex3f( hx,-hy,-hz)
    glTexCoord2f(1,1); glVertex3f( hx,-hy, hz)
    glTexCoord2f(0,1); glVertex3f(-hx,-hy, hz)
    glEnd()
