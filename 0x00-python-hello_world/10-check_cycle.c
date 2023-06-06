#include "lists.h"

/**
 * check_cycle - a function that checks if a singly linked list has a cycle
 * @list: a parameter
 * Return: 0
 */

int check_cycle(listint_t *list)
{
	listint_t *s_once;
	listint_t *s_twice;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	s_once = list;
	s_twice = list->next;
	while (s_twice != NULL && s_twice->next != NULL)
	{
		if (s_once == s_twice)
		{
			return (1);
		}
		s_once = s_once->next;
		s_twice = s_twice->next->next;
	}
	return (0);
}
