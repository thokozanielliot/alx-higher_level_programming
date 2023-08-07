#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: singly linked list
 *
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *sl = list;
	listint_t *fs = list;

	if (!list)
		return (0);

	while (sl && fs && fs->next)
	{
		sl = sl->next;
		fs = fs->next->next;
		if (sl == fs)
			return (1);
	}
	return (0);
}
