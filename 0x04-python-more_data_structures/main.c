#include <stdio.h> 
#include <stdlib.h>
#include <math.h>
int main (void) {

int sizeA , sizeB ;

printf("enter the size of the array A : ") ;
scanf("%d",&sizeA) ;
printf("enter the size of the array B : ") ;
scanf("%d",&sizeB) ;
int a [sizeA + sizeB] ,  b [sizeB] ;
int *pA ;
int *pB ;
pA = a ;
pB = b ;
 
for(pA = a ; pA <a+ sizeA ; pA++) {
    printf("A [%d] = ",pA - a+1) ;
    scanf("%d",pA) ;
}

for(pB = b ; pB <b+ sizeB ; pB++) {
    printf("B [%d] = ",pB - b+1) ;
    scanf("%d",pB) ;
}

for(pA = a +  sizeB ,pB = b ; pA < a + sizeA * 2 ; pA++ ,pB++) {
    *pA = *pB ;
}

for(pA = a ; pA < a +  sizeA * 2 ; pA++ ) {
    printf("%d ",*(pA)) ;
}
return 0 ;

}
