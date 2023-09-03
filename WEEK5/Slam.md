
### Launch Simulation World
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_world.launch

### Run SLAM Node
#### To gmapping run , gotta do :
sudo apt-get install ros-melodic-slam-gmapping

export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

### Control the bot
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

### Saving the Map
rosrun map_server map_saver -f ~/map
