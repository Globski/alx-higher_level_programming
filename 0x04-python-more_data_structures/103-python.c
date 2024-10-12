#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints basic information about a Python bytes object.
 * @bytes_obj: PyObject pointer to a bytes object.
 */
void print_python_bytes(PyObject *bytes_obj)
{
	Py_ssize_t size, i;
	const char *str;

	if (!PyBytes_Check(bytes_obj))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(bytes_obj);
	str = PyBytes_AsString(bytes_obj);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes: ", size < 10 ? size : 10);

	for (i = 0; i < (size < 10 ? size : 10); i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < (size < 10 ? size - 1 : 9))
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - Prints basic information about a Python list object.
 * @list_obj: PyObject pointer to a list object.
 */
void print_python_list(PyObject *list_obj)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	if (!PyList_Check(list_obj))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(list_obj);
	allocated = ((PyListObject *)list_obj)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(list_obj, i);
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
