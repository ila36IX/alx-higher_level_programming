#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <string.h>

#define ngtf(n) ((n >= 0) ? (n) : (n + 0xff + 1))

/**
 * print_python_bytes - Print python bytes infos
 *
 * @p: Bytes object
 * Return: Nothing
 */
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
		printf("%02x", ngtf(str[i]));
	}
	printf("\n");
}

/**
 * print_python_list - Print list details
 *
 * @p: List object
 * Return: Nothing
 */
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
		if (PyBytes_Check(obj->ob_item[i]))
			print_python_bytes(obj->ob_item[i]);
	}
}
