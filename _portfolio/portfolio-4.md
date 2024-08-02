---
title: "CoSyR: coherent synchrotron radiation and self-consistent beam dynamics in synchrotrons"
excerpt: "<br/><img src='/images/cosyr.png' width='400' height='240'>"
collection: research
---

High-brightness (dense, short-pulsed, well-collimated) electron beams underpin the modern accelerators and x-ray light sources (such as the free-electron-lasers). Charged particles radiate electromagnetic waves when they accelerate. This is called synchrotron radiation for modern storage-ring based accelerators. The radiation power increases so sharply with the beam brightness/energy to a level that the radiation may directly perturb the beam dynamics (such as micro-bunching). Accurately modeling this kind of beam dynamics is crucial to the design of modern accelerators, but is also extremely challenging because of the history dependence (e.g., radiation travels forward at a negligible pace relative to the highly relativistic beam, so the radiation at beam head may originate long ago from electrons at the beam tail). 

Here, we construct a computational framework that can do this job self-consistently in a time-progression fashion. It is based on a Lagrangian method for the electromagnetic wave calculation. These waves, represented by wavelets, are emitted at each step, and they are traced at successive steps forming a set of near-field wavelets at real-time of the beam. These wavelets are then interpolated to a moving mesh of the beam in order to push particles. This way, the coherent synchrotron radiation effects can be simulated self-consistently with small errors as compared to usual FDTD methods. 

F.-Y. Li, C.-K. Huang, R. V. Garimella, T. J. T. Kwan, and B. E. Carlsten, Validation of a novel method for the calculation of near-field synchrotron radiation, Proc. of 10th IPAC, 397-399 (2019).

C.-K. Huang, F.-Y. Li, H. N. Rakotoarivelo, et al., CoSyR: a novel beam dynamics code for the modeling of synchrotron radiation effects, arXiv:2109.14901; Nucl. Inst. Methods A (2022).

[CoSyR repo](https://github.com/lanl/cosyr)

