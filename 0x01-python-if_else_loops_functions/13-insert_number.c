#include "lists.h"


/**
 * insert_sorted - inserts into sorted list where first node is skipped
 * @head: pointer to first node
 * @new: new node to insert
 * @number: integer to insert to list
 * Return: new node (success), NULL (fail)
 */
listint_t *insert_sorted(listint_t **head, listint_t *new, int number)
{
	listint_t *traverse = NULL, *temp = NULL;
	int i;

	temp = *head;
	traverse = temp->next;
	for (i = 0; traverse != NULL; i++)
	{
		if (traverse->n > number)
		{
			new->n = number;
			new->next = traverse;
			temp->next = new;
			return (new);
		}
		else if (traverse->next == NULL)
		{
			new->n = number;
			new->next = NULL;
			traverse->next = new;
			return (new);
		}
		traverse = traverse->next;
		temp = temp->next;
	}
	free(new);
	return (NULL);
}


/**
 * insert_node - adds a nude to a sorted singly linked list
 * @head: pointer to first node of list
 * @number: value to insert into into new node
 * Return: new node (success), NULL (fail)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *temp = NULL;

	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	if (head == NULL)
	{
		new_node->n = number;
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	temp = *head;
	if (temp->n > number)
	{
		new_node->n = number;
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}
	insert_sorted(head, new_node, number);
	return (new_node);
}
