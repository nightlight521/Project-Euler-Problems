#include <iostream>

int main() {
	int previous, current, sum, next;
	previous = 1;
	current = 2;
	while (current <= 4000000) {
		if (current % 2 == 0) {
			sum = sum + current;
		}	
		next = current + previous;
		previous = current;
		current = next;
	}
	std::cout << sum << "\n";
}
