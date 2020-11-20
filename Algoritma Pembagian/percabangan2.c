#include <stdio.h>
#include <math.h>

main ()
{
    int a,b,c,d,e,deskriminan,x1,x2,x;
    printf("bilangan pertama=:");
    scanf("%i",&a);
    printf("bilangan kedua=:");
    scanf("%i",&b);
    printf("bilangan ketiga=:");
    scanf("%i",&c);
    deskriminan=pow(b,2)-(4*a*c);
    printf("Deskriminan : %d",deskriminan);

if (deskriminan == 0){
    printf("\n");
    x=(-b/(2*a));
    printf("Akarnya: ");
    printf("\n");
    printf("x1=x2= %d",x);
}
else if (deskriminan > 0){
    printf("\n");
    printf("\n");
    x1=-b+pow(deskriminan,(1/2))/(2*a);
    printf("\n");
    x2=-b-pow(deskriminan,(1/2))/(2*a);
    printf("\n");
    printf("Akarnya: ");
    printf("\n");
    printf("x1 =%d",x1);
    printf("\n");
    printf("x2 =%d",x2);
}
else {
    printf("\n");
    printf("Akarnya Imajiner");
}}
