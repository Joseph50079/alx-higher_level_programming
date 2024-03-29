#include <Python.h>

void print_python_list_info(PyObject *p)
{
	if (!PyList_Check(p)) {
		PyErr_SetString(PyExc_TypeError, "Object is not a Python list");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);

	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++) {
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

