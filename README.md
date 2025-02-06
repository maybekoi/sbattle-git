# Sonic Battle (USA)

This my attempt at a disassembly of Sonic Battle (USA)

As of right now it doesn't build and I get this error:

```
C:\devkitPro\devkitARM\bin\arm-none-eabi-objcopy.exe: sbattle.gba[EWRAM]: section has no contents
make: *** [Makefile:76: sbattle.gba] Error 1
```

### Setting up the repository

* You must have a copy of the Sonic Battle ROM named `baserom.gba` in the repository directory.

* Install [**devkitARM**](http://devkitpro.org/wiki/Getting_Started/devkitARM).

* You can then build sbattle using `make` in the MSYS environment provided with devkitARM.