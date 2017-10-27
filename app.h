#ifdef __cplusplus
extern "C" {
#endif

#include "ev3api.h"

#define MIDWAY_NUM 1
#define MAIN_PRIORITY           TMIN_APP_TPRI + 1
#define RUNNING_PRIORITY        MAIN_PRIORITY + 3 //モータ周りのタスク用の優先度
#define SENSOR_PRIORITY         MAIN_PRIORITY + 1 //センサ周りのタスクの優先度
#define CALCULATION_PRIORITY    MAIN_PRIORITY + 2 //各種計算用タスクの優先度
#define SCREEN_PRIORITY         MAIN_PRIORITY + 4 //スクリーンタスクの優先度
#define FILE_STREAM_PRIORITY    MAIN_PRIORITY + 5

#ifndef STACK_SIZE
#define STACK_SIZE      4096
#endif /* STACK_SIZE */

#ifndef TOPPERS_MACRO_ONLY

void msg_f(const char *str, int32_t line);

extern void screen_task(intptr_t exinf);
extern void sensor_task(intptr_t exinf);
extern void motor_task(intptr_t exinf);
extern void main_flow_task(intptr_t exinf);
extern void main_flow_cyc(intptr_t exinf);
extern void initialize_task(intptr_t exinf);
extern void file_stream_task(intptr_t exinf);




#endif /* TOPPERS_MACRO_ONLY */

#ifdef __cplusplus
}
#endif
