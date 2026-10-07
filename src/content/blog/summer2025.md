---
title: ROS 2 and Gazebo - From First Nodes to Navigation
tags:
  - Simulation
# Original WordPress post date; see README.md for sources.
publishDate: 2025-06-27
img: /assets/ros_blog_cover.png
img_alt: Gazebo simulation and RViz side by side, showing a robot navigating a mapped environment.
description: |
  A summer learning project that progressed from ROS 2 fundamentals to sensor-based obstacle avoidance and autonomous TurtleBot3 navigation.
---

In summer 2025, I started learning ROS 2 to connect my mechanical design experience with robot software. I had seen the Zebracorns use it for simulation and autonomous behavior, and wanted to understand the system well enough to build my own experiments.

I set up a dual-boot Linux environment and worked through ROS 2 Jazzy and Gazebo Harmonic tutorials. ROS 2 handles communication between pieces of robot software; Gazebo supplies a simulated world where I could try those pieces without physical hardware.

## Starting with motion and coordinate frames

My first experiments focused on nodes, messages, and coordinate frames: how one part of the software communicates with another, and how a robot keeps track of positions. A follower-turtle demo made that tangible by using TF2 transforms to track a leader's pose.

<iframe width="560" height="315" src="https://videopress.com/embed/Qn01LZer" title="ROS 2 follower turtle tracking a leader using coordinate transforms" frameborder="0" loading="lazy" allowfullscreen allow="clipboard-write"></iframe>

I also drove an animated actor around a square path in Gazebo, using velocity commands and a simple behavior loop.

<iframe width="560" height="315" src="https://videopress.com/embed/KgFIfR13" title="Gazebo actor following a square path through ROS 2 velocity commands" frameborder="0" loading="lazy" allowfullscreen allow="clipboard-write"></iframe>

## Giving the robot something to react to

Next, I wrote a C++ node that read simulated LiDAR range data and steered a vehicle away from nearby walls. It was a small exercise, but it connected the full loop: a sensor measurement, a decision in code, and a motion command back to the robot.

<iframe width="560" height="315" src="https://videopress.com/embed/Etdl2a13" title="Simulated vehicle avoiding walls using LiDAR data and a C++ ROS 2 node" frameborder="0" loading="lazy" allowfullscreen allow="clipboard-write"></iframe>

## Building up to autonomous navigation

Using Nav2 and ROBOTIS TurtleBot tutorials, I assembled a TurtleBot3 navigation demo with mapping, localization, path planning, and obstacle avoidance. Getting it running involved plenty of troubleshooting around sensor topics, coordinate transforms, and process startup. Seeing the robot reach a goal on its own made those pieces feel like one system.

<iframe width="560" height="315" src="https://videopress.com/embed/TFlmDW1Y" title="TurtleBot3 navigating to goals with mapping and obstacle avoidance" frameborder="0" loading="lazy" allowfullscreen allow="clipboard-write"></iframe>

<script src="https://videopress.com/videopress-iframe.js"></script>

<figure>
  <img src="/assets/rqt.png" alt="An rqt graph showing connections between ROS 2 nodes and message topics." loading="lazy" />
  <figcaption>Inspecting the connections between nodes helped me understand and debug the navigation system.</figcaption>
</figure>

These were tutorial-based learning projects, with my own experiments built on top. They gave me a foundation in ROS 2, simulated sensors, and debugging that I now draw on in [my robotics and simulation work](/about/#experience). The original longer-term ideas included custom drivetrains, Isaac Sim, and integrating my [cycloidal gearmotor concept](/blog/cycloidal_proposal/) into a simulation workflow.
