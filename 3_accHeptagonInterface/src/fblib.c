#include "fblib.h"


void Fblib__blocked_step( Fblib__blocked_out *out , Fblib__blocked_mem* self)
{
    out->o=is_front_blocked();
}
