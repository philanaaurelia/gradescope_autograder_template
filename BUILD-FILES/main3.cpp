#include "divider.h"
#include <iostream>

int main() {
  Divider<float>* division = new Divider<float>();

  std::cout << division->GetQuotient(6.53513462453421123415, 2.31406341650374081) << std::endl;

  return 0;
}