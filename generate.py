import pyrosim.pyrosim as ps

#size
l=1.5
w=2
h=1.5

#position
x=0
y=0
z=1.5

def robot_world():
    ps.Start_URDF("body.urdf")
    ps.Send_Cube(name="segment1", pos=[x,y,z], size=[l,w,h])
    ps.Send_Joint(name="segment1_segment2", parent="segment1", child="segment2", type="revolute", position=[1.5,0.0,1.5])
    ps.Send_Cube(name="segment2", pos=[0.0,0.0,0.0], size=[l,w,h])
    ps.Send_Joint(name="segment2_segment3", parent="segment2", child="segment3", type="revolute", position=[1.5,0.0,0])
    ps.Send_Cube(name="segment3", pos=[0.0,0.0,0.0], size=[l,w,h])
    ps.Send_Joint(name="segment3_segment4", parent="segment3", child="segment4", type="revolute", position=[1.5,0.0,0])
    ps.Send_Cube(name="segment4", pos=[0.0,0.0,0.0], size=[l,w,h])
    ps.Send_Joint(name="segment4_segment5", parent="segment4", child="segment5", type="revolute", position=[1.5,0.0,0])
    ps.Send_Cube(name="segment5", pos=[0.0,0.0,0.0], size=[l,w,h])
    ps.Send_Joint(name="segment5_segment6", parent="segment5", child="segment6", type="revolute", position=[1.5,0.0,0])
    ps.Send_Cube(name="segment6", pos=[0.0,0.0,0.0], size=[l,w,h])
    ps.End()

robot_world()