---
title: Suspended Swerve Rover Concept
tags:
  - Simulation
# Month-level sorting anchor: latest project month in resume (September 2025-May 2026).
publishDate: 2026-05-01
img: /assets/rover_top.png
img_alt: CAD rendering of the rover's tubular chassis and four independent pushrod suspension assemblies.
description: |
  An experimental rover concept combining four steerable wheel modules with independent suspension, developed for terrain testing in simulation.
---

This project explores a rover drivetrain with four independently steerable wheels and suspension at each corner. The goal is to study whether combining swerve steering with long suspension travel could help a rover maneuver over uneven terrain and through confined spaces.

Swerve steering lets each wheel choose its own direction, allowing the vehicle to move sideways as well as forward. The suspension concept uses double wishbones to guide wheel motion and pushrods to transfer that motion to springs and dampers positioned farther inside the chassis.

## Suspension and packaging

I developed the chassis, suspension, and coaxial swerve modules using master sketches, 3D sketches, and weldments. The design combines an aluminum/steel tube chassis with 7075 aluminum suspension and swerve components, QA1 coilovers with 350 lb/in springs, and AKM42C servomotors.

The CAD geometry targets ±150 mm of suspension travel, a ±5° camber range, and approximately 500 mm of ground clearance. These are design targets to evaluate under load and in simulation. Locating the spring and damper inboard is intended to reduce their exposure to the terrain.

<figure>
  <img src="/assets/master_geo.png" alt="Three-dimensional master sketch defining the rover chassis and suspension mounting geometry." loading="lazy" />
  <figcaption>The master geometry used to coordinate the chassis and four suspension assemblies.</figcaption>
</figure>

<figure>
  <img src="/assets/suspension_geo.png" alt="Side-view sketch of the rover suspension linkage and wheel travel geometry." loading="lazy" />
  <figcaption>Suspension geometry for studying linkage motion and packaging.</figcaption>
</figure>

## Simulation and next steps

The validation work is in progress. My plan is to bring the assembly into NVIDIA Isaac Sim through URDF and USD model formats, then connect its joints to ROS 2 controllers and Isaac Action Graphs. This would let me test steering, suspension response, and vehicle behavior in a simulated Mars environment.

Terrain mapping with simulated RTX LiDAR and autonomous navigation are planned extensions. The important next step is to compare the design's intended motion with its behavior under representative loads and terrain conditions.
