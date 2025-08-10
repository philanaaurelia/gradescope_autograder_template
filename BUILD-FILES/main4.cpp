#include "divider.h"
#include <iostream>

int main() {
  Divider<double>* division = new Divider<double>();

  std::cout << division->GetQuotient(6.53513462453421123415, 2.31406341650374081) << std::endl;

  return 0;
}