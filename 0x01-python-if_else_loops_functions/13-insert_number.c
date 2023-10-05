#include "lists.h"


/**
 * insert_node - insert to sorted nodes
 * @head: pointer to the head
 * @number: n
 * Return: new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;
	listint_t *fast, *temp;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
	{
		return (NULL);
	}
	temp->n = number;

	if (*head == NULL)
	{
		*head = temp;
		return (temp);
	}
	ptr = *head;
	if (ptr != NULL)
	{
		if (ptr->n > temp->n)
		{
			temp->next = ptr;
			ptr = temp;
			
			return (temp);
		}
		fast = ptr;
		while (fast->next != NULL && fast->next->n < temp->n)
		{
			fast = fast->next;
		}

		temp->next = fast->next;
		fast->next = temp;
	}
	else
		return (NULL);

	return (temp);
}
