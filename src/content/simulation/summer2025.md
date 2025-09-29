---
title: (Blog) Diving into ROS 2 and Simulation
tags:
  - Simulation
publishDate: 2020-03-04 00:00:00
img: /assets/ros_blog_cover.png
img_alt: cover pic
description: |
  My Summer 2025 learning journey!
---

Over the past few weeks of summer break, I’ve been diving deep into ROS 2 and Gazebo simulation to sharpen my robotics software skills. After hearing about ROS from my old robotics team, The Zebracorns, and seeing how powerful it was for things like swerve drive simulation and autonomous behavior, I finally took the plunge myself. I started by setting up a dual-booted Linux environment and working through the ROS 2 Jazzy tutorials. That covered everything from the command line tools and client libraries to writing basic nodes, publishing and subscribing, working with TF2 frames, and visualizing data in RViz. I also explored rqt for GUI-based debugging and learned how to log and replay data using bag files.

Once I had the core ROS tools down, I moved into the world of simulation with Gazebo Harmonic, learning the basics of SDF files, sensor configuration (mostly LIDAR), and how to spawn and control models through ROS 2. One of my first fun experiments was building on the TF2 examples, where I created a demo where a “follower” turtle tracked a “leader” turtle’s pose by subscribing to its transform. Watching the second turtle move to mirror the first in real time with RViz gave me a tangible sense of how ROS handles spatial transforms and frame graphs.

<iframe width="560" height="315" src="https://videopress.com/embed/Qn01LZer" frameborder="0" allowfullscreen allow="clipboard-write"></iframe>
<script src="https://videopress.com/videopress-iframe.js"></script>

I also tried scripting some basic actor behavior in Gazebo. Using ROS 2 to drive an animated actor along a square path, I got to explore simple velocity command publishing and behavior loops inside simulation. It’s a relatively small example, but it gave me a hands-on feel for how simulated humans or vehicles could be integrated into larger testing environments for planning or perception.

<iframe width="560" height="315" src="https://videopress.com/embed/KgFIfR13" frameborder="0" allowfullscreen allow="clipboard-write"></iframe>
<script src="https://videopress.com/videopress-iframe.js"></script>

Another highlight was a LIDAR-based wall avoidance routine. I spawned a vehicle in a basic world and wrote a C++ node to read LIDAR data and steer it away from nearby obstacles. This gave me a chance to connect sensor input with real-time control, and to reinforce how ROS messages flow between simulated sensors, processing nodes, and actuators.

<iframe width="560" height="315" src="https://videopress.com/embed/Etdl2a13" frameborder="0" allowfullscreen allow="clipboard-write"></iframe>
<script src="https://videopress.com/videopress-iframe.js"></script>

By the third week, I upgraded to a new desktop build—mainly to unlock heavier simulation workloads and prep for future mechatronics and controls projects. That extra power really paid off when I tackled ROS 2 Navigation (Nav2). Based off the Nav2 and ROBOTIS Turtlebot tutorials, I worked up to a full TurtleBot3 demo navigating through a simulated world with SLAM, global planning, and local control. Getting the full pipeline running required a lot of troubleshooting, especially around sensor topics, transform frames, and process management, but it was worth it to see the robot autonomously navigate to goals with obstacle avoidance in place.

<iframe width="560" height="315" src="https://videopress.com/embed/TFlmDW1Y" frameborder="0" allowfullscreen allow="clipboard-write"></iframe>
<script src="https://videopress.com/videopress-iframe.js"></script>

![Alt text](/assets/rqt.png)

Looking ahead, I’m planning to experiment with swapping out TurtleBot’s drivetrain in simulation for a more complex custom one of my own design—something closer to what I’d actually build, but still compatible with ROS’s sensor and localization stack. I also want to start exploring NVIDIA Isaac Sim, especially for photorealistic perception simulation and tighter GPU integration. Eventually, I plan to bring in one of my personal long-term hardware projects: the cycloidal motor, a compact, high-reduction gearmotor concept I’ve been developing. The goal is to build out its kinematics, simulate it under load, and integrate it into a full ROS-based workflow. This summer has been all about building the foundation, and now I’m excited to push it further.

