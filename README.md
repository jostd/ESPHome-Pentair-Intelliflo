# ESPHome-Pentair-Intelliflo-VS
This is a brach of https://github.com/nicostrown/ESPHome-Pentair-Intelliflo:main
This works on the original Variable Speed Pump. The setRPM RS485 is 0x01 instead of 0x0A. 
GPIO pins modified for M5Stack Atomic RS485.
This pump has no pressure sensor and the program status is always zero. So I removed flow control and the following sensors: flow, pressure and program.

<img width="251" height="455" alt="image" src="https://github.com/user-attachments/assets/3859b733-d521-4371-8814-79755097b959" />

Also, the Pump-Mode selector now also has an 'off' mode and an energy sensor is added to track the pumps consumption on the energy dashboard.

Hardware used:
  - https://shop.m5stack.com/products/atom-lite-esp32-development-kit
  <img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/0a4d37e5-8ed7-4f7a-baed-375e59900ea4" />
  
  - https://shop.m5stack.com/products/atomic-rs485-base
  <img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/e1f63e0c-dbb5-4759-beb5-8c4a9cb8fdf2" />


