APP_NAME = 'aitframework-alpha'

CPP_MODULES = [
    'String',
]

DIRECTORIES = [
    'AITFramework',
]

INCLUDE_LIBRARIES = [
    'libcpp-ev3',
    'libcpp-ev3ext',
]

TASK_DEFINITIONS = '''
DOMAIN(TDOM_APP) {
        CRE_TSK( INITIALIZE_TASK, {TA_ACT, 0, initialize_task, MAIN_PRIORITY, STACK_SIZE, NULL } );
        CRE_TSK( SCREEN_TASK, { TA_NULL,  0, screen_task,   SCREEN_PRIORITY,   STACK_SIZE, NULL } );
        CRE_TSK( SENSOR_TASK, { TA_NULL,  0, sensor_task,   SENSOR_PRIORITY,   STACK_SIZE, NULL } );
        CRE_TSK( MOTOR_TASK, { TA_NULL,  0, motor_task,   RUNNING_PRIORITY,   STACK_SIZE, NULL } );
        CRE_TSK( MAIN_FLOW_TASK, { TA_NULL,  0, main_flow_task,   MAIN_PRIORITY,   STACK_SIZE, NULL } );
        CRE_TSK( FILE_STREAM_TASK, { TA_NULL,  0, file_stream_task,   FILE_STREAM_PRIORITY,   STACK_SIZE, NULL } );

        EV3_CRE_CYC( MAIN_FLOW_CYC, { TA_NULL, 0, main_flow_cyc, 4, 1});
}
'''

LIBRARY_TEMPLATE = 'include $(EV3RT_SDK_LIB_DIR)/{library_name}/Makefile'
APP_DIR_TEMPLATE = '$(mkfile_path){dir_name}/src'
APP_INCLUDE_TEMPLATE = '-I$(mkfile_path){dir_name}/include'


APP_CONFIG_HEADER = """
INCLUDE("app_common.cfg");

#include "app.h"

{task_definition}

ATT_MOD("app.o");
""".format(task_definition=TASK_DEFINITIONS)

MAKEFILE_TEMPLATE = """
mkfile_path := $(dir $(lastword $(MAKEFILE_LIST)))
COPTS += -fno-use-cxa-atexit
SRCLANG := c++


APPL_COBJS += {c_objs}
APPL_CXXOBJS += {cpp_objs}

ifdef CONFIG_EV3RT_APPLICATION
# Include libraries
{libraries}
endif

APPL_DIR += {app_dirs}
INCLUDES += {app_includes}
"""
