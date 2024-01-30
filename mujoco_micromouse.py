import time

import mujoco
import mujoco.viewer

def action(model, data, left, right):
    data.actuator('right').ctrl[0] = right
    data.actuator('left').ctrl[0] = left

def get_distance(model, data):
    lf = data.sensor('LF').data[0]#sensordata[lf_id]
    ls = data.sensor('LS').data[0]#sensordata[ls_id]
    rs = data.sensor('RS').data[0]#sensordata[rs_id]
    rf = data.sensor('RF').data[0]#sensordata[rf_id]
    return lf,ls,rs,rf

def get_accel(model, data):
  ax = data.sensor('Accel').data[0]
  ay = data.sensor('Accel').data[1]
  az = data.sensor('Accel').data[2]
  return ax,ay,az

def get_gyro(model, data):
  gx = data.sensor('Gyro').data[0]
  gy = data.sensor('Gyro').data[1]
  gz = data.sensor('Gyro').data[2]
  return gx,gy,gz

paused = False
def key_callback(keycode):
  if chr(keycode) == ' ':
    global paused
    paused = not paused

#Create model
model = mujoco.MjModel.from_xml_path('mouse_in_maze.xml')
data = mujoco.MjData(model)

gear = 0.3e-2
wheel_r = 0.0135

#Get ID
#wheel_left_id = mujoco.mj_name2id(model, 3,'left wheel joint')
#wheel_right_id = mujoco.mj_name2id(model, 3,'right wheel joint')
#wheel_ang_left = data.qpos[7]
#wheel_ang_right = data.qpos[8]
#actuator_right_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_ACTUATOR, 'right')
#actuator_left_id  = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_ACTUATOR, 'left')
#lf_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SENSOR, 'LF')
#ls_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SENSOR, 'LS')
#rs_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SENSOR, 'RS')
#rf_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SENSOR, 'RF')
#vel_y_id = 1 
#angle_id = 3

#touch1_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SENSOR, 'HB1')
#touch2_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SENSOR, 'HB2')
#accel_id  = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SENSOR, 'Accel')
#gyro_id   = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_SENSOR, 'Gyro')

#print('#Left Front Sensor ID',  lf_id)
#print('#Left Side Sensor ID',   ls_id)
#print('#Right Side Sensor ID',  rs_id)
#print('#Right Front Sensor ID', rf_id)
#print('#TOUCH1 ID', touch1_id)
#print('#TOUCH2 ID', touch2_id)
#print('#Accel ID', accel_id)
#print('#Gyro ID',  gyro_id)

#Main Loop
now = 0.0
past = 0.0
turn_flag = 0
with mujoco.viewer.launch_passive(model, data, key_callback=key_callback) as viewer:
  while viewer.is_running():
    if not paused:
      lf, ls, rs, rf = get_distance(model, data)
      ax, ay, az = get_accel(model, data)
      gx, gy, gz = get_gyro(model, data)

      #Control
      err = ls - rs
      velocity = 0.05
      k= 0.6
      if turn_flag==1 or (lf<0.05 and rf <0.05):
        turn_flag = 1
        right_mot =  0.06
        left_mot  = -0.06
        if lf > 0.09 and rf > 0.09:
          turn_flag = 0
        #print('Turn')
      else:
        right_mot = velocity + k * err
        left_mot =  velocity - k * err
        #print('Foward')

      #Move
      action(model, data, left_mot, right_mot)

      #Simulation
      mujoco.mj_step(model, data)
      
      #Vizualize
      now = data.time
      if now-past>0.01:
        past = now
        viewer.sync()
        #Sensor Data Show
        #print(now, ax, ay, az, gx, gy, gz)
        #print(lf,ls,rs,rf)
        #print(data.sensordata)
        #print(data.sensor('Gyro').data[0])
        print(now,\
              data.actuator('right').length[0],   data.actuator('left').length[0],\
              data.actuator('right').velocity[0], data.actuator('left').velocity[0],\
              ax, ay, az, gx, gy, gz)
      