---
title: Configurable Sheet-Metal Bumpers
tags:
  - FIRST Robotics
# Original Chief Delphi post date (UTC); see README.md for source.
publishDate: 2023-10-24
img: /assets/bumpers.gif
img_alt: CAD animation of a robot chassis surrounded by two configurable sheet-metal-backed bumper sections.
description: |
  A publicly shared Onshape bumper configurator with six geometry inputs and quick-release mounts for FIRST Robotics Competition robots.
---

Robot bumpers are the padded structures around a competition robot's frame. I developed the Zebracorns' configurable two-piece assembly to make a recurring design task reusable across chassis and seasons, then shared it with the FIRST Robotics community.

## One model, multiple robot frames

Six Onshape inputs control frame width and length, frame-to-backing spacing, two split openings, and mounting height. A second variable studio derives the geometry with formulas, regenerating backing parts and assembly mates together.

The full sheet-metal backing supports the padded bumper assembly. Sliding tabs and spring pins allow quick replacement; the mounting hardware remains adaptable for frame gussets and other chassis features. The practical aim was to shorten repeat CAD work and produce fabrication quotes earlier during build season.

I documented the configurator and its setup in the [original Chief Delphi release](https://www.chiefdelphi.com/t/the-zebracorns-behind-the-stripes-design-code-and-build-blog-2023-2024/440094/11). One important setup detail: the `ground_clearance` input controls the height of the upper gussets, rather than the lower edge of the bumper. Its offset depends on the drivetrain's mounting arrangement. The original configuration was designed around the 2024 rules, so each adaptation needs a clearance and rules check.

## Public release and community use

More than 150 teams used this design. My contribution was the original configurable design and public release, including the CAD and configuration instructions shared with the community.

The project demonstrates a form of engineering impact I value: documenting a useful design so other teams can adapt the approach, rather than keeping the solution tied to one robot. It combines parametric CAD, assembly relationships, sheet-metal design, service access, and communication with a wider technical community.

[Open the configurable CAD in Onshape](https://cad.onshape.com/documents/3a3e250de05f1f4195603d03/w/2ff30d34a754fd8f94e2569d/e/8188f19f1adb79387bdd9945?renderMode=0&uiState=653712cdbe03c74c278eb831)
