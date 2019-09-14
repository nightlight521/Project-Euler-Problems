#include <iostream>
#include <vector>

int main() {
	int integer = 3;
	std::vector<int> primes = {2};
	while (primes.size() != 10001) {
		for (int i = 0; i < primes.size(); i++) {
			if (integer % primes[i] == 0) {
				break;
			}
			if (i == primes.size()-1) {
				primes.push_back(integer);
			}
		}
		integer++;
	}
	std::cout << primes[10000];
}
