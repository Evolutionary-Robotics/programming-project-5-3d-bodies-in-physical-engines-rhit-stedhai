import pybullet as p
import pybullet_data
import pyrosim.pyrosim as ps
import time
import numpy as np

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeID = p.loadURDF("plane.urdf")
#p.loadSDF("box.sdf")
robotId = p.loadURDF("body.urdf")
p.changeDynamics(robotId, 0, linearDamping=0, angularDamping=0, jointDamping=1.5)
p.changeDynamics(robotId, 1, linearDamping=0, angularDamping=0, jointDamping=1.0)
p.changeDynamics(robotId, 2, linearDamping=0, angularDamping=0, jointDamping=0.5)
p.changeDynamics(robotId, 3, linearDamping=0, angularDamping=0, jointDamping=1.0)
p.changeDynamics(robotId, 4, linearDamping=0, angularDamping=0, jointDamping=1.5)

x = np.linspace(0, np.pi*10, 10000)
y1 = (np.sin(x)+1)*np.pi/32
y2 = (np.sin(x)+1)*np.pi/16
y3 = (np.sin(x)+1)*np.pi/8

ps.Prepare_To_Simulate(bodyID=robotId)
for t in range(10000):
    ps.Set_Motor_For_Joint(bodyIndex=robotId, 
                           jointName = b'segment1_segment2', 
                           controlMode=p.POSITION_CONTROL, 
                           targetPosition=y1[t],
                           maxForce=500)
    ps.Set_Motor_For_Joint(bodyIndex=robotId, 
                           jointName = b'segment2_segment3', 
                           controlMode=p.POSITION_CONTROL, 
                           targetPosition=y2[t],
                           maxForce=1000)
    ps.Set_Motor_For_Joint(bodyIndex=robotId, 
                           jointName = b'segment3_segment4', 
                           controlMode=p.POSITION_CONTROL, 
                           targetPosition=y3[t],
                           maxForce=2000)
    ps.Set_Motor_For_Joint(bodyIndex=robotId, 
                           jointName = b'segment4_segment5', 
                           controlMode=p.POSITION_CONTROL, 
                           targetPosition=y2[t],
                           maxForce=1000)
    ps.Set_Motor_For_Joint(bodyIndex=robotId, 
                           jointName = b'segment5_segment6', 
                           controlMode=p.POSITION_CONTROL, 
                           targetPosition=y1[t],
                           maxForce=500)
    p.stepSimulation()
    time.sleep(1/750)

p.disconnect()