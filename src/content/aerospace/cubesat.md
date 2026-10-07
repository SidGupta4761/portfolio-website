---
title: CubeSat Classroom Flight Test
tags:
  - Aerospace
# Project date unconfirmed; omitted rather than using the old 2020 placeholder.
img: /assets/cubesat_cover.png
img_alt: The assembled classroom CubeSat with an aluminum frame, top-mounted solar panel, and internal electronics.
description: |
  Built, wired, and programmed a CubeSat-style classroom prototype, then collected synchronized camera and sensor data during a flight test.
---

For my senior-year Satellite Design class at NCSSM, I built and flight-tested a CubeSat-style prototype. The project brought mechanical assembly, wiring, sensing, and software into one small package.

The final assembly included a Raspberry Pi, battery pack, solar panel, camera, and inertial measurement unit (IMU). I wrote the telemetry software to record sensor readings alongside timestamped images, making it possible to connect what the camera saw with the prototype's measured motion.

## What the flight test showed

The final test captured ten images alongside acceleration and magnetic-field readings over roughly ten seconds. The presentation below includes the hardware layout, flight images, data table, and observations from the test.

One practical takeaway was that image timing and exposure settings deserved as much attention as the electronics. Collecting data is only useful if the images and measurements are clear enough to interpret together.

[Explore the telemetry code on GitHub](https://github.com/SidGupta4761/cubesat-fblock-group2/tree/main)

## Final presentation

[Open the flight-test presentation (PDF)](/assets/cubesat_final_slideshow.pdf)

<iframe
  src="/assets/cubesat_final_slideshow.pdf"
  title="CubeSat classroom prototype and final flight-test presentation"
  width="100%"
  height="600px"
  loading="lazy"
  style="border: none;"
></iframe>
