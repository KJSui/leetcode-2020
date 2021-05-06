#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct ringbuf_s {
    uint8_t * buff;
    uint8_t  head, tail;
    size_t size;
} ringbuf_t;

int init_ringbuf(ringbuf_t *rb, size_t capacity){
    rb = calloc(capacity, sizeof(ringbuf_t));
    if(rb){
        rb->size = capacity;
        rb->buf = rbuff;
        rb->head = rb->tail = rbuff;
        rb->curr_sz = 0;
    } else {
        return -1;
    }
    return 0;
}


bool ringbuf_is_full(ringbuf_t *rb){
    if(rb->curr_sz == rb->capacity)
        return true;
    return false;
}

bool ringbuf_is_empty(ringbuf_t *rb){
    if(rb->curr_sz == 0){
        return true;
    }
    return false;
}



bool insert(ringbuf_t *rb, int* val){
    int next;
    next = rb->head + 1;
    rb->tail ++;
    rb->curr_sz ++;
    if(rb->tail == NULL){
        rb->tail = rb->buf;
    }
    return true
}

int deque(ringbuf_t *rb, uint8_t * val){
    int next;
    if (rb->head == rb->tail)
        return -1;
    
    next = rb->head + 1;

    if(next >= rb->size)
        next = 0;

    *val = rb->buff[rb->head];
    rb->head = next;
    return 0;
}


int cir_buff_pop(ringbuf_t )


