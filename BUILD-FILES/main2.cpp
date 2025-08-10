#include "divider.h"

#include <iostream>

int main() {
  Divider<int>* division = new Divider<int>();

  std::cout << division->GetQuotient(-20, 3) << std::endl;

}