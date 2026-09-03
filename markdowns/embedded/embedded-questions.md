<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Embedded Systems & RTOS Logo" width="100" height="100">
  </a>
  <h1>Embedded Systems & RTOS Interview Questions & Answers</h1>
  <p><b>Comprehensive interview questions covering FreeRTOS, Priority Inversion, Memory-Mapped I/O, ISRs, and DMA</b></p>
</div>

---

## Table of Contents

1. [How does Priority Inversion occur in Real-Time Operating Systems (RTOS), and how does Priority Inheritance solve it?](#q1) <span class="advanced">Advanced</span>
2. [Why is the `volatile` keyword essential in Embedded C, and what happens when the compiler optimizes it away?](#q2) <span class="advanced">Advanced</span>
3. [How do you implement Deferred Interrupt Processing in FreeRTOS using Task Notifications and Queues?](#q3) <span class="advanced">Advanced</span>
4. [How does Direct Memory Access (DMA) Double-Buffering work, and how do you maintain CPU Cache Coherency?](#q4) <span class="advanced">Advanced</span>
5. [How do you debug an ARM Cortex-M HardFault Handler and extract the stacked register frame (PC, LR, SP)?](#q5) <span class="advanced">Advanced</span>
6. [What are the differences between SPI, I2C, UART, and CAN bus protocols?](#q6) <span class="intermediate">Intermediate</span>
7. [How does a Linker Script (`.ld`) define memory regions (`.text`, `.data`, `.bss`, `.rodata`, Heap, Stack)?](#q7) <span class="advanced">Advanced</span>
8. [What is the difference between Preemptive and Cooperative Multitasking in RTOS?](#q8) <span class="beginner">Beginner</span>
9. [How do you implement an Independent Watchdog (IWDG) vs Window Watchdog (WWDG)?](#q9) <span class="intermediate">Intermediate</span>
10. [What is Memory-Mapped I/O (MMIO) vs Port-Mapped I/O (PMIO)?](#q10) <span class="beginner">Beginner</span>
11. [How does Nested Vectored Interrupt Controller (NVIC) priority grouping work in ARM Cortex-M?](#q11) <span class="advanced">Advanced</span>
12. [What is a Circular Ring Buffer and how do you implement it for UART RX in bare-metal systems?](#q12) <span class="intermediate">Intermediate</span>
13. [How does an In-Application Programming (IAP) Bootloader verify and flash firmware OTA (Over-The-Air)?](#q13) <span class="advanced">Advanced</span>
14. [What is the role of the Vector Table in ARM Cortex-M microcontrollers?](#q14) <span class="intermediate">Intermediate</span>
15. [How do you handle Debouncing for mechanical switches in software without blocking delays?](#q15) <span class="beginner">Beginner</span>
16. [What is MISRA C and what are its core safety rules in automotive and medical firmware?](#q16) <span class="intermediate">Intermediate</span>
17. [How do you configure Low-Power Sleep Modes (Sleep, Stop, Standby) in microcontrollers?](#q17) <span class="intermediate">Intermediate</span>
18. [What is Bit-Banging and when is it necessary?](#q18) <span class="beginner">Beginner</span>
19. [How do you implement Fixed-Point Arithmetic to avoid floating-point library overhead on MCUs without an FPU?](#q19) <span class="intermediate">Intermediate</span>
20. [What is the difference between Reentrant Code and Thread-Safe Code in embedded firmware?](#q20) <span class="intermediate">Intermediate</span>
21. [How do you prevent Race Conditions when accessing 16/32-bit registers on 8-bit microcontrollers?](#q21) <span class="intermediate">Intermediate</span>
22. [What is an RTOS Tick Rate and what are the trade-offs of setting it to 1000Hz vs 100Hz?](#q22) <span class="intermediate">Intermediate</span>
23. [How does CAN Bus Arbitration work using Dominant (0) and Recessive (1) bits?](#q23) <span class="advanced">Advanced</span>
24. [What is JTAG vs SWD (Serial Wire Debug) in hardware debugging?](#q24) <span class="beginner">Beginner</span>
25. [How do you safely write and erase internal Microcontroller Flash memory without corrupting running code?](#q25) <span class="advanced">Advanced</span>
26. [What is the purpose of the SysTick Timer in ARM Cortex-M RTOS ports?](#q26) <span class="intermediate">Intermediate</span>
27. [How do you calculate Battery Life for an IoT device with duty cycles (Active vs Deep Sleep)?](#q27) <span class="intermediate">Intermediate</span>
28. [What is Aliasing and how does the Nyquist-Shannon Sampling Theorem dictate ADC sampling rates?](#q28) <span class="intermediate">Intermediate</span>
29. [How do you configure an ADC with Analog Watchdog to trigger interrupts on voltage spikes?](#q29) <span class="intermediate">Intermediate</span>
30. [What is Pulse Width Modulation (PWM) and how do hardware Timers generate variable duty cycles?](#q30) <span class="beginner">Beginner</span>
31. [How do you implement Software Timers in FreeRTOS without creating separate tasks for each timer?](#q31) <span class="intermediate">Intermediate</span>
32. [What is Endianness (Little-Endian vs Big-Endian) and how do you handle network byte order in firmware?](#q32) <span class="beginner">Beginner</span>
33. [How do you design a Fail-Safe State Machine for safety-critical medical devices?](#q33) <span class="advanced">Advanced</span>
34. [What is a Pull-Up and Pull-Down Resistor and why are floating inputs dangerous in CMOS circuits?](#q34) <span class="beginner">Beginner</span>
35. [How do you measure Code Execution Time on bare-metal systems using DWT Cycle Counter?](#q35) <span class="advanced">Advanced</span>
36. [What is the difference between Flash Memory, SRAM, and EEPROM?](#q36) <span class="beginner">Beginner</span>
37. [How do you calibrate an internal RC Oscillator (HSI) against an external crystal (HSE)?](#q37) <span class="intermediate">Intermediate</span>
38. [What is Clock Tree Configuration (PLL, Prescalers) in modern 32-bit MCUs?](#q38) <span class="intermediate">Intermediate</span>
39. [How do you implement Lock-Free Counting Semaphores in embedded C?](#q39) <span class="advanced">Advanced</span>
40. [What is Stack Overflow in embedded systems and how does FreeRTOS Stack Watermark detection work?](#q40) <span class="intermediate">Intermediate</span>
41. [How do you configure an External Interrupt (EXTI) line on GPIO pins?](#q41) <span class="beginner">Beginner</span>
42. [What is a Brown-Out Reset (BOR) and how does it prevent microcontroller flash corruption?](#q42) <span class="intermediate">Intermediate</span>
43. [How do you implement CRC32 in hardware accelerators vs software lookup tables?](#q43) <span class="intermediate">Intermediate</span>
44. [What is Real-Time Clock (RTC) backup domain and coin-cell battery power switching?](#q44) <span class="beginner">Beginner</span>
45. [How do you perform Firmware Encryption and Secure Boot on modern MCUs?](#q45) <span class="advanced">Advanced</span>
46. [What is the difference between Polling, Interrupts, and DMA in peripheral data transfer?](#q46) <span class="beginner">Beginner</span>
47. [How do you handle Floating Ground and Ground Loops in industrial RS-485 / CAN communication?](#q47) <span class="intermediate">Intermediate</span>
48. [What is Optical Isolation and how do Optocouplers protect digital inputs from high-voltage transients?](#q48) <span class="beginner">Beginner</span>
49. [How do you interface an SD Card via SPI vs 4-bit SDIO mode in embedded firmware?](#q49) <span class="intermediate">Intermediate</span>
50. [What is Open-Drain (Open-Collector) with external pull-up vs Push-Pull output?](#q50) <span class="beginner">Beginner</span>
51. [How do you implement Mutex vs Binary Semaphore in RTOS task synchronization?](#q51) <span class="intermediate">Intermediate</span>
52. [What is the ARM Cortex-M Bit-Banding feature?](#q52) <span class="advanced">Advanced</span>
53. [How do you design an Uninterruptible Power Supply (UPS) monitoring circuit for embedded gateways?](#q53) <span class="intermediate">Intermediate</span>
54. [What is Dead Time Generation in Complementary PWM for Motor Control (H-Bridge)?](#q54) <span class="advanced">Advanced</span>
55. [How do you implement a Software Watchdog for multiple concurrent RTOS tasks?](#q55) <span class="intermediate">Intermediate</span>
56. [What is Code Relocation and executing code from RAM instead of Flash?](#q56) <span class="advanced">Advanced</span>
57. [How do you measure Power Consumption using Current Shunt Monitors and INA219 sensors?](#q57) <span class="beginner">Beginner</span>
58. [What is the difference between ARM Cortex-M0, M3, M4, and M7 core architectures?](#q58) <span class="intermediate">Intermediate</span>
59. [How do you configure Hardware Flow Control (RTS/CTS) in UART communication?](#q59) <span class="beginner">Beginner</span>
60. [What is Static Memory Allocation in FreeRTOS (`configSUPPORT_STATIC_ALLOCATION = 1`)?](#q60) <span class="intermediate">Intermediate</span>
61. [How do you implement a PID (Proportional-Integral-Derivative) Controller in embedded C?](#q61) <span class="intermediate">Intermediate</span>
62. [What is Cross-Compilation and how does a Toolchain (`arm-none-eabi-gcc`) build binaries for target MCUs?](#q62) <span class="beginner">Beginner</span>
63. [How do you detect Hardware Faults (BusFault, MemManageFault, UsageFault) in ARM Cortex-M?](#q63) <span class="advanced">Advanced</span>
64. [What is USB CDC (Communication Device Class) vs HID (Human Interface Device)?](#q64) <span class="beginner">Beginner</span>
65. [How do you handle Jitter in high-frequency Sensor Sampling?](#q65) <span class="intermediate">Intermediate</span>
66. [What is In-Circuit Emulation (ICE) and Boundary Scan in hardware manufacturing testing?](#q66) <span class="advanced">Advanced</span>
67. [How do you implement Dynamic Voltage and Frequency Scaling (DVFS) in low-power firmware?](#q67) <span class="advanced">Advanced</span>
68. [What is the difference between Level-Triggered and Edge-Triggered Interrupts?](#q68) <span class="beginner">Beginner</span>
69. [How do you manage Flash Wear Leveling in embedded filesystems (LittleFS, SPIFFS)?](#q69) <span class="intermediate">Intermediate</span>
70. [What is a Bus Contention and how do tristate buffers prevent multiple devices driving a shared bus?](#q70) <span class="beginner">Beginner</span>
71. [How do you configure an RTOS Queue with Queue Sets to wait on multiple queues simultaneously?](#q71) <span class="intermediate">Intermediate</span>
72. [What is Memory Protection Unit (MPU) in ARM Cortex-M and how does it prevent buffer overflows?](#q72) <span class="advanced">Advanced</span>
73. [How do you implement Software I2C Clock Stretching?](#q73) <span class="intermediate">Intermediate</span>
74. [What is Overclocking Microcontrollers and what are the hardware risks (Timing Violations, Thermal Runaway)?](#q74) <span class="intermediate">Intermediate</span>
75. [How do you implement Heartbeat LED blinking using Non-Blocking Timers in bare-metal systems?](#q75) <span class="beginner">Beginner</span>
76. [What is Boundary Check and Defending against Buffer Overflows in Embedded C?](#q76) <span class="beginner">Beginner</span>
77. [How do you configure Hardware Acceleration for Cryptography (AES, SHA) on microcontrollers?](#q77) <span class="intermediate">Intermediate</span>
78. [What is the difference between Volatile Memory and Non-Volatile Memory?](#q78) <span class="beginner">Beginner</span>
79. [How do you debug an intermittent system freeze using an external Hardware Logic Analyzer?](#q79) <span class="intermediate">Intermediate</span>
80. [What is Context Switching Overhead and how does Hardware Register Stacking affect RTOS latency?](#q80) <span class="advanced">Advanced</span>
81. [How do you design a Low-Power Wake-On-Motion system using an Accelerometer interrupt?](#q81) <span class="intermediate">Intermediate</span>
82. [What is the difference between Thread Mode and Handler Mode in ARM Cortex-M?](#q82) <span class="intermediate">Intermediate</span>
83. [How do you calibrate an Analog Temperature Sensor using Two-Point Calibration?](#q83) <span class="intermediate">Intermediate</span>
84. [What is CAN FD (Flexible Data-Rate) and how does it improve over classical CAN 2.0B?](#q84) <span class="intermediate">Intermediate</span>
85. [How do you prevent Deadlocks in multi-threaded RTOS applications?](#q85) <span class="intermediate">Intermediate</span>
86. [What is Asynchronous Serial Framing Error and what causes it in UART?](#q86) <span class="beginner">Beginner</span>
87. [How do you implement Software-Based Watchdog Petting across distributed sensor nodes?](#q87) <span class="intermediate">Intermediate</span>
88. [What is the purpose of the Assembly Reset Handler (`Reset_Handler`) in startup code?](#q88) <span class="advanced">Advanced</span>
89. [How do you handle Floating Point Numbers on MCUs with Single-Precision vs Double-Precision FPU?](#q89) <span class="intermediate">Intermediate</span>
90. [What is Hardware CRC Calculation for Packet Integrity in wireless RF links (LoRa, BLE)?](#q90) <span class="beginner">Beginner</span>
91. [How do you configure an ADC for Differential Input Measurements?](#q91) <span class="intermediate">Intermediate</span>
92. [What is Safety Integrity Level (SIL / ASIL) and what firmware processes are required for ISO 26262?](#q92) <span class="advanced">Advanced</span>
93. [How do you implement an On-Chip EEPROM Emulation in Flash memory?](#q93) <span class="intermediate">Intermediate</span>
94. [What is Jitter and Latency in Interrupt Handling (Interrupt Latency)?](#q94) <span class="intermediate">Intermediate</span>
95. [How do you design an Ultra-Reliable Embedded System that recovers automatically from cosmic-ray Single Event Upsets (SEU)?](#q95) <span class="advanced">Advanced</span>
96. [What is the purpose of the Assembly HardFault Trampoline in ARM Cortex-M?](#q96) <span class="advanced">Advanced</span>
97. [How do you configure Real-Time Trace with ARM CoreSight Embedded Trace Macrocell (ETM)?](#q97) <span class="advanced">Advanced</span>
98. [What is the difference between Edge-Aligned and Center-Aligned PWM for Motor Drivers?](#q98) <span class="intermediate">Intermediate</span>
99. [How do you implement Non-Volatile Parameter Storage using Wear-Resistant Wear Leveling in NOR Flash?](#q99) <span class="intermediate">Intermediate</span>
100. [How do you prevent Microcontroller Latch-Up caused by Input Overvoltage?](#q100) <span class="beginner">Beginner</span>

---

<a id="q1"></a>
### Q1: How does Priority Inversion occur in Real-Time Operating Systems (RTOS), and how does Priority Inheritance solve it?

**Difficulty**: Advanced

**Strategy**:
Priority Inversion occurs when a low-priority task (L) holds a shared mutex, and a high-priority task (H) attempts to acquire it and blocks. A medium-priority task (M) that does not need the mutex preempts L, indefinitely starving H (as occurred on the Mars Pathfinder spacecraft). Solved by Priority Inheritance: when H blocks on a mutex held by L, the RTOS temporarily elevates L's priority to H's level until L releases the mutex, preventing M from preempting L.

**Code Example**:
```c
// FreeRTOS Mutex with Priority Inheritance
#include "FreeRTOS.h"
#include "semphr.h"

SemaphoreHandle_t xSharedMutex;

void vInit(void) {
    // xSemaphoreCreateMutex automatically supports Priority Inheritance
    xSharedMutex = xSemaphoreCreateMutex();
}

void vHighPriorityTask(void* pvParams) {
    // If low priority task holds mutex, RTOS elevates low task priority to High
    if (xSemaphoreTake(xSharedMutex, portMAX_DELAY) == pdTRUE) {
        // Critical section
        xSemaphoreGive(xSharedMutex);
    }
}
```

---

<a id="q2"></a>
### Q2: Why is the `volatile` keyword essential in Embedded C, and what happens when the compiler optimizes it away?

**Difficulty**: Advanced

**Strategy**:
The `volatile` keyword instructs the C compiler that a variable's value can change unexpectedly at any time from outside the program's control (e.g. by hardware peripherals, memory-mapped I/O registers, or Interrupt Service Routines). Without `volatile`, the compiler optimizer caches the register value in a CPU register or optimizes away polling loops entirely into infinite loops.

**Code Example**:
```c
// Memory-Mapped Status Register Polling
#define UART_STATUS_REG (*((volatile uint32_t*)0x4000C000))
#define TX_READY_FLAG   (1 << 5)

void send_byte(uint8_t data) {
    // Compiler CANNOT cache UART_STATUS_REG in a register
    // Reads directly from hardware memory address on every iteration
    while ((UART_STATUS_REG & TX_READY_FLAG) == 0) {
        // Busy wait for hardware buffer to empty
    }
    *((volatile uint8_t*)0x4000C004) = data;
}
```

---

<a id="q3"></a>
### Q3: How do you implement Deferred Interrupt Processing in FreeRTOS using Task Notifications and Queues?

**Difficulty**: Advanced

**Strategy**:
Interrupt Service Routines (ISRs) must execute in microseconds to prevent missing subsequent hardware interrupts. ISRs should only capture minimal hardware state, clear the interrupt flag, and defer heavy processing to an RTOS worker task using lightweight Task Notifications (`vTaskNotifyGiveFromISR`) or Queues (`xQueueSendFromISR`), waking up the worker task immediately with context switch (`portYIELD_FROM_ISR`).

**Code Example**:
```c
// Deferred Interrupt Processing in FreeRTOS
TaskHandle_t xWorkerTaskHandle;

void UART_IRQHandler(void) {
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;
    uint8_t byte = UART->DATA; // Read byte
    UART->STATUS &= ~INT_FLAG; // Clear flag

    // Wake worker task immediately
    vTaskNotifyGiveFromISR(xWorkerTaskHandle, &xHigherPriorityTaskWoken);
    portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
}
```

---

<a id="q4"></a>
### Q4: How does Direct Memory Access (DMA) Double-Buffering work, and how do you maintain CPU Cache Coherency?

**Difficulty**: Advanced

**Strategy**:
DMA transfers data directly between hardware peripherals (ADC, SPI, Ethernet) and RAM without CPU intervention. In double-buffering (ping-pong buffers), DMA fills Buffer A while CPU processes Buffer B. On completion, DMA switches to Buffer B and generates an interrupt. On ARM Cortex-M7 with D-Cache, the CPU must invalidate its cache line before reading DMA memory to avoid reading stale cached data.

**Code Example**:
```c
// Invalidate CPU L1 Data Cache Before Reading DMA Buffer
SCB_InvalidateDCache_by_Addr((uint32_t*)dma_rx_buffer, BUFFER_SIZE);
process_data(dma_rx_buffer);
```

---

<a id="q5"></a>
### Q5: How do you debug an ARM Cortex-M HardFault Handler and extract the stacked register frame (PC, LR, SP)?

**Difficulty**: Advanced

**Strategy**:
On a HardFault, Cortex-M hardware pushes eight registers onto the stack (R0-R3, R12, LR, PC, xPSR). An assembly trampoline determines whether the Main Stack Pointer (MSP) or Process Stack Pointer (PSP) was active and passes the pointer to a C handler that prints the faulting Program Counter (PC) and Configurable Fault Status Register (CFSR).

**Code Example**:
```c
void HardFault_HandlerC(uint32_t* stacked_args) {
    uint32_t stacked_r0 = stacked_args[0];
    uint32_t stacked_pc = stacked_args[6]; // Faulting instruction address!
    uint32_t stacked_lr = stacked_args[5]; // Return address
    printf("HardFault at PC: 0x%08X, LR: 0x%08X\n", stacked_pc, stacked_lr);
    while (1); // Halt for JTAG debugger
}
```

---

<a id="q6"></a>
### Q6: What are the differences between SPI, I2C, UART, and CAN bus protocols?

**Difficulty**: Intermediate

**Strategy**:
SPI: synchronous, full-duplex, 4-wire, master-slave, >50MHz; I2C: 2-wire, synchronous, multi-master with addressing, up to 3.4MHz; UART: asynchronous point-to-point; CAN: differential 2-wire, multi-master, priority-arbitrated, automotive grade.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What are the differences between SPI, I2C, UART, and CAN bus protocols?
// Production-ready C firmware
```

---

<a id="q7"></a>
### Q7: How does a Linker Script (`.ld`) define memory regions (`.text`, `.data`, `.bss`, `.rodata`, Heap, Stack)?

**Difficulty**: Advanced

**Strategy**:
Defines physical flash and RAM addresses; `.text` holds executable code in Flash; `.rodata` holds constants; `.data` initialized variables copied from Flash to RAM at boot; `.bss` zero-initialized RAM variables.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How does a Linker Script (`.ld`) define memory regions (`.text`, `.data`, `.bss`, `.rodata`, Heap, Stack)?
// Production-ready C firmware
```

---

<a id="q8"></a>
### Q8: What is the difference between Preemptive and Cooperative Multitasking in RTOS?

**Difficulty**: Beginner

**Strategy**:
Preemptive: RTOS SysTick timer interrupts and preempts running tasks to run higher priority task; Cooperative: tasks run until they explicitly yield (`taskYIELD`).

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the difference between Preemptive and Cooperative Multitasking in RTOS?
// Production-ready C firmware
```

---

<a id="q9"></a>
### Q9: How do you implement an Independent Watchdog (IWDG) vs Window Watchdog (WWDG)?

**Difficulty**: Intermediate

**Strategy**:
IWDG has internal dedicated RC clock, resets system if software hangs and fails to refresh counter; WWDG must be refreshed within a specific time window, detecting early/late software execution.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement an Independent Watchdog (IWDG) vs Window Watchdog (WWDG)?
// Production-ready C firmware
```

---

<a id="q10"></a>
### Q10: What is Memory-Mapped I/O (MMIO) vs Port-Mapped I/O (PMIO)?

**Difficulty**: Beginner

**Strategy**:
MMIO shares address space with RAM; accessed using standard pointers and memory instructions. PMIO uses separate address bus with dedicated CPU instructions (`IN`, `OUT`).

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Memory-Mapped I/O (MMIO) vs Port-Mapped I/O (PMIO)?
// Production-ready C firmware
```

---

<a id="q11"></a>
### Q11: How does Nested Vectored Interrupt Controller (NVIC) priority grouping work in ARM Cortex-M?

**Difficulty**: Advanced

**Strategy**:
Divides priority bits into Preemption Priority (determines if interrupt can preempt active interrupt) and Subpriority (determines order of simultaneous interrupts).

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How does Nested Vectored Interrupt Controller (NVIC) priority grouping work in ARM Cortex-M?
// Production-ready C firmware
```

---

<a id="q12"></a>
### Q12: What is a Circular Ring Buffer and how do you implement it for UART RX in bare-metal systems?

**Difficulty**: Intermediate

**Strategy**:
Fixed array with `head` and `tail` pointers; ISR writes incoming byte to `head` and increments; main loop reads from `tail` without locking.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is a Circular Ring Buffer and how do you implement it for UART RX in bare-metal systems?
// Production-ready C firmware
```

---

<a id="q13"></a>
### Q13: How does an In-Application Programming (IAP) Bootloader verify and flash firmware OTA (Over-The-Air)?

**Difficulty**: Advanced

**Strategy**:
Bootloader verifies image cryptographic SHA-256 signature, writes new binary to Flash application sector, verifies CRC32, updates vector table offset (`VTOR`), and jumps to new entry point.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How does an In-Application Programming (IAP) Bootloader verify and flash firmware OTA (Over-The-Air)?
// Production-ready C firmware
```

---

<a id="q14"></a>
### Q14: What is the role of the Vector Table in ARM Cortex-M microcontrollers?

**Difficulty**: Intermediate

**Strategy**:
Array of 32-bit function pointers stored at address `0x00000000` (or offset in VTOR); holds initial Stack Pointer address, Reset Handler, NMI, HardFault, and peripheral ISR vectors.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the role of the Vector Table in ARM Cortex-M microcontrollers?
// Production-ready C firmware
```

---

<a id="q15"></a>
### Q15: How do you handle Debouncing for mechanical switches in software without blocking delays?

**Difficulty**: Beginner

**Strategy**:
Poll button pin every 10ms via timer interrupt; shift digital readings into an 8-bit shift register; trigger valid press only when register matches `0xFF`.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you handle Debouncing for mechanical switches in software without blocking delays?
// Production-ready C firmware
```

---

<a id="q16"></a>
### Q16: What is MISRA C and what are its core safety rules in automotive and medical firmware?

**Difficulty**: Intermediate

**Strategy**:
Coding standard preventing undefined behavior: forbids dynamic memory allocation (`malloc`), enforces single return points, bans pointer arithmetic on arbitrary integers.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is MISRA C and what are its core safety rules in automotive and medical firmware?
// Production-ready C firmware
```

---

<a id="q17"></a>
### Q17: How do you configure Low-Power Sleep Modes (Sleep, Stop, Standby) in microcontrollers?

**Difficulty**: Intermediate

**Strategy**:
Sleep: turns off CPU clock, peripherals run; Stop: turns off all clocks, RAM retained; Standby: powers down core logic, wakes up only on external pin or RTC alarm.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you configure Low-Power Sleep Modes (Sleep, Stop, Standby) in microcontrollers?
// Production-ready C firmware
```

---

<a id="q18"></a>
### Q18: What is Bit-Banging and when is it necessary?

**Difficulty**: Beginner

**Strategy**:
Emulating serial communication protocols (SPI, I2C) in software by manually toggling General Purpose I/O (GPIO) pins when hardware peripherals are unavailable.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Bit-Banging and when is it necessary?
// Production-ready C firmware
```

---

<a id="q19"></a>
### Q19: How do you implement Fixed-Point Arithmetic to avoid floating-point library overhead on MCUs without an FPU?

**Difficulty**: Intermediate

**Strategy**:
Represent fractional numbers using scaled integers (e.g. Q15 format: 1 sign bit, 15 fractional bits); perform multiplication followed by right shift.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement Fixed-Point Arithmetic to avoid floating-point library overhead on MCUs without an FPU?
// Production-ready C firmware
```

---

<a id="q20"></a>
### Q20: What is the difference between Reentrant Code and Thread-Safe Code in embedded firmware?

**Difficulty**: Intermediate

**Strategy**:
Reentrant code can be safely called simultaneously by multiple tasks or interrupted by an ISR without using shared static or global variables.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the difference between Reentrant Code and Thread-Safe Code in embedded firmware?
// Production-ready C firmware
```

---

<a id="q21"></a>
### Q21: How do you prevent Race Conditions when accessing 16/32-bit registers on 8-bit microcontrollers?

**Difficulty**: Intermediate

**Strategy**:
Disable interrupts (`cli()`) before reading high and low byte registers, and re-enable interrupts immediately after (`sei()`).

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you prevent Race Conditions when accessing 16/32-bit registers on 8-bit microcontrollers?
// Production-ready C firmware
```

---

<a id="q22"></a>
### Q22: What is an RTOS Tick Rate and what are the trade-offs of setting it to 1000Hz vs 100Hz?

**Difficulty**: Intermediate

**Strategy**:
1000Hz provides 1ms time resolution but increases CPU context switch overhead; 100Hz saves CPU cycles and power but limits scheduling granularity to 10ms.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is an RTOS Tick Rate and what are the trade-offs of setting it to 1000Hz vs 100Hz?
// Production-ready C firmware
```

---

<a id="q23"></a>
### Q23: How does CAN Bus Arbitration work using Dominant (0) and Recessive (1) bits?

**Difficulty**: Advanced

**Strategy**:
Nodes transmit message IDs simultaneously; dominant bits overwrite recessive bits on the bus; a node transmitting recessive that detects dominant realizes it lost arbitration and yields.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How does CAN Bus Arbitration work using Dominant (0) and Recessive (1) bits?
// Production-ready C firmware
```

---

<a id="q24"></a>
### Q24: What is JTAG vs SWD (Serial Wire Debug) in hardware debugging?

**Difficulty**: Beginner

**Strategy**:
JTAG uses 4-5 pins (TDI, TDO, TCK, TMS, TRST); SWD uses only 2 pins (SWDIO bidirectional data and SWCLK clock), saving PCB space on small packages.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is JTAG vs SWD (Serial Wire Debug) in hardware debugging?
// Production-ready C firmware
```

---

<a id="q25"></a>
### Q25: How do you safely write and erase internal Microcontroller Flash memory without corrupting running code?

**Difficulty**: Advanced

**Strategy**:
Flash cannot be written byte-by-byte; must be unlocked, sector erased to `0xFF`, and programmed in half-words. Interrupts must be disabled or execution relocated to RAM during write.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you safely write and erase internal Microcontroller Flash memory without corrupting running code?
// Production-ready C firmware
```

---

<a id="q26"></a>
### Q26: What is the purpose of the SysTick Timer in ARM Cortex-M RTOS ports?

**Difficulty**: Intermediate

**Strategy**:
24-bit dedicated down-counting system timer integrated into core CPU; generates periodic interrupts driving the RTOS scheduler context switches.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the purpose of the SysTick Timer in ARM Cortex-M RTOS ports?
// Production-ready C firmware
```

---

<a id="q27"></a>
### Q27: How do you calculate Battery Life for an IoT device with duty cycles (Active vs Deep Sleep)?

**Difficulty**: Intermediate

**Strategy**:
Calculate weighted average current consumption: $I_{\text{avg}} = (I_{\text{active}} \times T_{\text{active}} + I_{\text{sleep}} \times T_{\text{sleep}}) / T_{\text{total}}$; divide battery capacity by $I_{\text{avg}}$.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you calculate Battery Life for an IoT device with duty cycles (Active vs Deep Sleep)?
// Production-ready C firmware
```

---

<a id="q28"></a>
### Q28: What is Aliasing and how does the Nyquist-Shannon Sampling Theorem dictate ADC sampling rates?

**Difficulty**: Intermediate

**Strategy**:
Sampling rate must be at least twice the highest frequency component of the analog signal ($f_s \ge 2f_{\text{max}}$) to prevent false low-frequency alias distortion.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Aliasing and how does the Nyquist-Shannon Sampling Theorem dictate ADC sampling rates?
// Production-ready C firmware
```

---

<a id="q29"></a>
### Q29: How do you configure an ADC with Analog Watchdog to trigger interrupts on voltage spikes?

**Difficulty**: Intermediate

**Strategy**:
Configure hardware comparator high and low thresholds; ADC automatically fires an interrupt when sampled channel voltage exits the safe window without CPU polling.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you configure an ADC with Analog Watchdog to trigger interrupts on voltage spikes?
// Production-ready C firmware
```

---

<a id="q30"></a>
### Q30: What is Pulse Width Modulation (PWM) and how do hardware Timers generate variable duty cycles?

**Difficulty**: Beginner

**Strategy**:
Timer increments counter up to Auto-Reload Register (ARR); compares against Capture Compare Register (CCR); toggles output pin when counter matches CCR.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Pulse Width Modulation (PWM) and how do hardware Timers generate variable duty cycles?
// Production-ready C firmware
```

---

<a id="q31"></a>
### Q31: How do you implement Software Timers in FreeRTOS without creating separate tasks for each timer?

**Difficulty**: Intermediate

**Strategy**:
FreeRTOS uses a single Timer Daemon Service Task reading an internal timer queue; executes callback functions when timers expire.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement Software Timers in FreeRTOS without creating separate tasks for each timer?
// Production-ready C firmware
```

---

<a id="q32"></a>
### Q32: What is Endianness (Little-Endian vs Big-Endian) and how do you handle network byte order in firmware?

**Difficulty**: Beginner

**Strategy**:
Little-endian stores least significant byte first (ARM, x86); Big-endian stores most significant byte first (Network standard); use `ntohl()` and `htonl()` to convert.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Endianness (Little-Endian vs Big-Endian) and how do you handle network byte order in firmware?
// Production-ready C firmware
```

---

<a id="q33"></a>
### Q33: How do you design a Fail-Safe State Machine for safety-critical medical devices?

**Difficulty**: Advanced

**Strategy**:
State machine with explicit transition tables; illegal transitions trigger immediate transition to dedicated Safe State (valves closed, power cut), asserting hardware alarm.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you design a Fail-Safe State Machine for safety-critical medical devices?
// Production-ready C firmware
```

---

<a id="q34"></a>
### Q34: What is a Pull-Up and Pull-Down Resistor and why are floating inputs dangerous in CMOS circuits?

**Difficulty**: Beginner

**Strategy**:
Pull-up/down pins hold input at known voltage (VCC or GND) when switch is open; floating pins oscillate between logic states, drawing excessive leakage current and false triggering.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is a Pull-Up and Pull-Down Resistor and why are floating inputs dangerous in CMOS circuits?
// Production-ready C firmware
```

---

<a id="q35"></a>
### Q35: How do you measure Code Execution Time on bare-metal systems using DWT Cycle Counter?

**Difficulty**: Advanced

**Strategy**:
Enable Data Watchpoint and Trace (DWT) cycle counter register (`DWT->CYCCNT`); read counter before and after routine and divide by CPU clock frequency.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you measure Code Execution Time on bare-metal systems using DWT Cycle Counter?
// Production-ready C firmware
```

---

<a id="q36"></a>
### Q36: What is the difference between Flash Memory, SRAM, and EEPROM?

**Difficulty**: Beginner

**Strategy**:
Flash: non-volatile, block-erase, stores code; SRAM: volatile, fast, byte-accessible, stores runtime variables; EEPROM: non-volatile, byte-erasable, stores calibration parameters.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the difference between Flash Memory, SRAM, and EEPROM?
// Production-ready C firmware
```

---

<a id="q37"></a>
### Q37: How do you calibrate an internal RC Oscillator (HSI) against an external crystal (HSE)?

**Difficulty**: Intermediate

**Strategy**:
Measure number of HSI clock cycles between external 32.768kHz crystal pulses using input capture timer; adjust internal trimming register.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you calibrate an internal RC Oscillator (HSI) against an external crystal (HSE)?
// Production-ready C firmware
```

---

<a id="q38"></a>
### Q38: What is Clock Tree Configuration (PLL, Prescalers) in modern 32-bit MCUs?

**Difficulty**: Intermediate

**Strategy**:
Routes low-frequency external crystal (e.g. 8MHz) through Phase-Locked Loop (PLL) frequency multipliers and bus prescalers (AHB, APB) to clock CPU at 168MHz.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Clock Tree Configuration (PLL, Prescalers) in modern 32-bit MCUs?
// Production-ready C firmware
```

---

<a id="q39"></a>
### Q39: How do you implement Lock-Free Counting Semaphores in embedded C?

**Difficulty**: Advanced

**Strategy**:
Use atomic fetch-add and load instructions with atomic compare-and-swap (CAS) loops or LDREX/STREX ARM exclusive access instructions.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement Lock-Free Counting Semaphores in embedded C?
// Production-ready C firmware
```

---

<a id="q40"></a>
### Q40: What is Stack Overflow in embedded systems and how does FreeRTOS Stack Watermark detection work?

**Difficulty**: Intermediate

**Strategy**:
Task stack grows beyond allocated boundary corrupting adjacent memory; FreeRTOS fills stack with known byte pattern `0xA5` and checks if canary bytes at stack end are overwritten.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Stack Overflow in embedded systems and how does FreeRTOS Stack Watermark detection work?
// Production-ready C firmware
```

---

<a id="q41"></a>
### Q41: How do you configure an External Interrupt (EXTI) line on GPIO pins?

**Difficulty**: Beginner

**Strategy**:
Map GPIO pin to EXTI controller, configure rising/falling edge trigger registers, and enable corresponding interrupt line in NVIC.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you configure an External Interrupt (EXTI) line on GPIO pins?
// Production-ready C firmware
```

---

<a id="q42"></a>
### Q42: What is a Brown-Out Reset (BOR) and how does it prevent microcontroller flash corruption?

**Difficulty**: Intermediate

**Strategy**:
Hardware supervisor circuit holding MCU in reset state when supply voltage dips below minimum operating threshold, preventing unpredictable CPU instruction execution.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is a Brown-Out Reset (BOR) and how does it prevent microcontroller flash corruption?
// Production-ready C firmware
```

---

<a id="q43"></a>
### Q43: How do you implement CRC32 in hardware accelerators vs software lookup tables?

**Difficulty**: Intermediate

**Strategy**:
Feed data bytes into MCU hardware CRC peripheral; returns 32-bit checksum in 1 clock cycle; software lookup table takes hundreds of instructions.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement CRC32 in hardware accelerators vs software lookup tables?
// Production-ready C firmware
```

---

<a id="q44"></a>
### Q44: What is Real-Time Clock (RTC) backup domain and coin-cell battery power switching?

**Difficulty**: Beginner

**Strategy**:
Dedicated ultra-low-power domain running off external 32.768kHz crystal and V_BAT coin cell; maintains calendar date/time when main system power is removed.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Real-Time Clock (RTC) backup domain and coin-cell battery power switching?
// Production-ready C firmware
```

---

<a id="q45"></a>
### Q45: How do you perform Firmware Encryption and Secure Boot on modern MCUs?

**Difficulty**: Advanced

**Strategy**:
Hardware Cryptographic Engine verifies RSA/ECDSA public key signature in boot ROM; decrypts AES-128/256 encrypted firmware directly into Flash memory.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you perform Firmware Encryption and Secure Boot on modern MCUs?
// Production-ready C firmware
```

---

<a id="q46"></a>
### Q46: What is the difference between Polling, Interrupts, and DMA in peripheral data transfer?

**Difficulty**: Beginner

**Strategy**:
Polling: CPU constantly checks status register (wastes CPU); Interrupt: peripheral signals CPU when data arrives; DMA: hardware transfers data directly to RAM without CPU.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the difference between Polling, Interrupts, and DMA in peripheral data transfer?
// Production-ready C firmware
```

---

<a id="q47"></a>
### Q47: How do you handle Floating Ground and Ground Loops in industrial RS-485 / CAN communication?

**Difficulty**: Intermediate

**Strategy**:
Use galvanic isolation (optocouplers or digital isolators) and isolated DC-DC power supplies between microcontroller and transceiver.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you handle Floating Ground and Ground Loops in industrial RS-485 / CAN communication?
// Production-ready C firmware
```

---

<a id="q48"></a>
### Q48: What is Optical Isolation and how do Optocouplers protect digital inputs from high-voltage transients?

**Difficulty**: Beginner

**Strategy**:
Transfers electrical signals using light waves via internal infrared LED and phototransistor; provides thousands of volts of electrical isolation between circuits.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Optical Isolation and how do Optocouplers protect digital inputs from high-voltage transients?
// Production-ready C firmware
```

---

<a id="q49"></a>
### Q49: How do you interface an SD Card via SPI vs 4-bit SDIO mode in embedded firmware?

**Difficulty**: Intermediate

**Strategy**:
SPI mode uses 4 wires with lower bandwidth (<25MHz); SDIO uses dedicated clock, command, and 4 parallel data lines supporting high-speed 50MHz transfers.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you interface an SD Card via SPI vs 4-bit SDIO mode in embedded firmware?
// Production-ready C firmware
```

---

<a id="q50"></a>
### Q50: What is Open-Drain (Open-Collector) with external pull-up vs Push-Pull output?

**Difficulty**: Beginner

**Strategy**:
Push-pull actively drives output HIGH and LOW; Open-drain only drives LOW or disconnects (floating), relying on external pull-up resistor (used for I2C and wired-OR buses).

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Open-Drain (Open-Collector) with external pull-up vs Push-Pull output?
// Production-ready C firmware
```

---

<a id="q51"></a>
### Q51: How do you implement Mutex vs Binary Semaphore in RTOS task synchronization?

**Difficulty**: Intermediate

**Strategy**:
Binary Semaphore is for signaling between tasks/ISRs (no owner); Mutex is for mutual exclusion and must be released by the same task that acquired it (supports priority inheritance).

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement Mutex vs Binary Semaphore in RTOS task synchronization?
// Production-ready C firmware
```

---

<a id="q52"></a>
### Q52: What is the ARM Cortex-M Bit-Banding feature?

**Difficulty**: Advanced

**Strategy**:
Maps a 32MB bit-band alias memory region to an individual 1MB SRAM or peripheral bit region; writing to the alias address performs atomic bit set/clear in hardware.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the ARM Cortex-M Bit-Banding feature?
// Production-ready C firmware
```

---

<a id="q53"></a>
### Q53: How do you design an Uninterruptible Power Supply (UPS) monitoring circuit for embedded gateways?

**Difficulty**: Intermediate

**Strategy**:
Monitor battery voltage via ADC divider, detect AC mains drop via optocoupler interrupt, and safely flush filesystem buffers before triggering system shutdown.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you design an Uninterruptible Power Supply (UPS) monitoring circuit for embedded gateways?
// Production-ready C firmware
```

---

<a id="q54"></a>
### Q54: What is Dead Time Generation in Complementary PWM for Motor Control (H-Bridge)?

**Difficulty**: Advanced

**Strategy**:
Inserts small microsecond delay between turning off high-side MOSFET and turning on low-side MOSFET to prevent short-circuit 'shoot-through' across power rails.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Dead Time Generation in Complementary PWM for Motor Control (H-Bridge)?
// Production-ready C firmware
```

---

<a id="q55"></a>
### Q55: How do you implement a Software Watchdog for multiple concurrent RTOS tasks?

**Difficulty**: Intermediate

**Strategy**:
Dedicated watchdog task periodically checks if all worker tasks have updated their heartbeat flags; if any task fails to report within timeout, triggers system reset.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement a Software Watchdog for multiple concurrent RTOS tasks?
// Production-ready C firmware
```

---

<a id="q56"></a>
### Q56: What is Code Relocation and executing code from RAM instead of Flash?

**Difficulty**: Advanced

**Strategy**:
Copy function instructions from Flash to RAM at boot using linker script attribute `__attribute__((section(".ramfunc")))`; executed for zero-wait-state speed and flash erase safety.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Code Relocation and executing code from RAM instead of Flash?
// Production-ready C firmware
```

---

<a id="q57"></a>
### Q57: How do you measure Power Consumption using Current Shunt Monitors and INA219 sensors?

**Difficulty**: Beginner

**Strategy**:
Measures differential voltage drop across small precision shunt resistor ($V = I \times R$) using I2C ADC; calculates current and power consumption in milliwatts.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you measure Power Consumption using Current Shunt Monitors and INA219 sensors?
// Production-ready C firmware
```

---

<a id="q58"></a>
### Q58: What is the difference between ARM Cortex-M0, M3, M4, and M7 core architectures?

**Difficulty**: Intermediate

**Strategy**:
M0: ultra-low power 2-stage pipeline; M3: 3-stage pipeline with hardware divide; M4: adds DSP instructions and single-precision FPU; M7: 6-stage superscalar pipeline with double FPU and L1 cache.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the difference between ARM Cortex-M0, M3, M4, and M7 core architectures?
// Production-ready C firmware
```

---

<a id="q59"></a>
### Q59: How do you configure Hardware Flow Control (RTS/CTS) in UART communication?

**Difficulty**: Beginner

**Strategy**:
RTS (Request to Send) signals sender that receiver is ready for data; CTS (Clear to Send) tells transmitter to halt sending when receiver buffer is full.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you configure Hardware Flow Control (RTS/CTS) in UART communication?
// Production-ready C firmware
```

---

<a id="q60"></a>
### Q60: What is Static Memory Allocation in FreeRTOS (`configSUPPORT_STATIC_ALLOCATION = 1`)?

**Difficulty**: Intermediate

**Strategy**:
Allocates task TCB and stack buffers from statically declared arrays at compile time, eliminating heap fragmentation and fulfilling safety standards (IEC 61508).

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Static Memory Allocation in FreeRTOS (`configSUPPORT_STATIC_ALLOCATION = 1`)?
// Production-ready C firmware
```

---

<a id="q61"></a>
### Q61: How do you implement a PID (Proportional-Integral-Derivative) Controller in embedded C?

**Difficulty**: Intermediate

**Strategy**:
Calculate error ($e = \text{setpoint} - \text{measured}$); output $= K_p \cdot e + K_i \int e\,dt + K_d \frac{de}{dt}$; clamp output to actuator limits to prevent integral windup.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement a PID (Proportional-Integral-Derivative) Controller in embedded C?
// Production-ready C firmware
```

---

<a id="q62"></a>
### Q62: What is Cross-Compilation and how does a Toolchain (`arm-none-eabi-gcc`) build binaries for target MCUs?

**Difficulty**: Beginner

**Strategy**:
Compiles source code on host machine (x86) to generate machine code for a different target architecture (ARM); includes compiler, assembler, linker, and newlib C runtime.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Cross-Compilation and how does a Toolchain (`arm-none-eabi-gcc`) build binaries for target MCUs?
// Production-ready C firmware
```

---

<a id="q63"></a>
### Q63: How do you detect Hardware Faults (BusFault, MemManageFault, UsageFault) in ARM Cortex-M?

**Difficulty**: Advanced

**Strategy**:
Enable fault status registers in System Control Block (`SCB->SHCSR`); inspect CFSR register to diagnose divide-by-zero, unaligned access, or invalid memory fetch.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you detect Hardware Faults (BusFault, MemManageFault, UsageFault) in ARM Cortex-M?
// Production-ready C firmware
```

---

<a id="q64"></a>
### Q64: What is USB CDC (Communication Device Class) vs HID (Human Interface Device)?

**Difficulty**: Beginner

**Strategy**:
CDC emulates virtual COM port for high-speed serial data streaming; HID transfers input reports (keyboards, mice) using standard OS built-in drivers without custom driver installation.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is USB CDC (Communication Device Class) vs HID (Human Interface Device)?
// Production-ready C firmware
```

---

<a id="q65"></a>
### Q65: How do you handle Jitter in high-frequency Sensor Sampling?

**Difficulty**: Intermediate

**Strategy**:
Trigger ADC conversions using hardware timer output events (TRGO) rather than software loops; transfers samples via DMA with zero CPU timing jitter.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you handle Jitter in high-frequency Sensor Sampling?
// Production-ready C firmware
```

---

<a id="q66"></a>
### Q66: What is In-Circuit Emulation (ICE) and Boundary Scan in hardware manufacturing testing?

**Difficulty**: Advanced

**Strategy**:
Boundary scan (IEEE 1149.1) shifts test patterns through JTAG scan chains of all IC pins on a PCB to verify solder integrity and shorts without physical test probes.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is In-Circuit Emulation (ICE) and Boundary Scan in hardware manufacturing testing?
// Production-ready C firmware
```

---

<a id="q67"></a>
### Q67: How do you implement Dynamic Voltage and Frequency Scaling (DVFS) in low-power firmware?

**Difficulty**: Advanced

**Strategy**:
Scale CPU core clock frequency and internal voltage regulator dynamically based on current processing load to minimize active power consumption ($P \propto C V^2 f$).

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement Dynamic Voltage and Frequency Scaling (DVFS) in low-power firmware?
// Production-ready C firmware
```

---

<a id="q68"></a>
### Q68: What is the difference between Level-Triggered and Edge-Triggered Interrupts?

**Difficulty**: Beginner

**Strategy**:
Level-triggered fires continuously as long as pin remains at voltage level (requires clearing peripheral source); Edge-triggered fires once on rising/falling voltage transition.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the difference between Level-Triggered and Edge-Triggered Interrupts?
// Production-ready C firmware
```

---

<a id="q69"></a>
### Q69: How do you manage Flash Wear Leveling in embedded filesystems (LittleFS, SPIFFS)?

**Difficulty**: Intermediate

**Strategy**:
Rotates block writes evenly across all flash sectors to prevent premature memory cell degradation, tracking bad blocks and providing power-loss resilience.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you manage Flash Wear Leveling in embedded filesystems (LittleFS, SPIFFS)?
// Production-ready C firmware
```

---

<a id="q70"></a>
### Q70: What is a Bus Contention and how do tristate buffers prevent multiple devices driving a shared bus?

**Difficulty**: Beginner

**Strategy**:
Occurs when two devices drive opposite logic voltages (HIGH vs LOW) onto the same wire simultaneously; Tristate buffers place idle devices into high-impedance (High-Z) state.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is a Bus Contention and how do tristate buffers prevent multiple devices driving a shared bus?
// Production-ready C firmware
```

---

<a id="q71"></a>
### Q71: How do you configure an RTOS Queue with Queue Sets to wait on multiple queues simultaneously?

**Difficulty**: Intermediate

**Strategy**:
Combine multiple queues and semaphores into a FreeRTOS Queue Set; task blocks on `xQueueSelectFromSet` and wakes up whenever any member queue receives data.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you configure an RTOS Queue with Queue Sets to wait on multiple queues simultaneously?
// Production-ready C firmware
```

---

<a id="q72"></a>
### Q72: What is Memory Protection Unit (MPU) in ARM Cortex-M and how does it prevent buffer overflows?

**Difficulty**: Advanced

**Strategy**:
Hardware unit defining memory region access permissions (read/write/execute); raises MemManage fault if unprivileged task attempts to access forbidden kernel RAM regions.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Memory Protection Unit (MPU) in ARM Cortex-M and how does it prevent buffer overflows?
// Production-ready C firmware
```

---

<a id="q73"></a>
### Q73: How do you implement Software I2C Clock Stretching?

**Difficulty**: Intermediate

**Strategy**:
When slave needs time to process data, it pulls SCL line LOW; master detects SCL held LOW and pauses clock generation until slave releases line HIGH.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement Software I2C Clock Stretching?
// Production-ready C firmware
```

---

<a id="q74"></a>
### Q74: What is Overclocking Microcontrollers and what are the hardware risks (Timing Violations, Thermal Runaway)?

**Difficulty**: Intermediate

**Strategy**:
Exceeding manufacturer clock specs causes setup/hold timing violations in internal flip-flops, memory corruption, and increased leakage current leading to permanent latch-up.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Overclocking Microcontrollers and what are the hardware risks (Timing Violations, Thermal Runaway)?
// Production-ready C firmware
```

---

<a id="q75"></a>
### Q75: How do you implement Heartbeat LED blinking using Non-Blocking Timers in bare-metal systems?

**Difficulty**: Beginner

**Strategy**:
Record system tick timestamp; check if `current_tick - last_toggle >= BLINK_INTERVAL`; toggles LED state without executing blocking `delay()` functions.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement Heartbeat LED blinking using Non-Blocking Timers in bare-metal systems?
// Production-ready C firmware
```

---

<a id="q76"></a>
### Q76: What is Boundary Check and Defending against Buffer Overflows in Embedded C?

**Difficulty**: Beginner

**Strategy**:
Always check array index against array capacity before write; replace dangerous functions (`strcpy`, `sprintf`) with bounded equivalents (`strncpy`, `snprintf`).

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Boundary Check and Defending against Buffer Overflows in Embedded C?
// Production-ready C firmware
```

---

<a id="q77"></a>
### Q77: How do you configure Hardware Acceleration for Cryptography (AES, SHA) on microcontrollers?

**Difficulty**: Intermediate

**Strategy**:
Feed key and data blocks into memory-mapped registers of hardware crypto coprocessor; reads encrypted output in 16 clock cycles instead of thousands of CPU cycles.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you configure Hardware Acceleration for Cryptography (AES, SHA) on microcontrollers?
// Production-ready C firmware
```

---

<a id="q78"></a>
### Q78: What is the difference between Volatile Memory and Non-Volatile Memory?

**Difficulty**: Beginner

**Strategy**:
Volatile loses data when power is disconnected (SRAM, DRAM); Non-Volatile retains stored data permanently without power (Flash, EEPROM, FRAM).

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the difference between Volatile Memory and Non-Volatile Memory?
// Production-ready C firmware
```

---

<a id="q79"></a>
### Q79: How do you debug an intermittent system freeze using an external Hardware Logic Analyzer?

**Difficulty**: Intermediate

**Strategy**:
Attach logic analyzer probes to communication pins (UART TX, SPI MOSI) and toggle debug GPIO pins at key firmware milestones; inspect trace timelines to pinpoint freeze point.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you debug an intermittent system freeze using an external Hardware Logic Analyzer?
// Production-ready C firmware
```

---

<a id="q80"></a>
### Q80: What is Context Switching Overhead and how does Hardware Register Stacking affect RTOS latency?

**Difficulty**: Advanced

**Strategy**:
CPU pushes current task registers to stack, swaps stack pointer to next task, and pops new registers; takes 12-40 clock cycles depending on FPU lazy stacking.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Context Switching Overhead and how does Hardware Register Stacking affect RTOS latency?
// Production-ready C firmware
```

---

<a id="q81"></a>
### Q81: How do you design a Low-Power Wake-On-Motion system using an Accelerometer interrupt?

**Difficulty**: Intermediate

**Strategy**:
Configure I2C accelerometer to run in low-power mode (<5uA); when acceleration exceeds G-threshold, accelerometer asserts interrupt pin waking MCU from deep sleep.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you design a Low-Power Wake-On-Motion system using an Accelerometer interrupt?
// Production-ready C firmware
```

---

<a id="q82"></a>
### Q82: What is the difference between Thread Mode and Handler Mode in ARM Cortex-M?

**Difficulty**: Intermediate

**Strategy**:
Thread mode is normal execution mode for user code/tasks (can be privileged or unprivileged); Handler mode is entered automatically when servicing exceptions/interrupts (always privileged).

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the difference between Thread Mode and Handler Mode in ARM Cortex-M?
// Production-ready C firmware
```

---

<a id="q83"></a>
### Q83: How do you calibrate an Analog Temperature Sensor using Two-Point Calibration?

**Difficulty**: Intermediate

**Strategy**:
Measure ADC readings at two known temperatures ($0^\circ C$ ice bath, $100^\circ C$ boiling water); calculate slope $m$ and offset $c$ for linear transfer function $T = m \cdot ADC + c$.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you calibrate an Analog Temperature Sensor using Two-Point Calibration?
// Production-ready C firmware
```

---

<a id="q84"></a>
### Q84: What is CAN FD (Flexible Data-Rate) and how does it improve over classical CAN 2.0B?

**Difficulty**: Intermediate

**Strategy**:
Increases maximum data payload from 8 bytes to 64 bytes per frame, and boosts data-phase transmission speeds from 1 Mbps up to 5-8 Mbps.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is CAN FD (Flexible Data-Rate) and how does it improve over classical CAN 2.0B?
// Production-ready C firmware
```

---

<a id="q85"></a>
### Q85: How do you prevent Deadlocks in multi-threaded RTOS applications?

**Difficulty**: Intermediate

**Strategy**:
Enforce strict hierarchical lock acquisition order across all tasks, use timeout-bounded mutex acquisition (`xSemaphoreTake(mutex, 100)`), and avoid nested locks.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you prevent Deadlocks in multi-threaded RTOS applications?
// Production-ready C firmware
```

---

<a id="q86"></a>
### Q86: What is Asynchronous Serial Framing Error and what causes it in UART?

**Difficulty**: Beginner

**Strategy**:
Receiver fails to detect the expected stop bit at the scheduled bit-time period; caused by baud rate mismatch (>3% deviation) or electrical noise on the RX wire.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Asynchronous Serial Framing Error and what causes it in UART?
// Production-ready C firmware
```

---

<a id="q87"></a>
### Q87: How do you implement Software-Based Watchdog Petting across distributed sensor nodes?

**Difficulty**: Intermediate

**Strategy**:
Sensor nodes send periodic telemetry heartbeats to gateway; gateway triggers hardware alarm if any remote node fails to report within expected window.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement Software-Based Watchdog Petting across distributed sensor nodes?
// Production-ready C firmware
```

---

<a id="q88"></a>
### Q88: What is the purpose of the Assembly Reset Handler (`Reset_Handler`) in startup code?

**Difficulty**: Advanced

**Strategy**:
First code executed after CPU reset: copies `.data` segment from Flash to RAM, zeroes out `.bss` segment in RAM, initializes system clocks, and branches to `main()`.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the purpose of the Assembly Reset Handler (`Reset_Handler`) in startup code?
// Production-ready C firmware
```

---

<a id="q89"></a>
### Q89: How do you handle Floating Point Numbers on MCUs with Single-Precision vs Double-Precision FPU?

**Difficulty**: Intermediate

**Strategy**:
Operations on 32-bit `float` execute in 1-2 hardware cycles; operations on 64-bit `double` on single-precision FPUs emulate in software, taking hundreds of cycles.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you handle Floating Point Numbers on MCUs with Single-Precision vs Double-Precision FPU?
// Production-ready C firmware
```

---

<a id="q90"></a>
### Q90: What is Hardware CRC Calculation for Packet Integrity in wireless RF links (LoRa, BLE)?

**Difficulty**: Beginner

**Strategy**:
Hardware calculates CRC polynomial on outgoing packet payload; receiving radio hardware verifies CRC and automatically drops corrupted packets without waking CPU.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Hardware CRC Calculation for Packet Integrity in wireless RF links (LoRa, BLE)?
// Production-ready C firmware
```

---

<a id="q91"></a>
### Q91: How do you configure an ADC for Differential Input Measurements?

**Difficulty**: Intermediate

**Strategy**:
Measures voltage difference between two analog pins ($V_{\text{diff}} = V_+ - V_-$) rather than pin to ground, cancelling out common-mode electromagnetic noise.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you configure an ADC for Differential Input Measurements?
// Production-ready C firmware
```

---

<a id="q92"></a>
### Q92: What is Safety Integrity Level (SIL / ASIL) and what firmware processes are required for ISO 26262?

**Difficulty**: Advanced

**Strategy**:
Automotive functional safety standard requiring formal hazard analysis, dual-core lockstep hardware, 100% MC/DC test coverage, and static analysis compliance.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Safety Integrity Level (SIL / ASIL) and what firmware processes are required for ISO 26262?
// Production-ready C firmware
```

---

<a id="q93"></a>
### Q93: How do you implement an On-Chip EEPROM Emulation in Flash memory?

**Difficulty**: Intermediate

**Strategy**:
Uses two alternating Flash sectors; writes variable updates sequentially as (key, value) pairs; when active sector is full, copies latest valid values to secondary sector and erases old sector.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement an On-Chip EEPROM Emulation in Flash memory?
// Production-ready C firmware
```

---

<a id="q94"></a>
### Q94: What is Jitter and Latency in Interrupt Handling (Interrupt Latency)?

**Difficulty**: Intermediate

**Strategy**:
Delay between hardware assertion of interrupt line and execution of first instruction of ISR; influenced by active instruction completion, pipeline reload, and register stacking.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is Jitter and Latency in Interrupt Handling (Interrupt Latency)?
// Production-ready C firmware
```

---

<a id="q95"></a>
### Q95: How do you design an Ultra-Reliable Embedded System that recovers automatically from cosmic-ray Single Event Upsets (SEU)?

**Difficulty**: Advanced

**Strategy**:
Use ECC RAM, run periodic memory scrubbers, configure Independent Watchdog timers, validate data structures with CRCs, and maintain redundant critical variables.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you design an Ultra-Reliable Embedded System that recovers automatically from cosmic-ray Single Event Upsets (SEU)?
// Production-ready C firmware
```

---

<a id="q96"></a>
### Q96: What is the purpose of the Assembly HardFault Trampoline in ARM Cortex-M?

**Difficulty**: Advanced

**Strategy**:
Checks EXC_RETURN bit 2 to determine whether MSP or PSP stack was in use, moving the stack pointer into R0 before calling the C fault handler.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the purpose of the Assembly HardFault Trampoline in ARM Cortex-M?
// Production-ready C firmware
```

---

<a id="q97"></a>
### Q97: How do you configure Real-Time Trace with ARM CoreSight Embedded Trace Macrocell (ETM)?

**Difficulty**: Advanced

**Strategy**:
Streams uncompressed instruction execution trace out of dedicated high-speed trace pins to an external trace capture probe (J-Trace) without slowing CPU.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you configure Real-Time Trace with ARM CoreSight Embedded Trace Macrocell (ETM)?
// Production-ready C firmware
```

---

<a id="q98"></a>
### Q98: What is the difference between Edge-Aligned and Center-Aligned PWM for Motor Drivers?

**Difficulty**: Intermediate

**Strategy**:
Center-aligned counts up and down, reducing harmonic distortion and electromagnetic noise (EMI) on three-phase BLDC motor drives.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: What is the difference between Edge-Aligned and Center-Aligned PWM for Motor Drivers?
// Production-ready C firmware
```

---

<a id="q99"></a>
### Q99: How do you implement Non-Volatile Parameter Storage using Wear-Resistant Wear Leveling in NOR Flash?

**Difficulty**: Intermediate

**Strategy**:
Appends records sequentially to active 4KB sector with state flags; erases old sector only when full after migrating active keys.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you implement Non-Volatile Parameter Storage using Wear-Resistant Wear Leveling in NOR Flash?
// Production-ready C firmware
```

---

<a id="q100"></a>
### Q100: How do you prevent Microcontroller Latch-Up caused by Input Overvoltage?

**Difficulty**: Beginner

**Strategy**:
Place current-limiting series resistors and external Schottky clamping diodes to VCC and GND on input lines to clamp voltage spikes.

**Code Example**:
```c
// Embedded Systems & RTOS Implementation for: How do you prevent Microcontroller Latch-Up caused by Input Overvoltage?
// Production-ready C firmware
```

---
