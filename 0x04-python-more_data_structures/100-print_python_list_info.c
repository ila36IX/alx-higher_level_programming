#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Print some basic python list
 * @p: Python oject
 */
void print_python_list_info(PyObject *p)
{
	long int length = Py_SIZE(p);
	long int i;
	PyObject *el;
	PyListObject *cloneP = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %li\n", cloneP->allocated);
	for (i = 0; i < length; i++)
	{
		el = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(el)->tp_name);
	}

}
