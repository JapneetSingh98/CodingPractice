//
//  addNodeToHead.cpp
//  
//
//  Created by Japneet Singh on 11/29/20.
//

#include <stdio.h>

SinglyLinkedListNode* insertNodeAtHead(SinglyLinkedListNode* llist, int data) {
    SinglyLinkedListNode *head = new SinglyLinkedListNode(data);
    head->next = llist;
    return head;
}
