#include <iostream>

int main(){
	int acc1, acc2;
	for (int i = 1; i < 1000; i++) {
		if (i % 3 == 0 && i % 5 != 0) {
			acc1 = acc1 + i;
	
		}
		else if (i % 5 == 0) {
			acc2 = acc2 + i;
		}
	}
	std::cout << acc1 + acc2, "\n";
}
