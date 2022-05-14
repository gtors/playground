/*
 * This file defines 3 modules (multi, multi.foo, multi.bar),
 * only the first one is called the same as the compiled file.
 */
#include<Python.h>

static struct PyModuleDef multi = {
    PyModuleDef_HEAD_INIT,
    "multi",
    "multi doc",
    -1,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC PyInit_multi(void)
{
    // TODO: refcounting & check nulls
    PyObject *builtins = PyImport_ImportModule("builtins");
    PyObject *eval = PyObject_GetAttrString(builtins, "exec");
    char* load_modules_expression = 
        "from importlib.machinery import ModuleSpec, ExtensionFileLoader\n"
        "from importlib.util import module_from_spec, find_spec\n"
        "multi_spec = find_spec('multi')\n"
        "for name in ('multi.foo', 'multi.bar'):\n"
        "    spec = ModuleSpec(name, ExtensionFileLoader(name, 'multi.so'), origin=multi_spec.origin)\n"
        "    module = module_from_spec(spec)\n"
        "    spec.loader.exec_module(module)\n"
        ;
    PyObject *args = Py_BuildValue("(s)", load_modules_expression);
    PyObject *result = PyObject_CallObject(eval, args);

    return PyModule_Create(&multi);
}

static struct PyModuleDef _foomodule = {
    PyModuleDef_HEAD_INIT,
    "multi.foo",
    "multi.foo doc",
    -1,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC PyInit_foo(void)
{
    return PyModule_Create(&_foomodule);
}

static struct PyModuleDef _barmodule = {
    PyModuleDef_HEAD_INIT,
    "multi.bar",
    "multi.bar doc",
    -1,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC PyInit_bar(void){
    return PyModule_Create(&_barmodule);
}
