---
title: Suspended Swerve Concept for Mars Rover
tags:
  - Simulation
publishDate: 2020-03-04 00:00:00
img: /assets/rover_top.png
img_alt: cover pic
description: |
  An innovative rover drivetrain concept designed to explore farther than any rover ever could before.
---

Over the years, numerous rovers have been sent to the Moon and Mars, but all of them have been limited in their mobility. For example, we have not yet been able to venture into craters or down ravines. We are at a juncture in planetary exploration technology where we can transition from the conventional rocker bogie suspension rover design and start employing more unconventional designs.

This concept employs independent double-wishbone pushrod suspension for each of the 4 swerve modules at each corner. This combination of terrain adaptability and holonomic motion enables this drivetrain to traverse like a conventional rover, and when necessary, travel up and down steep inclines, and navigate tight and rough terrain not possible with traditional 6-wheeled rocker-bogie design.

![Alt text](/assets/master_geo.png)
![Alt text](/assets/suspension_geo.png)

This will be validated using simulation in NVIDIA Isaac Sim, by importing the final assembly over as a URDF (unified robot description format), then USD (universal scene description, used by NVIDIA OMniverse tools). This enables full joint articulation and control, using a combination of custom and existing ROS packages, and Isaac Action Graphs for teleoperated control. The environment will be a USD of harsh Mars terrains, and in the future, I also plan to implement 3d mapping and navigation with RTX LiDAR and packages similar to Nav2.

Here is a bulleted list of some key design features:
- Designed experimental Mars rover drivetrain with welded aluminum/steel tube chassis, 4 coaxial swerve modules, and pushrod double-wishbone suspension for extreme terrain exploration (caves, volcanoes).
- Applied 3D sketches, weldments, master sketching to design chassis, suspension, and coaxial swerve modules; used 350 lb/in 12-12.5” ride height QA1 coilovers, AKM42C servomotors, and half-pocketed 7075 billet for suspension and swerve components.
- Engineered pushrod double-wishbone suspension with ±150 mm travel and ±5° camber range; achieved 500 mm ground clearance and protected spring/damper from exposure to extreme terrain.
- (In progress) Simulated rover behavior in NVIDIA Isaac Sim (PhysX) and controlled via ROS2, using action graphs, custom nodes, and swerve steering controllers to validate swerve drivetrain performance and suspension dynamics in Mars terrain and gravity.

