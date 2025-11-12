// Main firmware for EV BMS
#include "bms.h"
int main() {
    BMS_Init();
    while(1) {
        BMS_Update();
    }
}
