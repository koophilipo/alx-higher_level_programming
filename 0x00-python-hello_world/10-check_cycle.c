#include "lists.h"

/**
 * check_cycle - varifies the exitence of cycle in list
 * @ptr: head of list
 *
 * Return: 1 cycle exits (success), 0 no cycle (fail)
 */
int check_cycle(listint_t *ptr)
{
	listint_t *check_traverse = ptr;
	listint_t *traverse = ptr;

	if (ptr == NULL)
	{
		return (0);
	}

	while (check_traverse && traverse && (traverse->next))
	{
		if (check_traverse->next == traverse->next->next)
		{
			return (1);
		}
		traverse = traverse->next->next;
		check_traverse = check_traverse->next;
	}
	return (0);
}
