---
title: 3D-Printed Differential Swerve Module
tags:
  - Miscellaneous
# Project date unconfirmed; omitted rather than using the old 2020 placeholder.
img: /assets/diffy_module.png
img_alt: CAD rendering of a compact differential swerve module with green gears surrounding the wheel.
description: | 
  A compact wheel module exploring how a differential mechanism can share motor power between driving and steering.
---

A swerve module lets a robot wheel both roll and change its steering direction. This design explores a differential arrangement that combines motor inputs to control those two motions, with the aim of sharing available power between driving and steering.

I developed a 3D-printable CAD assembly to explore the mechanism's packaging and gear layout. The section view below shows how the gears and wheel fit together inside the module.

<figure>
  <img src="/assets/diffy_section.png" alt="Section view through the differential swerve module showing the wheel, gears, and supporting bearings." loading="lazy" />
  <figcaption>A cutaway of the module's internal construction.</figcaption>
</figure>

I shared the design on [GrabCAD](https://grabcad.com/library/ftc-differential-swerve-drive-1), where it passed 100 downloads. It is a module design; a complete drivebase and its control system remain next steps.

The next stage would be to build a drivebase, develop ROS-based control, and compare physical behavior with simulation. That would give me a way to evaluate steering response, drivetrain losses, and durability rather than judge the design from CAD alone.
