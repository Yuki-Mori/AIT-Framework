#include "app.h"

void *__dso_handle=0;
void initialize_task(intptr_t exinf) {
    ext_tsk();
}

void main_flow_cyc(intptr_t exinf) {
}

void main_flow_task(intptr_t exinf){
    ext_tsk();
}

void sensor_task(intptr_t exinf) {
    ext_tsk();
}

void motor_task(intptr_t exinf){
    ext_tsk();
}

void screen_task(intptr_t unused) {
    ext_tsk();
}

void file_stream_task(intptr_t unused){
    ext_tsk();
}
