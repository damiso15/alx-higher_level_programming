#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: 0 as Success
 */
int check_cycle(listint_t *list)
{
    listint_t *slow, *fast;

    if (!list)
        return (0);

    slow = list;
    fast = list->next;

    while (slow && fast && fast->next)
    {
        if (slow == fast)
            return (1);

        slow = slow->next;
        fast = fast->next->next;
    }

    return (0);
}

