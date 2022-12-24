#include "lists.h"

/**
 * check_cycle - check if linked list has a cycle in it
 * @list: head pointer of node
 * Return: 0 if there is no cycle else return 1
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp != NULL)
	{
		if (temp->next == list)
		{
			return (1);
		}
		else
			temp = temp->next;
	}

	return (0);
}
