#include "lists.h"
#include <stdio.h>
#include <stdlib.h>



/**
 * is_palindrome - checks if singly linked list is palindrome
 * @head: pointer to first node
 * Return: 0 is not palindrome, 1 is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i, j, len = 1, *values = NULL;
	listint_t *end, *start;

	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	end = *head;
	start = *head;
	for (i = 0; end->next != NULL; i++)
	{
		end = end->next;
		len += 1;
	}
	values = (int *)malloc(len * sizeof(int));
	for (i = 0; i < len; i++)
	{
		values[i] = start->n;
		start = start->next;
	}
	for (i = 0, j = len - 1; i < (len / 2); j--, i++)
	{
		if (values[i] != values[j])
		{
			return (0);
		}
	}

	free(values);
	return (1);
}
