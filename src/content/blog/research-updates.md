---
title: Research Updates
tags:
  - Research
  - Robotics
publishDate: 2026-09-24
img: /assets/research-updates/maarco-thumbnail.jpg
img_alt: MAARCO’s twin-screw rover leaving tracks during a sand test.
description: |
  Catching up on hydrogel wave-energy harvesters, MAARCO rover field tests, and the experiments we’re working toward next at NC State.
---

Since joining research at NC State in fall 2025, I’ve been working on two projects that have taken me from a wave tank on the Outer Banks to muddy rover tests around Raleigh. One explores how soft materials can harvest energy from ocean waves; the other focuses on a robot designed to travel across difficult terrain. My [About page](/about/#experience) gives a quick overview of my involvement, but I wanted to share more about the ideas behind the work, what I’ve contributed, and the problems we’re still trying to solve.

The wave-energy work began with Dr. David Kim, then a postdoctoral researcher in NC State’s [Intelligent Structures and Systems Research Lab (iSSRL)](https://issrl.mae.ncsu.edu/). We started discussing frequency up-conversion for the lab’s DEEC-Tec project. That name stands for *distributed embedded energy converter technologies*: an approach that combines many small energy converters into a larger structure. For ocean energy, the idea is that a flexible structure can deform with passing waves, allowing converters throughout it to turn that motion into electricity. [This DEEC-Tec overview](https://research-hub.nlr.gov/en/publications/distributed-embedded-energy-converter-technologies-deec-tec/) explains how the individual converters fit into the larger system.

Our work builds on soft energy harvesters made with hydrogels, which are water-filled polymer networks. A useful starting point is the 2021 paper by Veenasri Vallem and colleagues, including NC State’s Dr. Michael Dickey, [*A Soft Variable-Area Electrical-Double-Layer Energy Harvester*](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202103142). Their device used liquid-metal electrodes encased in a hydrogel containing mobile ions. At the boundary between the metal and the gel, charges form an electrical double layer, which behaves like a capacitor. Deforming an electrode changes its surface area and capacitance, driving charge through an external circuit as the system rebalances. Repeated deformation and relaxation produce alternating current. The device can also operate underwater, making it particularly interesting for marine applications.

The frequency of that deformation matters. The prior work reported greater current response with increased mechanical input frequency, a finding also discussed in [Emily Duan’s NC State dissertation](https://repository.lib.ncsu.edu/bitstreams/cebd53af-21ff-4566-aea6-30137b32141f/download). This motivated our question: could relatively slow wave motion excite faster vibrations in a hydrogel sample? That is what we mean by *frequency up-conversion*. Higher current under the conditions of a published experiment does not guarantee higher useful power in our setup; we still need to understand how deformation, mechanical losses, and the electrical load affect the result.

The main approach David and I investigated uses magnets attached to the hydrogel and a separate array of magnets moving back and forth nearby. In the proposed wave-driven system, waves would also drive this reciprocating array. As successive magnets pass the sample, their changing forces would deflect and release it, with the aim of producing faster repeated motion than the underlying wave cycle. The magnets provide a way to transfer mechanical force to the sample; the hydrogel-based harvester converts the resulting deformation into electrical output.

We traveled to the wave tank at ECU’s Outer Banks campus to examine setups used in related DEEC-Tec projects from the lab. Seeing those experiments helped us think through how to test our own mechanism, but it also raised a practical question: how could we iterate without making a trip to the coast for every change?

We settled on a benchtop setup built around an APS shaker, a machine that supplies controlled back-and-forth motion. An extrusion mounted on the shaker would carry the reciprocating magnet array, while a lab stand would support the hydrogel fixture. Custom 3D-printed parts would retain the samples and neodymium coin magnets. This would let us work through changes in alignment, spacing, and mounting under repeatable conditions before returning to wave-tank testing.

<figure>
  <img src="/assets/research-updates/aps-shaker.jpg" alt="APS electrodynamic shaker mounted vertically on a lab frame." width="1200" height="1600" loading="lazy" decoding="async" />
  <figcaption>The APS shaker used to supply controlled motion for our benchtop experiments.</figcaption>
</figure>

<figure>
  <video controls playsinline preload="none" poster="/assets/research-updates/hydrogel-shaker-test-poster.jpg" width="1280" height="720" aria-describedby="hydrogel-test-caption">
    <source src="/assets/research-updates/hydrogel-shaker-test.mp4" type="video/mp4" />
    <a href="/assets/research-updates/hydrogel-shaker-test.mp4">Watch the hydrogel shaker test.</a>
  </video>
  <figcaption id="hydrogel-test-caption">A hydrogel sample during a shaker test as we explored its response to the benchtop setup.</figcaption>
</figure>

We also discussed ways to make the material itself respond to magnetic fields, including magnetic liquid metals (MLMs) and incorporating ferrofluids into the hydrogel formulation. Those were exploratory ideas alongside the discrete-magnet approach. At the end of the fall semester, David returned to Korea for work. With no supervisor specifically overseeing frequency up-conversion at that point, our subproject went on hiatus.

During spring 2026, I also helped field-test MAARCO with PhD students Sumedh Beknalkar and Julian Haessner. MAARCO stands for *Multi-terrain Amphibious ARCtic explOrer*. It is a rover with two screw-shaped, or helical, drives, developed to investigate travel across the changing mix of ground and water found in Arctic environments. The broader research asks how to model and control that motion, with applications in reaching difficult areas for environmental measurements. The [lab’s project overview](https://issrl.mae.ncsu.edu/research/maarco/) provides more background on its locomotion and navigation goals.

Our testing took place much closer to campus: around volleyball courts, Lake Johnson, and Jordan Lake, where we could encounter sand, mud, and uneven ground. My involvement focused on helping evaluate the GPS and odometry systems. GPS gives a position estimate from satellite signals, while odometry estimates how the rover’s position and orientation change over time using onboard motion measurements. Comparing those estimates is especially useful on soft terrain, where the drives can rotate without producing the expected amount of travel.

<figure>
  <video controls playsinline preload="none" poster="/assets/research-updates/maarco-field-test-poster.jpg" width="1280" height="720" aria-describedby="maarco-test-caption">
    <source src="/assets/research-updates/maarco-field-test.mp4" type="video/mp4" />
    <a href="/assets/research-updates/maarco-field-test.mp4">Watch the MAARCO field test.</a>
  </video>
  <figcaption id="maarco-test-caption">MAARCO during field testing, where we compared GPS and odometry estimates of the rover’s motion.</figcaption>
</figure>

I collaborated with a senior student on an exponential moving average filter for data from the rover’s inertial measurement unit, or IMU. An IMU measures quantities such as acceleration and angular velocity, but its readings also contain noise and vibration. Filtering can reduce rapid fluctuations before they affect the motion estimate.

An exponential moving average blends each new measurement with the previous filtered value. In a common formulation, `filtered = α × measurement + (1 − α) × previous_filtered`, where α sets how strongly the output responds to new data. Older measurements gradually lose influence. A smaller α gives a smoother signal but responds more slowly; a larger α follows changes sooner and retains more noise. This makes the filter inexpensive to compute, while leaving an important tuning decision: how much smoothing can we apply before we start obscuring real rover motion? [MathWorks describes the related exponential-weighting approach](https://www.mathworks.com/help/dsp/ug/sliding-window-method-and-exponential-weighting-method.html).

We first tested the filter in MATLAB and compared the resulting odometry against GPS data as a reference. That comparison gives us a way to assess whether filtering helps the motion estimate, beyond making a plotted signal look smoother. GPS has its own uncertainty, and smoothing alone cannot remove sensor bias or guarantee that accumulated position error disappears.

We also discussed simulation as a way to study the rover’s interaction with deformable terrain. Possibilities included Project Chrono and an Isaac Sim workflow with particle-based terrain calculations using NVIDIA Warp. The goal would be to model how material moves around the helical drives and connect that behavior to the rover’s motion. These are tools and workflows we’ve been exploring; comparing their predictions with field data will be an important part of deciding how useful they are for our setup.

Later in the spring, the frequency up-conversion work resumed when Dr. Sunmin Jang joined the Dickey Lab as a visiting scholar. I began working with him, initially spending much more time learning to manufacture the hydrogel samples consistently. At a high level, this involves preparing and mixing a precursor, molding it, and using UV curing to form the gel. The recipe is proprietary for now, so I’m leaving out the formulation and processing settings. Practicing this process was an important step toward making samples that we could meaningfully compare across mechanical tests.

Once we had spent time on sample fabrication, we returned to the challenge of attaching magnets. Embedding them during curing was an appealing option, but we were concerned that heat during the curing process could reduce their magnetization. We have not yet established whether our curing conditions cause that problem for the magnets we use.

Our workaround has been to cure the gel around acrylic placeholders that form retaining “lips” on its upper surface. After curing, we remove the placeholders and insert the magnets. This avoids exposing the magnets to the curing process, but testing has revealed a mechanical weakness: under some test conditions, the lips fatigue and tear. When that happens, a magnet can pull free and jump into the reciprocating array. A feature that holds a magnet during assembly therefore still has to prove that it can survive repeated loading.

The next step is to test whether the magnets retain their strength after exposure to the UV curing machine. If they do, we can investigate curing them directly into the samples and evaluate whether that improves retention. We also plan to measure the hydrogels’ vibration behavior in different mounting configurations with help from PhD student Olivia Mabe. A laser vibrometer will let us measure motion without attaching a sensor to the soft sample, and fast Fourier transform (FFT) analysis will show which frequencies are present. With an appropriate excitation and measurement procedure, we can use those measurements to investigate the samples’ natural frequencies and how they change with the setup.

Work on MAARCO is continuing as well, through simulation exploration and design and fabrication of a larger rover. The plan is to carry more instruments and take it to western North Carolina for testing in harsher conditions and more difficult terrain. Across both projects, I’ve enjoyed moving between fabrication, experiments, and data analysis. There are still open questions about magnet retention, hydrogel dynamics, and rover localization, and the next round of tests should give us more concrete evidence to work with.
