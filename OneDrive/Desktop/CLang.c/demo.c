#include <stdio.h>

int main() {
    // Define an array with 5 elements
    int arr[] = {1, 2, 3, 4, 5};
    int length = sizeof(arr) / sizeof(arr[0]); // Calculate the number of elements in the array

    // Print each element of the array
    for(int i = 0; i < length; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
