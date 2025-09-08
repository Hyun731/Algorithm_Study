#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node *next;
} Node;

typedef struct list{
    struct node *head;
    struct node *tail;
} List;

void initList(List *list){
    list->head = NULL;
    list->tail = NULL;
}

void append(List *list, int data) {
    Node *newNode = malloc(sizeof(Node));
    if (newNode == NULL){
        printf("메모리 할당 실패\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    if (list->head == NULL) {list->head = newNode; list->tail = newNode;}
    else {list->tail->next = newNode; list->tail = newNode;}

}

void freeList(List *list) {
    Node *cur = list->head;
    Node *temp;
    while (cur != NULL) {
        temp = cur;
        cur = cur->next;
        free(temp);
    }
    initList(list);
}

void printList(const List *list) {
    Node *cur = list->head;
    while (cur != NULL) {
        printf("%d -> ", cur->data);
        cur = cur->next;
    }
    printf("NULL\n");
}

int main(){
}
