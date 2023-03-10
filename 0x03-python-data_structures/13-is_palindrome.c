#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head of list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    int len = 0, i, j;
    int arr[10000];
    listint_t *current = *head;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (current != NULL)
    {
        arr[len++] = current->n;
        current = current->next;
    }

    for (i = 0, j = len - 1; i < j; i++, j--)
    {
        if (arr[i] != arr[j])
            return (0);
    }

    return (1);
}

