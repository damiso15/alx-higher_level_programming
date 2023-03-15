#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints some basic info about Python lists.
 * @p: A PyObject pointer to a Python list.
 **/
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - Prints some basic info about Python bytes objects.
 * @p: A PyObject pointer to a Python bytes object.
 **/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	char *s;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	for (size = 0; size < PyBytes_Size(p) && size < 10; size++)
	{
		s = PyBytes_AsString(p) + size;
		printf(" %02hhx", *s);
	}
	printf("\n");
}

