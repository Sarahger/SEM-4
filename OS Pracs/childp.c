#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>

void main()
{
    //pid_t p = fork();
    int p;
    p = fork();
    if (p>0)
    {
        printf("Parent Process ID : %d\n",getpid());
        printf("Chile Process ID : %d\n",getppid());
    }
}