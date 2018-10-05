from pyrobot.simulators.pysim import *
import math

def INIT():
    # (width, height), (offset x, offset y), scale:
    sim = TkSimulator((850, 850), (850, 850), 32)
    # x1, y1, x2, y2 in meters:
    sim.addBox(0, 25.7, 13, 25.9, "black")
    sim.addBox(0, 4.27, 5.45, 4.72, "black")
    sim.addBox(0, 4.72, 6.39, 21.34, "black")
    sim.addBox(11.22, -0.2, 13, 2.01, "black")
    sim.addBox(2.38, 0, 3.35, 0.76, "black")
    sim.addBox(3.65, 0, 6.39, 2.01, "black")
    sim.addBox(9.66, 24.26, 13, 25.7, "black")
    sim.addBox(5, 23.88, 6.39, 24.26, "black")
    # chair
    sim.addBox(10.2, 2.7, 11.1, 3.6, "blue", wallcolor="blue")
    # sofa
    sim.addBox(11.42, 3.55, 13, 4.45, "blue", wallcolor="blue")

    # port, name, x, y, th, bounding Xs, bounding Ys, color
    # (optional TK color name):

    sim.addRobot(60000, TkPioneer("RedPioneer", 7, 21, -180 * math.pi / 180, ((0.225, 0.225, -0.225, -0.225), (0.175, -0.175, -0.175, 0.175))))
    sim.addRobot(60001, TkPioneer("GreenMyro",8, 21, -180 * math.pi / 180, ((0.225, 0.225, -0.225, -0.225), (0.175, -0.175, -0.175, 0.175))))
    sim.addRobot(60002, TkPioneer("BlueMyro", 9, 21, -180 * math.pi / 180, ((0.225, 0.225, -0.225, -0.225), (0.175, -0.175, -0.175, 0.175))))
    # add some sensors:
    sim.robots[0].addDevice(PioneerFrontSonars())
    sim.robots[1].addDevice(PioneerFrontSonars())
    sim.robots[2].addDevice(PioneerFrontSonars())
    return sim