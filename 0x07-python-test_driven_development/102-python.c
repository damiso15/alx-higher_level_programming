#include <Python.h>

/**
 * print_python_string - Prints some basic info about a Python string object
 * @p: A pointer to a PyObject object representing a string
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t len;
    Py_UNICODE *str;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    len = PyUnicode_GET_LENGTH(p);
    str = PyUnicode_AsUnicode(p);

    printf("  type: %s\n", (sizeof(Py_UNICODE) == 2) ? "compact unicode object" : "unicode object");
    printf("  length: %ld\n", len);
    printf("  value: %ls\n", str);
}

