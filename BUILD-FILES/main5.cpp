#include "divider.h"
#include <iostream>

int main() {
  Divider<float>* division = new Divider<float>();

  std::cout << division->GetQuotient(0, 248348923) << std::endl;

  return 0;
}