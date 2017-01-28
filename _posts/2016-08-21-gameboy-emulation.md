---
layout: post
title: Gameboy Emulation
---

For the last few days, I've been working on writing an emulator for the
[Nintendo Gameboy](https://en.wikipedia.org/wiki/Game_Boy).

Emulation is
a pretty cool concept. It allows a computer to masquerade around as a different
system altogether. What this means is that if my emulator gets working eventually,
I should be able to play games originally written for the Game Boy (like Pokemon Red)
on my PC using it.

### How it works

Basically, we use the hardware at our disposal to emulate each and every aspect of the
other hardware. This means emulating the CPU, the memory and the GPU and many other things.
Emulating the CPU is pretty simple. The gameboy has a processor which is a variant of the
Zilog Z80. So all we have to do is implement the original instructions of the Z80 in software
and do book-keeping of all its registers and the memory.

### Progress so far

I started with the aim of getting the [bootstrap program](https://www.youtube.com/watch?v=ZUf_gJp8Ivo) of the gameboy to run, before moving
on to actual games.

I (along with friends) have written enough instructions so far, that the system is able
to emulate about half of the bootstrap program of the gameboy. However, there is some code in
the bootstrap program that makes it wait for a VBLANK signal from the GPU. Since the GPU doesn't
exist yet, the emulator gets stuck here.

So the next thing that I'm going to work on is getting some kind of GPU running.

### References

There is a lot of great documentation on emulating the Gameboy that I've been reading.
Two blogs that have helped a great deal are [here](http://imrannazar.com/GameBoy-Emulation-in-JavaScript:-The-CPU) and [here](https://realboyemulator.wordpress.com/getting-started/).
I've been looking at opcodes for the instructions from [here](http://gameboy.mongenel.com/dmg/opcodes.html) and [here](http://marc.rawer.de/Gameboy/Docs/GBCPUman.pdf). I don't think I would have gotten even
this far without these resources.
