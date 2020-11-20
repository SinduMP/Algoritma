#include <stdio.h>
#include <math.h>

main ()
{
    int a,b,c,d,e,lmbcr,diskon,bayar1,bayar2;
    printf("Hari: (1:senin,2:selasa,3:rabu,4:kamis,5:jumat,6:sabtu,7:minggu)");
    printf("\n");
    printf("jam : 0-23");
    printf("\n");
    printf("menit/detik : 0-60");
    printf("\n");
    printf("hari=:");
    scanf("%d",&a);
    printf("jam mulai telepon=:");
    scanf("%d",&b);
    printf("berapa jam menelepon=:");
    scanf("%d",&c);
    printf("berapa menit menelepon=:");
    scanf("%d",&d);
    printf("berapa detik menelepon=:");
    scanf("%d",&e);
    lmbcr=(c*3600)+(d*60)+e;
    diskon=0.3*(((lmbcr)/(20))*200);
    bayar1=(((lmbcr)/(20))*200)- (diskon);
    bayar2=(((lmbcr)/(20))*200);

if ( a ==7 || b >= 22 || b <= 7 ) {
        printf("Lama bicara(detik) : %i",lmbcr);
        printf("\n");
        printf("Biaya = tiap 20 detik Rp200");
        printf("\n");
        printf("Diskon =Rp %d",diskon);
        printf("\n");
        printf("Maka Biaya yg harus dibayarkan :Rp %d",bayar1);
}
else {
        printf("Lama bicara(detik) : %i",lmbcr);
        printf("\n");
        printf("Biaya = tiap 20 detik Rp200");
        printf("\n");
        printf("Maka Biaya yg harus dibayarkan :Rp %d",bayar2);
}
}
