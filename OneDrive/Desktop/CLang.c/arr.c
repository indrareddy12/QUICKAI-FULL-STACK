#include <stdio.h>


int main() {
    int n, i;

    // Asking the user for the number of elements in the array
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int array[n];

    // Taking input for each element of the array
    printf("Enter %d elements:\n", n);
    for (i = 0; i < n; i++) {
        printf("Element %d: ", i + 1);
        scanf("%d", &array[i]);
    }

    // Printing the array elements
    printf("The elements of the array are:\n");
    for (i = 0; i < n; i++) {
        printf("%d ", array[i]);
    }

    return 0;
}
