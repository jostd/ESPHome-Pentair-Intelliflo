# ESPHome-Pentair-Intelliflo-VS
This is a brach of https://github.com/nicostrown/ESPHome-Pentair-Intelliflo:main
This works on the original Variable Speed Pump. The setRPM RS485 is 0x01 instead of 0x0A. 
GPIO pins modified for M5Stack Atomic RS485.
This pump has no pressure sensor and the program status is always zero. So I removed flow control and the following sensors: flow, pressure and program.

<img width="251" height="455" alt="image" src="https://github.com/user-attachments/assets/3859b733-d521-4371-8814-79755097b959" />

Also, the Pump-Mode selector now also has an 'off' mode.
