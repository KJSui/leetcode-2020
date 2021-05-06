typedef struct chunk{
    struct chunk * prev;
    struct chunk * next;
    int flag;
    int size;
    char * block;
} chk;
typedef struct ChunkArray{
    chk memory[SIZE];
} chk_arr;

void init_chunkarray(char * mem, int total_size){
    chk_arr *pool;
    int i = 0;
    int block_size = 0;
    int block_byte_num = 0;
    int SIZE = 10;
    block_size = total_size/SIZE;
    block_byte_num = block_size/sizeof(char);
    for(int i = 0; i < SIZE; i++){
        pool->memory[i]->block = mem + i* block_byte_num;
        pool->memory[i]->size = block_byte_num;
        pool->memory[i]->flag = 0;
        if(i == 0)
            pool->memory[i]->prev = NULL;
        else if(i == SIZE-1){
            pool->memory[i-1]->next = pool->memory[i];
            pool->memory[i]->prev = pool->memory[i-1];
            pool->memory[i]->next = NULL;
        } else {
            pool->memory[i-1]->next = pool->memory[i];
            pool->memory[i]->prev = pool->memory[i-1]; 
        }
    }
    return;
}

void write(void * dest){
    memcpy()
}

void read(){

}

void check(){

}

void reset(){
    
}