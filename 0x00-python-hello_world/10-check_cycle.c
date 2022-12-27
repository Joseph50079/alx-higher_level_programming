#include "lists.h"

/**
 * check_cycle - check if linked list has a cycle in it
 * @list: head pointer of node
 * Return: 0 if there is no cycle else return 1
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *ptr = list;

	if (list == NULL)
		return (0);
	while (temp->next != NULL && ptr->next != NULL)
	{
		if (temp->next == list || temp->next == ptr->next->next)
		{
			return (1);
		}
		else
		{
			temp = temp->next;
			ptr = ptr->next->next;
		}
	}

	return (0);
}
