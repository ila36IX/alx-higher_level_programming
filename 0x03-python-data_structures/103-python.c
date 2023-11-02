#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list(PyObject *p)
{
	long int i;
	PyVarObject *o = (PyVarObject *) p;
	PyListObject *obj = (PyListObject *) p;
	long int size = o->ob_size;
	const char *type_str = NULL;
	
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", obj->allocated);
	for (i = 0; i < size; i++)
	{
		type_str = ((obj->ob_item[i])->ob_type)->tp_name;
		printf("Element %ld: %s\n", i, type_str);
	}
}

void print_python_bytes(PyObject *p)
{
	char *str;
	long int size;
	long int first_chars = 0;
	long int i;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
 	 	printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	str = PyBytes_AsString(p);
	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		first_chars = size + 1;
	else
		first_chars = 10;
	printf("  first %ld bytes:", first_chars);
	for (i = 0; i < first_chars; i++)
	{
		printf(" ");
		printf("%02x", str[i]);
	}
	printf("\n");
}
