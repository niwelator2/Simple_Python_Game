#include <iostream>

// Funkcja obliczająca n-ty element ciągu Fibonacciego iteracyjnie
unsigned long long fibonacci(int n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        unsigned long long fib1 = 0;
        unsigned long long fib2 = 1;
        unsigned long long fibn = 0;
        
        for (int i = 2; i <= n; ++i) {
            fibn = fib1 + fib2;
            fib1 = fib2;
            fib2 = fibn;
        }
        
        return fibn;
    }
}

int main() {
    int n;
    std::cout << "Podaj n: ";
    std::cin >> n;

    if (n < 0) {
        std::cout << "Ciąg Fibonacciego jest zdefiniowany tylko dla liczb nieujemnych." << std::endl;
    } else {
        unsigned long long wynik = fibonacci(n);
        std::cout << "F(" << n << ") = " << wynik << std::endl;
    }

    return 0;
}
