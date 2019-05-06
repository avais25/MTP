

typedef struct Fblib__blocked_out {
  int o;
} Fblib__blocked_out;

typedef struct Fblib__blocked_mem {
  int i;
} Fblib__blocked_mem;



void Fblib__blocked_step(Fblib__blocked_out *o, Fblib__blocked_mem* self);
