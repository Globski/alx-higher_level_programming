#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slowCycle, *fastCycle;

	if (list == NULL || list->next == NULL)
		return (0);

	slowCycle  = list;
	fastCycle = list->next;

	while (fastCycle != NULL && fastCycle->next != NULL)
	{
		if (slowCycle == fastCycle)
			return (1);

		slowCycle = slowCycle->next;
		fastCycle = fastCycle->next->next;
	}

	return (0);
}

