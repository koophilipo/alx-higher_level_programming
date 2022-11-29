#include "lists.h"

/**
 * check_cycle - varifies the exitence of cycle in list
 * @ptr: head of list
 *
 * Return: 1 cycle exits (success), 0 no cycle (fail)
 */
int check_cycle(char *ptr)
{
	listint_t *head = ptr;
	listint_t *traverse = ptr;

	if (ptr == NULL)
	{
		return (0);
	}

	while ((traverse->next) != NULL)
	{
		if (head == (traverse->next))
		{
			return (1);
		}
		traverse = traverse->next;
	}
	return (0);
}
