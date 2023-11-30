#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to be inserted.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *currentNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}

	currentNode = *head;
	while (currentNode->next != NULL && currentNode->next->n < number)
		currentNode = currentNode->next;

	newNode->next = currentNode->next;
	currentNode->next = newNode;

	return (newNode);
}
