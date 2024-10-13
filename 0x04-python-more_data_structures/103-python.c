#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints basic info about Python bytes objects
 * @p: PyObject pointer to a bytes object
 */
void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyObject_Length(p);
    const char *str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %zd bytes: ", size < 10 ? size : 10);

    for (Py_ssize_t i = 0; i < (size < 10 ? size : 10); i++)
    {
        printf("%02x", (unsigned char)str[i]);
        if (i < (size < 10 ? size - 1 : 9))
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_list - prints basic info about Python lists
 * @p: PyObject pointer to a list object
 */
void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyObject_Length(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %zd: ", i);
        if (PyBytes_Check(item))
        {
            print_python_bytes(item);
        }
        else
        {
            printf("%s\n", Py_TYPE(item)->tp_name);
        }
    }
}
