# Simple example Python script for SoC estimation
import pandas as pd

def estimate_soc(voltage):
    soc = (voltage - 3.0) / (4.2 - 3.0) * 100
    return max(0, min(soc, 100))

if __name__ == "__main__":
    print("Example: SoC for 3.8V =", estimate_soc(3.8), "%")
