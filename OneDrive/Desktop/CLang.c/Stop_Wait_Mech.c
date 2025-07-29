#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Define frame and ACK
#define FRAME_SIZE 1  
#define ACK_SIZE 1 

// Probability of losing a frame or an ACK (simulating a noisy channel)
#define LOSS_PROBABILITY 0.1

// Function prototypes
int send_frame(int frame);
int receive_ack();
int simulate_error();

int main() {
    int frame = 0;
    int ack;
    srand(time(NULL));

    for (int i = 0; i < 10; i++) { // Simulate sending 10 frames
        printf("Sending frame: %d\n", frame);
        while (!send_frame(frame)) {
            printf("Frame %d lost. Retransmitting...\n", frame);
        }

        while ((ack = receive_ack()) != frame) {
            printf("ACK lost or corrupted. Waiting for ACK for frame %d...\n", frame);
        }

        printf("Received ACK for frame: %d\n", frame);
        frame = (frame + 1) % 2; // Switch between 0 and 1 for next frame
    }

    return 0;
}

// Simulate sending a frame. Returns 1 if successful, 0 if frame is lost.
int send_frame(int frame) {
    printf("Frame %d sent.\n", frame);
    return !simulate_error();
}

// Simulate receiving an ACK. Returns the frame number or -1 if ACK is lost.
int receive_ack() {
    if (simulate_error()) {
        printf("ACK lost or corrupted.\n");
        return -1;
    }
    int ack = rand() % 2; // Simulate correct ACK reception
    printf("ACK %d received.\n", ack);
    return ack;
}

// Simulate a channel error. Returns 1 if error occurs, 0 otherwise.
int simulate_error() {
    return ((float)rand() / RAND_MAX) < LOSS_PROBABILITY;
}
