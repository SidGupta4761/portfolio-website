---
title: IoT Soil-Moisture Monitor
tags:
  - Miscellaneous
# Month-level sorting anchor: ETSD January term 2025; exact day unknown.
publishDate: 2025-01-01
img: /assets/etsd_cover.jpeg
img_alt: A Raspberry Pi Pico W soil-monitoring prototype with a breadboard, LCD, sensor wiring, and laptop.
description: |
  A Raspberry Pi Pico W prototype that displays soil-moisture readings and sends a phone alert when they fall below a set threshold.
---

I built this soil-moisture monitor during NCSSM's January 2025 ETSD term. The goal was straightforward: check a sensor reading locally and receive a phone alert when the soil became too dry.

A Raspberry Pi Pico W reads the moisture sensor and displays information on an LCD. Its Wi-Fi connection triggers IFTTT, an automation service, to send a notification when the reading falls below a specified threshold.

## Prototype demonstration

The video shows the LCD and phone notifications working together. For this demonstration, the probe was left out of the soil, so its low-moisture reading repeatedly triggered the alert. This demonstrates the notification path; calibration and sustained testing in soil would be the next steps toward a useful plant-monitoring system.

<figure>
  <video controls playsinline preload="none" width="600" aria-describedby="soil-monitor-caption">
    <source src="/assets/etsd_demo.mp4" type="video/mp4" />
    <a href="/assets/etsd_demo.mp4">Watch the soil-moisture monitor demonstration.</a>
  </video>
  <figcaption id="soil-monitor-caption">A low sensor reading triggering a phone notification while the LCD displays local information.</figcaption>
</figure>
