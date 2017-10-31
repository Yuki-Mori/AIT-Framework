from config import settings

def generateConfig():
    add_app_str = ''
    for module in settings.CPP_MODULES:
        add_app_str += "ATT_MOD(\"{module}\");\n".format(module=module+'.o')

    return settings.APP_CONFIG_HEADER + add_app_str

def generateMakefile():
    libraries = ''
    app_dirs = ''
    app_includes = ''

    for library in settings.INCLUDE_LIBRARIES:
        libraries += settings.LIBRARY_TEMPLATE.format(library_name = library) + '\n'

    for directory in settings.DIRECTORIES:
        app_dirs += settings.APP_DIR_TEMPLATE.format(dir_name = directory) + ' '
        app_includes += settings.APP_INCLUDE_TEMPLATE.format(dir_name = directory) + ' '

    cpp_objs = ''
    if len(settings.CPP_MODULES) != 0:
        cpp_objs = '.o '.join(settings.CPP_MODULES)+'.o'

    return settings.MAKEFILE_TEMPLATE.format(
        c_objs='',
        cpp_objs=cpp_objs,
        libraries=libraries,
        app_dirs=app_dirs,
        app_includes=app_includes
    )
