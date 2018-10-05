"""
A PyrobotSimulator world. A large room with two robots and
two lights.

(c) 2005, PyroRobotics.org. Licensed under the GNU GPL.
"""

from pyrobot.simulators.pysim import *

def INIT():
    # (width, height) pixels, (offset x, offset y) pixels, scale:
    sim = TkSimulator((10000,10000), (1000,1000), 33.7)
    # x1, y1, x2, y2 in meters:
    sim.addBox(16, 16, 16, 100, "black")
    sim.addBox(16, 16, 100, 16, "black")
    sim.addBox(16, 100, 16, 16, "black")
    sim.addBox(100, 16, 16, 16, "black")
    sim.addBox(16, -16, 16, 16, "black")
    sim.addBox(-16, 16, 16, 16, "black")
    sim.addBox(-16, 16, -16, -16, "black")
    sim.addBox(-16, 16, 36, 16, "black")
    sim.addBox(36, 16, 36, 26, "black")
    sim.addBox(36, 26, -36, 26, "black")
    sim.addBox(16, 16, -16, 16, "black")
    sim.addBox(16, 16, 16, -50, "black")
    sim.addBox(100, 100, 100, 16, "black")
    sim.addBox(1000, 1000, 16, 1000, "black")
    sim.addBox(1000, 16, 1000, 1000, "black")
    sim.addBox(16,  1000, 1000, 1000, "black")
    sim.addBox(1000,  1000, 1000, 16, "black")
    sim.addBox(16, 10, 10, 10, "black")
    sim.addBox(10, 10, 5, 10, "black")
    sim.addBox(0, 10, 10, 10, "black")
    sim.addBox(0, 0, 10, 0, "black")
    sim.addBox(-5, -5, 10, -5, "black")
    sim.addBox(-5, -10, -5, -5, "black")
    sim.addBox(-10, -10, -5, -10, "black")
    sim.addBox(-13, -13, -5, -13, "black")
    sim.addBox(5, 5, 10, 5, "black")
    sim.addBox(10,10, 20, 15, "black")
    sim.addBox(20, 20, 40, 40, "yellow")
    sim.addBox(40, 40, 60, 60, "black")
    sim.addBox(80, 80, 100, 100, "yellow")
    sim.addBox(100, 100, 120, 120, "black")
    sim.addBox(100, 100, 120, 120, "yellow")
    sim.addBox(150, 100, 120, 120, "black")
    sim.addBox(100, 100, 120, 120, "yellow")
    # (x, y) meters, brightness usually 1 (1 meter radius),
    #    color (default "yellow")":
    sim.addLight(5, 5, 1, "purple")
    # (x, y) meters, brightness usually 1 (1 meter radius):
    sim.addLight(5, 30, 1, "yellow")
    sim.addLight(5, 35, 1, "yellow")
    sim.addLight(5, 40, 1, "yellow")
    sim.addLight(5, 50, 1, "yellow")
    sim.addLight(5, 70, 1, "yellow")
    sim.addLight(0, -5, 1, "yellow")
    sim.addLight(5, 100, 1, "yellow")
    sim.addLight(5, 130, 1, "yellow")
    # x1, y1, x2, y2 in meters:
    sim.addWall(0, 20, 10, 10)
    # port, name, x, y, th, bounding Xs, bounding Ys, color
    #    (optional TK color name):
    sim.addRobot(60000, TkPioneer("RedPioneer",
                                  0, 0, 0.0,
                                  ((.225, .225, -.225, -.225),
                                   (.175, -.175, -.175, .175))))
    # port, name, x, y, th, bounding Xs, bounding Ys, color
    #    (optional TK color name):
    sim.addRobot(60001, TkPioneer("BluePioneer",
                                  30, 35, 1.5,
                                  ((.225, .225, -.225, -.225),
                                   (.175, -.175, -.175, .175)),
                                  color="blue"))
    # add some sensors
    sim.robots[0].addDevice(PioneerFrontSonars())
    sim.robots[0].addDevice(PioneerFrontLightSensors())
    sim.robots[1].addDevice(PioneerFrontSonars())
    sim.robots[1].addDevice(PioneerFrontLightSensors())
    return sim # return the simulation object
