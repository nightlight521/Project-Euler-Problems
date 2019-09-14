#include <iostream>

int main() {
	int squared_sum, sum_squared, sum;
	for (int i = 1; i <= 100; i++) {
		squared_sum += i*i;
		sum += i;
	}
	sum_squared = sum*sum;
	std::cout << sum_squared - squared_sum << "\n";
}
