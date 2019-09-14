#include <iostream>
#include <vector>

int main() {
        int integer = 3;
       	long long sum_of_primes = 2;
        std::vector<int> primes = {2};
        while (integer < 2000000) {
                for (int i = 0; i < primes.size(); i++) {
                        if (integer % primes[i] == 0) {
                                break;
                        }
                        if (i == primes.size()-1) {
                                sum_of_primes += integer;
				primes.push_back(integer);
                        }
                }
                integer++;
        }
        std::cout << sum_of_primes;
}

