#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: Pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int i = 0;
	int length = 0;
	int *list = NULL;
	listint_t *current = *head;

	if (head == NULL || *head == NULL)
	return (1);

	while (current)
	{
		current = current->next;
		length++;
	}
	list = malloc(sizeof(int) * length);
	current = *head;
	while (current)
	{
		list[i++] = current->n;
		current = current->next;
	}
	i = 0;
	while (i < (length / 2))
	{
		if (list[i] != list[length - 1 - i])
		return (0);
		i++;
	}
	return (1);
}
