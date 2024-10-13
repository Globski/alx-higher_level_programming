#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, alloc, i;
    PyObject *item;

    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", alloc);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);  // Safely get the item
        printf("Element %zd: ", i);
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        } else {
            printf("(%s)\n", Py_TYPE(item)->tp_name);  // Print the type of the item
        }
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size;
    const char *str;

    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);
    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str ? str : "(null)");

    size = (size < 10) ? size : 10;
    printf("  first %zd bytes: ", size);
    for (Py_ssize_t i = 0; i < size; i++) {
        printf("%02hhx", (unsigned char)str[i]);
        if (i < size - 1) {
            printf(" ");
        }
    }
    printf("\n");
}
