import time
import numpy as np
import mujoco
import mujoco.viewer

def action(model, data, u):
    data.actuator('motor').ctrl[0] = u

gear = 1.0
def get_angle(model, data):
    angle = data.actuator('motor').length[0]/gear
    return angle

def get_velocity(model, data):
  velocity = data.actuator('motor').velocity[0]/gear
  return velocity

def get_trque(model, data):
  trque = data.actuator('motor').force[0]
  return trque



paused = False
def key_callback(keycode):
  if chr(keycode) == ' ':
    global paused
    paused = not paused

#Create model
model = mujoco.MjModel.from_xml_path('motor_test.xml')
data = mujoco.MjData(model)


#Get ID
#wheel_left_id = mujoco.mj_name2id(model, 3,'left wheel joint')
#print('#Left Front Sensor ID',  lf_id)

#Main Loop
now = 0.0
past = 0.0
turn_flag = 0
with mujoco.viewer.launch_passive(model, data, key_callback=key_callback) as viewer:
  while viewer.is_running():
    if not paused:
        #Move
        action(model, data, 0.15)
        #Simulation
        mujoco.mj_step(model, data)
      
        #Vizualize
        now = data.time
        if now-past>0.001:
            past = now   
            viewer.sync()

            #Sensor Data Show
            #print(now, ax, ay, az, gx, gy, gz)
            #print(lf,ls,rs,rf)
            #print(data.sensordata)
            print(now, data.sensor('sensor').data[2])
            #print(now,\
            #      data.actuator('right').length[0],   data.actuator('left').length[0],\
            #      data.actuator('right').velocity[0], data.actuator('left').velocity[0],\
            #      ax, ay, az, gx, gy, gz)
            #print(now, mx, my, psi, deff_length)