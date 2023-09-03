Simultaneous Localization and Mapping (SLAM) is a crucial technique enabling robots to construct maps of their surroundings while determining their own position. This is achieved by leveraging sensors to monitor the robot's movement and identifying landmarks in the environment. SLAM plays a vital role in various applications, such as planetary exploration by rovers, ensuring safe navigation and obstacle avoidance.

For example, the Curiosity rover relies on a combination of visual SLAM and LiDAR SLAM to map its Martian environment. Visual SLAM employs a camera to track the rover's movements, while LiDAR SLAM utilizes a laser to measure distances to nearby objects. These measurements collectively create a detailed map of the rover's surroundings, enhancing its navigation capabilities and obstacle avoidance.

Similarly, the Perseverance rover also utilizes a SLAM system akin to Curiosity's but adds a laser altimeter for terrain height measurements. This additional data aids in path planning and helps the rover avoid steep slopes.

Even the Ingenuity helicopter on Mars employs SLAM for navigation. Its SLAM system utilizes a downward-facing camera to track its movements and generate a terrain map. This information guides the helicopter's flight path and ensures obstacle avoidance.

SLAM stands as a powerful tool, enabling robots to autonomously explore their surroundings safely, making it indispensable for planetary rovers and beyond.

In the realm of SLAM, there are several noteworthy approaches:

- **EKF SLAM:** This method employs an Extended Kalman Filter to estimate both the robot's pose and the environmental map. While it is straightforward and accurate, it can become computationally demanding for larger maps.

- **Particle Filter SLAM:** This technique utilizes a set of particles to represent the robot's pose and the environmental map. It offers robustness while being less computationally intensive than EKF SLAM, although it may sacrifice some accuracy.

- **Graph-based SLAM:** This approach employs a graph to represent the robot's pose and the environmental map. It provides flexibility to handle intricate environments, although its implementation can be more challenging.

Here's a summary of the three algorithms:

| Algorithm             | Pros                         | Cons                                      |
|-----------------------|------------------------------|-------------------------------------------|
| EKF SLAM              | Simple and accurate           | Computationally expensive for large maps  |
| Particle Filter SLAM  | Robust with lower computation | Slightly less accurate                    |
| Graph-based SLAM      | Flexible and adaptable        | More complex to implement                 |

The choice of which algorithm to use depends on the specific application. If precision is paramount, EKF SLAM is a solid option. If robustness is a priority, Particle Filter SLAM is a suitable choice. For applications requiring flexibility, Graph-based SLAM can be the preferred solution.
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
