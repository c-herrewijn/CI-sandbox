#include <iostream>

void trigger_segfault(void) {
    int* ptr = nullptr;
    *ptr = 42;  // Runtime segfault: Writing to null memory
}

int main() {
    trigger_segfault();
}
