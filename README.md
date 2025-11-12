# EV Battery Management System (BMS)

This project focuses on developing a Battery Management System for an Electric Vehicle.  
It includes SOC estimation algorithms, thermal modeling, firmware for STM32, and PCB design.

## Features
- Real-time SoC estimation using Coulomb counting
- CAN-based data communication
- Cell voltage and temperature monitoring
- MATLAB Simulink simulations
- Custom PCB design using KiCad

## Tools Used
- MATLAB/Simulink  
- STM32CubeIDE  
- KiCad  
- Python for data analysis

## Folder Overview
| Folder | Description |
|---------|--------------|
| `/Simulations` | MATLAB and Simulink models |
| `/Firmware` | Microcontroller source code |
| `/Hardware` | Circuit and PCB design files |
| `/Documentation` | Reports, results, and presentations |
| `/Python_Tools` | Scripts for testing and analysis |

## How to Run
1. Open `Simulations/BMS_SOC_Model.slx` in MATLAB.
2. Run `python Python_Tools/soc_estimation.py` to analyze SoC data.
3. Flash firmware using STM32CubeIDE.

---

📌 *Developed by Swati Sharma*  
📅 *2025 Project*
