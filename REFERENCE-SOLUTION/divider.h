#ifndef DIVIDER_H
#define DIVIDER_H

template <typename T>
class Divider {
  public:
  T GetQuotient(T, T);
};

template <typename T>
T Divider<T>::GetQuotient(T num, T den) {
  return (num / den);
}

#endif
