#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: the Python object representing the list
 *
 * This function prints the size, allocated space, and elements in the list.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;
    PyObject *item;

    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, item->ob_type->tp_name);

        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: the Python object representing the bytes
 *
 * This function prints the size, string representation, and the first few bytes.
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size;
    char *string;
    Py_ssize_t i;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);

    /* print first 10 bytes */
    printf("  first %zd bytes: ", (size < 10) ? size + 1 : 10);
    for (i = 0; i < size + 1 && i < 10; i++) {
        printf("%02hhx ", string[i]);
    }
    printf("\n");
}
