#include <iostream>
#include <iomanip>
#include <string>

const int MAX_NAME_SIZE = 100;

int main() {
	char name[MAX_NAME_SIZE];

	std::cout << "What is your name?";
	std::cin.getline(name, 256, '\n');

	std::cout << "Hello, " << name << "!" << std::endl;
}
