#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to a pointer to the head of the list.
 * @number: Number to be inserted.
 * Return: Address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_no = malloc(sizeof(listint_t));
	listint_t *current = *head;
	listint_t *pre = NULL;

	if (new_no == NULL)
		return (NULL);

	new_no->n = number;
	new_no->next = NULL;

	if (*head == NULL)
	{
		*head = new_no;
		return (new_no);
	}
	while (current != NULL && current->n < number)
	{
		pre = current;
		current = current->next;
	}
	if (pre == NULL)
	{
		new_no->next = *head;
		*head = new_no;
	}
	else
	{
		pre->next = new_no;
		new_no->next = current;
	}
	return (new_no);
}
