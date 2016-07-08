	.globl _start
_start:
/*
* This command loads the physical address of the GPIO region into r0.
*/
ldr r0,=0x20200000

/*
* Set GPIO 47 to Output mode by writing 0b001 to bits 21-23 (7 * 3)
* to GPFSEL4, which controls GPIOs 40 to 49.
* That is in the 4th word of the table at 0x20200010 or r0 + 0x10 (16 decimal)
*/
mov r1,#1
lsl r1,#21
str r1,[r0,#16]

/*
* Normally we would read the current contents of the location first, so we don't change GPIOs 40-46 and 48,49
* when we write to it. But this is only a quick example program. That bit comes later
*/

/*
* Turn GPIO 47 on by writing 1 to bit 15 of GPSET1. Each GPSETn location controls the output of up to 32 GPIOs.
* Writing a 1 to a GPSETn location sets that GPIO output (if it is in output mode) to a high state.
* Writing a 0 to a GPSETn location does nothing. To set a GPIO to output low you have to write a 1 to a GPCLRn.
*/
mov r1,#1
lsl r1,#15
str r1,[r0,#32]
loop$:
b loop$
