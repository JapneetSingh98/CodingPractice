//
//  printLinkedList.cpp
//  
//
//  Created by Japneet Singh on 11/25/20.
//

#include <stdio.h>

void printLinkedList(SinglyLinkedListNode* head) {
    cout << head->data << endl;
    SinglyLinkedListNode *nextNode = head->next;
    if (nextNode != NULL) {
        printLinkedList(nextNode);
    }
    return;
}
