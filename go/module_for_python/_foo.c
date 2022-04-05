#define PY_SSIZE_T_CLEAN
#define Py_LIMITED_API
#include <Python.h>
#include "foo.h"


static PyObject *say_wrapper(PyObject *self) {
    say();
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef methods[] = {
    {"say", (PyCFunction)say_wrapper, METH_NOARGS, "Just saying hello."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef foomodule = {
    PyModuleDef_HEAD_INIT, "foo", NULL, -1, methods
};

PyMODINIT_FUNC PyInit_foo(void) {
    return PyModule_Create(&foomodule);
}

