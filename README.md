# Sonic Battle (USA)

This my attempt at a disassembly of Sonic Battle (USA)

As of right now it doesn't build and I get this error:

```
[yophlox@archlinux sbattle-git]$ make
/opt/devkitpro/devkitARM/bin/arm-none-eabi-as -mcpu=arm7tdmi -mthumb-interwork -I asminclude -o build/sbattle/asm/code.o asm/code.s
/opt/devkitpro/devkitARM/bin/arm-none-eabi-as -mcpu=arm7tdmi -mthumb-interwork -I asminclude -o build/sbattle/data/data.o data/data.s
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld -T ldscript.txt -Map sbattle.map  build/sbattle/asm/code.o build/sbattle/data/data.o tools/agbcc/lib/libgcc.a tools/agbcc/lib/libc.a -o sbattle.elf
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld: build/sbattle/asm/code.o: in function `_08007F60':
(.rodata+0x8044): undefined reference to `_0800B086'
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld: (.rodata+0x8048): undefined reference to `_0800B086'
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld: (.rodata+0x804c): undefined reference to `_0800B086'
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld: (.rodata+0x8050): undefined reference to `_0800B086'
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld: (.rodata+0x8054): undefined reference to `_0800B086'
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld: build/sbattle/asm/code.o:(.rodata+0x8058): more undefined references to `_0800B086' follow
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld: build/sbattle/asm/code.o: in function `_0800B0BC':
(.rodata+0xb13c): undefined reference to `_0800BAA4'
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld: (.rodata+0xb1a0): undefined reference to `_0800BAA4'
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld: (.rodata+0xb1a4): undefined reference to `_0800BAA4'
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld: (.rodata+0xb1a8): undefined reference to `_0800BAA4'
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld: (.rodata+0xb1ac): undefined reference to `_0800BAA4'
/opt/devkitpro/devkitARM/bin/arm-none-eabi-ld: build/sbattle/asm/code.o:(.rodata+0xb1b0): more undefined references to `_0800BAA4' follow
make: *** [Makefile:73: sbattle.elf] Error 1
```

### Setting up the repository

* You must have a copy of the Sonic Battle ROM named `baserom.gba` in the repository directory.

* Install [**devkitARM**](http://devkitpro.org/wiki/Getting_Started/devkitARM).

* You can then build sbattle using the `make` command.