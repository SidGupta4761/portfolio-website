---
title: iOrganBio Reflection
tags:
  - Mechatronics
  - Lab Automation
  - Python
publishDate: 2026-10-06
img: /assets/iob-research/20260810_213720588_iOS.PNG
img_alt: iOrganBio's Hamilton Microlab STAR liquid-handling robot with plates, tip racks, and heater shakers on its deck.
description: |
  Eight months connecting Python, liquid-handling robots, and custom hardware to build an MES-driven media-preparation workflow at iOrganBio.
---

From January through August 2026, I worked at iOrganBio as a mechatronics intern. I joined part time during the semester, from January to May, and returned full time for the second half of the summer. The internship brought together a lot of what I enjoy about engineering: writing software, working with physical systems, and figuring out how to make both useful to the people operating them.

My main contribution was an **MES-driven media-preparation workflow that translated experimental condition matrices into automated Hamilton robot protocols**. Media are the nutrient mixtures used to grow cells; preparing different formulations is part of testing how culture conditions affect cell development. The workflow reduced scientist setup from approximately **1–3 days to 0.5–2 hours**, followed by 2–6 hours of autonomous robot execution. Those are separate parts of the process: the benefit was reducing the hands-on preparation required before the robot could take over.

[iOrganBio](https://iorgan.bio/) is a biotech startup in North Carolina's Research Triangle working on more consistent, scalable production of human cells and organoids, which are three-dimensional cell cultures that model aspects of tissue biology. Its CellForge platform combines automation, biological sensing, and AI-guided control to steer cell development toward defined targets. CellAtlas provides reference profiles of human cells and tissues to help define those targets and compare manufactured cells against them. Most of my work supported CellForge, particularly the automation connecting experimental plans to the physical lab.

The finer details of that work are proprietary, so this post focuses on my contributions, the tools I learned, and the engineering lessons I can share at a higher level.

## Learning the robot and its software

My first month focused on learning [PyLabRobot](https://docs.pylabrobot.org/), an open-source Python framework for laboratory automation, and using it with our Hamilton-compatible hardware. I helped lead the company's migration from Hamilton's VENUS software toward Python-based control with PyLabRobot. That meant learning how the software represented the equipment while getting familiar with the equipment itself.

I primarily worked with the [Hamilton Microlab STAR](https://www.hamiltoncompany.com/Microlab-STAR), a liquid-handling robot that automates picking up pipette tips, drawing up liquids, and dispensing them into tubes or plates. Its individual pipetting channels support flexible transfers, while its 96-channel head supports pipetting across a microplate in parallel. The surrounding hardware matters just as much: tips and tip racks, plates and their carriers, and heater shakers all have to fit into a coordinated workflow.

I used the [PyLabRobot Visualizer](https://docs.pylabrobot.org/stable/user_guide/machine-agnostic-features/using-the-visualizer.html) to simulate protocols and inspect the modeled deck and resource state. It gave me a way to follow what a protocol was doing before running it on the physical robot. Moving from that representation to real hardware was an important part of learning the system; a software visualization still needs to be checked against the actual setup.

<figure>
  <img src="/assets/iob-research/20260128_231822507_iOS.JPG" alt="A laptop displaying the PyLabRobot Visualizer beside the physical Hamilton STAR, showing the modeled deck alongside the robot's labware." width="3520" height="1980" loading="lazy" decoding="async" />
  <figcaption>The Hamilton STAR alongside its PyLabRobot deck visualization during my first month, January 2026.</figcaption>
</figure>

I also began defining custom plates, tubes, and adapters using PyLabRobot's [resource abstractions](https://docs.pylabrobot.org/stable/resources/introduction.html). These definitions describe physical dimensions and the positions of resources relative to one another. This was a particularly interesting bridge between mechanical design and software: the robot's understanding of a part depends on how accurately that part is represented in code.

## Turning experimental plans into usable automation

Over the semester, the media-preparation workflow became the center of my work. An experimental condition matrix describes the different combinations a scientist wants to test. My work translated that plan into liquid-handling protocols and connected it with the company's manufacturing execution system, or MES.

The challenge extended beyond getting the robot to perform transfers. A scientist also needed to prepare the deck and understand how the experimental plan mapped onto the run. I added load sheets and predefined deck layouts to make that setup easier to follow, while continuing to adapt the workflow to changing requirements and its integration with the MES.

This changed how I thought about usability in automation. The operator's preparation is part of the system, alongside the code and the robot. A useful workflow needs to connect all three: what the scientist wants to make, what they need to load, and what the hardware will execute.

## Working across software, controls, and mechanical design

Alongside liquid handling, I designed and integrated PID-controlled incubation systems for cell-culture workflows, incorporating environmental sensing and sterile operator access. PID control uses feedback from sensors to adjust a system toward a target condition. Working on those systems gave me another opportunity to connect control software with the behavior of physical hardware.

I also worked on mechanical details such as eccentric cam latches for incubator lids, with the aim of making them easier and faster to open, as well as miscellaneous hardware and adapters. These were smaller pieces of the platform, but they made the role feel very much like mechatronics: I could move between a Python protocol, an incubator control problem, and the geometry of a mechanism.

## Building with a growing startup

I worked with the main engineers, lead scientist, a senior software team member, and the CEO. Each brought a different perspective on the same system, from the biological experiment to software integration, hardware operation, and what we needed to demonstrate. Requirements changed quickly, and keeping those perspectives aligned became a substantial part of the work.

As an intern, that environment pushed me to ask more precise questions and explain my work to people outside my own technical background. A change that looked small from one perspective could affect several other parts of the workflow. I learned to think through those connections and communicate them as the implementation evolved.

When I returned full time for the second half of the summer, I continued developing media preparation while working with a team that had grown rapidly. I also presented my work in investor demonstrations and a major demonstration for GSK. Explaining the workflow to an external audience helped me connect the technical details to their practical value: what it enabled scientists to do and how it fit into CellForge.

<figure>
  <video controls playsinline preload="none" poster="/assets/iob-research/iorganbio-media-prep-poster.jpg" width="1280" height="720" aria-describedby="iorganbio-demo-caption">
    <source src="/assets/iob-research/iorganbio-media-prep.mp4" type="video/mp4" />
    <a href="/assets/iob-research/iorganbio-media-prep.mp4">Watch the Hamilton workflow demonstration.</a>
  </video>
  <figcaption id="iorganbio-demo-caption">An earlier development run from February 2026, showing the software execution and Hamilton pipetting hardware in action.</figcaption>
</figure>

## What I took away

One of the most rewarding parts of the internship was seeing the work evolve from my first experiments with PyLabRobot in January into a more complete workflow by August. The early work on resource definitions and robot control became part of a system that connected experimental planning, operator setup, and autonomous execution.

I left with stronger skills in Python-based lab automation, feedback control, mechanical design, and interdisciplinary communication. More than anything, the experience reinforced why I enjoy mechatronics: I like working across the boundaries between software and hardware, then seeing that work become something another person can use. I'm excited to carry that approach into future robotics, controls, and automation projects.
