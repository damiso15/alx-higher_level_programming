#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print basic information about Python bytes objects
 * @p: A pointer to a PyObject
 *
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *s;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
	printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
	s = ((PyBytesObject *)p)->ob_sval;
	for (i = 0; i < size && i < 10; i++)
		printf("%02hhx%c", s[i], i + 1 < size && i < 9 ? ' ' : '\n');
}

/**
 * print_python_list - Print basic information about Python lists
 * @p: A pointer to a PyObject
 *
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
