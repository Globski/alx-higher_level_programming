#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints basic info about Python bytes objects.
 * @p: A PyObject pointer to a bytes object.
 */
void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    const char *str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str ? str : "(null)");
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
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject pointer to a list object.
 */
void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

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
