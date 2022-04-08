#define PY_SSIZE_T_CLEAN
//#define Py_LIMITED_API
#include <Python.h>
#include <stdint.h>
#include "foo.h"


typedef struct {
    PyObject_HEAD;
    uintptr_t user;
} userobj;


static PyObject *
userobj_printname(userobj *self)
{
    user_print_name(self->user);

    Py_INCREF(Py_None);
    return Py_None;
}


static PyObject *
userobj_setname(userobj *self, PyObject *arg)
{
    char *name;

    if (!PyUnicode_Check(arg)) {
        PyErr_SetString(PyExc_TypeError,
                        "The first attribute value must be a string");
        return NULL;
    }

    user_set_name(self->user, PyUnicode_AsUTF8(arg));

    Py_INCREF(Py_None);
    return Py_None;
}


static PyMethodDef userobj_methods[] = {
    {"set_name", (PyCFunction)userobj_setname, METH_O,
        PyDoc_STR("")},
    {"print_name", (PyCFunction)userobj_printname, METH_NOARGS,
        PyDoc_STR("")},
    {NULL,      NULL},
};


static PyObject *
userobj_new(PyTypeObject *type, PyObject *args, PyObject *kwargs)
{
    userobj *obj;

    obj = (userobj *)type->tp_alloc(type, 0);
    if (obj == NULL)
        return NULL;

    obj->user = user_new();

    return (PyObject *)obj;
}


static void
userobj_dealloc(userobj *self)
{
    user_free(self->user);
    Py_TYPE(self)->tp_free((PyObject *) self);
}


static PyTypeObject userobj_type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "foo.user",
    .tp_doc = "Example of GO object",
    .tp_basicsize = sizeof(userobj),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_methods = userobj_methods,
    .tp_dealloc = (destructor) userobj_dealloc,
    .tp_new = userobj_new,
};


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
    PyModuleDef_HEAD_INIT,
    .m_name = "foo",
    .m_doc = NULL,
    .m_size = -1, 
    .m_methods = methods,
};


PyMODINIT_FUNC PyInit_foo(void) {
    PyObject *m;
    
    if (PyType_Ready(&userobj_type) < 0)
        return NULL;

    m = PyModule_Create(&foomodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&userobj_type);
    if (PyModule_AddObject(m, "user", (PyObject *) &userobj_type) < 0) {
        Py_DECREF(&userobj_type);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}

