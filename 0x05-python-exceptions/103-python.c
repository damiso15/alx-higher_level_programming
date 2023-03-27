#include <Python.h>
#include <float.h>

#define STR(s) #s
#define ERR_PREFIX "  Error"
#define ERR_INVALID_LIST ERR_PREFIX " [ERROR] Invalid List Object"
#define ERR_INVALID_BYTES ERR_PREFIX " [ERROR] Invalid Bytes Object"
#define ERR_INVALID_FLOAT ERR_PREFIX " [ERROR] Invalid Float Object"

/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to PyObject (PyListObject)
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	PyObject *obj;
	ssize_t i, size, alloc;

	fflush(stdout);

	if (!PyList_Check(p))
	{
		puts(ERR_INVALID_LIST);
		return;
	}

	list = (PyListObject *)p;
	size = PyList_Size(p);
	alloc = list->allocated;

	printf("[*] Python list info\n"
	       "[*] Size of the Python List = %zd\n"
	       "[*] Allocated = %zd\n", size, alloc);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(obj)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

/**
 * print_python_bytes - print some basic info about Python bytes
 * @p: pointer to PyObject (PyBytesObject)
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	ssize_t i, size;
	char *str;

	fflush(stdout);

	if (!PyBytes_Check(p))
	{
		puts(ERR_INVALID_BYTES);
		return;
	}

	bytes = (PyBytesObject *)p;
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n"
	       "  size: %zd\n"
	       "  trying string: %s\n"
	       "  first %zd bytes:", size, str ? str : "", size < 10 ? size : 10);

	for (i = 0; i < size && i < 10; i++)
		printf(" %02x", (unsigned char)str[i]);

	putchar('\n');
}

/**
 * print_python_float - print some basic info about Python float objects
 * @p: pointer to PyObject (PyFloatObject)
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *flt;

	fflush(stdout);

	if (!PyFloat_Check(p))
	{
		puts(ERR_INVALID_FLOAT);
		return;
	}

	flt = (PyFloatObject *)p;

	if (Py_IS_NAN(flt->ob_fval))
		printf("[-] float object inf\n");
	else if (Py_IS_INFINITY(flt->ob_fval) && flt->ob_fval > 0)
		printf("[-] float object inf\n");
	else if (Py_IS_INFINITY(flt->ob_fval) && flt->ob_fval < 0)
		printf("[-] float object -inf\n");
	else
		printf("[.] float object info\n"
		       "  value: %.*g\n", DBL_DIG, flt->ob_fval);
}

