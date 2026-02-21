#include <stdio.h>

int main()
{
    int choice, quantity;
    float total = 0;

    do
    {
        printf("\n===== SHOPPING CART =====\n");
        printf("1. Soap - Rs 30\n");
        printf("2. Perfume - Rs 80\n");
        printf("3. Shampoo - Rs 50\n");
        printf("4. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        if(choice >= 1 && choice <= 3)
        {
            printf("Enter quantity: ");
            scanf("%d", &quantity);

            if(choice == 1)
                total += quantity * 30;
            else if(choice == 2)
                total += quantity * 20;
            else if(choice == 3)
                total += quantity * 50;
        }

    } while(choice != 4);

    printf("\nTotal Amount = Rs %.2f\n", total);
    printf("Thank You!\n");

    return 0;
}
