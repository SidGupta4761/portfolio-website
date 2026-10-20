---
title: iOrganBio Reflection
tags:
  - Mechatronics
  - Lab Automation
  - Python
publishDate: 2026-10-06
img: /assets/cellforge.png
img_alt: iOrganBio's CellForge platform.
description: |
  Eight months working across Python, lab automation, and hardware as a mechatronics intern at iOrganBio.
---

**Confidentiality note:** Photos and videos of my work, source code, technical designs, and other proprietary information are iOrganBio's intellectual property, so I cannot share them publicly on this website. This reflection focuses on my experience and general engineering lessons, with company-specific implementation details omitted.

From January through August 2026, I worked at iOrganBio as a mechatronics intern. I joined part time during the semester, from January to May, and returned full time for the second half of the summer. The internship brought together a lot of what I enjoy about engineering: writing software, working with physical systems, and figuring out how to make both useful to the people operating them.

My main contributions were in **Python-based lab automation and hardware development**. I worked on making repetitive laboratory tasks easier to carry out and supporting the scientists who used the equipment. It was an opportunity to think about both the technical behavior of a system and the experience of the person operating it.

[iOrganBio](https://iorgan.bio/) is a biotech startup in North Carolina's Research Triangle working on more consistent, scalable production of human cells and organoids, which are three-dimensional cell cultures that model aspects of tissue biology. Working in that setting gave me a new perspective on how mechatronics can support biological research.

## Learning the robot and its software

My first month focused on learning [PyLabRobot](https://docs.pylabrobot.org/), an open-source Python framework for laboratory automation, and getting familiar with liquid-handling equipment. That meant learning how software represented physical equipment while getting familiar with the equipment itself.

Liquid-handling robots automate picking up pipette tips, drawing up liquids, and dispensing them into tubes or plates. Learning to work with them helped me appreciate how much reliable automation depends on understanding the physical equipment, as well as the software controlling it.

Learning tools such as the [PyLabRobot Visualizer](https://docs.pylabrobot.org/stable/user_guide/machine-agnostic-features/using-the-visualizer.html) helped me understand the relationship between a software model and physical hardware. Moving from a representation to real equipment was an important part of learning; a software visualization still needs to be checked against the actual setup.

PyLabRobot's [resource abstractions](https://docs.pylabrobot.org/stable/resources/introduction.html) were a particularly interesting bridge between mechanical design and software. These definitions describe physical dimensions and the positions of resources relative to one another. They reinforced a general lesson: a robot's understanding of a part depends on how accurately that part is represented in code.

## Turning experimental plans into usable automation

Over the semester, I became more comfortable translating laboratory needs into automation requirements. Understanding what a scientist needed to accomplish was just as important as understanding what the equipment could do.

The challenge extended beyond getting a robot to perform a task. I learned to pay closer attention to preparation, clear instructions, and how an operator would interact with the system. Those considerations shaped how I approached usability in my work.

This changed how I thought about usability in automation. The operator's preparation is part of the system, alongside the code and the robot. A useful workflow needs to connect all three: what the scientist wants to make, what they need to load, and what the hardware will execute.

## Working across software, controls, and mechanical design

Alongside liquid handling, I gained experience with feedback control, sensing, and mechanical design. Working across those areas gave me another opportunity to connect control software with the behavior of physical hardware.

I also spent time thinking about how mechanical choices affect ease of use. These tasks made the role feel very much like mechatronics: I could move between Python, a controls problem, and the geometry of a mechanism, while considering how each would affect the person using it.

## Building with a growing startup

I worked with people across engineering, science, software, and company leadership. Each brought a different perspective on the same system, from the biological experiment to software integration and hardware operation. Keeping those perspectives aligned became a substantial part of the work.

As an intern, that environment pushed me to ask more precise questions and explain my work to people outside my own technical background. A change that looked small from one perspective could affect several other parts of the workflow. I learned to think through those connections and communicate them as the implementation evolved.

When I returned full time for the second half of the summer, I continued building on what I had learned during the semester. Explaining my work to people with different backgrounds helped me connect engineering decisions to their practical value and communicate more clearly.

## What I took away

One of the most rewarding parts of the internship was seeing my confidence grow from my first experiences with lab automation in January to more independent engineering work by August. I became better at asking useful questions, checking assumptions against real hardware, and thinking about how someone else would use what I built.

I left with stronger skills in Python-based lab automation, feedback control, mechanical design, and interdisciplinary communication. More than anything, the experience reinforced why I enjoy mechatronics: I like working across the boundaries between software and hardware, then seeing that work become something another person can use. I'm excited to carry that approach into future robotics, controls, and automation projects.
