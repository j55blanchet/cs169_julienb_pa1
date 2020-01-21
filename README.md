# PA1 - CS169
Julien Blanchet | Robotics Perception Systems | 1/21/20

<hr>

## Requirements
* Run on an Husarion ROSbot
* Ubuntu 16.04 with Kinetic

## Setup

This repository is intended to be a *single package* within a catkin repository. Therefore, you must use an exising catkin workspace or create a new one. Steps for setup:

1. Ensure that your catkin workspace has the following packages installed (these are necessary to control hardware of the)
    * [rosbot_webui](https://github.com/husarion/rosbot_webui.git robot) - Clone into your workspace
    * [husarion_ros](https://github.com/husarion/husarion_ros.git) - Clone into your workspace
    * [astra_launch](https://github.com/orbbec/ros_astra_launch) - Install using `sudo apt-get install ros-kinetic-astra*`

    
1. `cd` to the `src` folder of your catkin workspace
1. copy the contents of this repositrory into a folder titled `cs169_julienb_pa1` (this will be the package name)
1. Run `catkin_make` at the root of your workspace.

## Running
1. `roslaunch cs169_julienb_pa1 moveforward.launch` to execute task #1
1. `roslaunch cs169_julienb_pa1 datacollection.launch` to execute task #2
1. `roslaunch cs169_julienb_pa1 odomplotter.launch` to execute task #3 (note: run rviz on your local computer and add visualization markers to see the odom plot output)

