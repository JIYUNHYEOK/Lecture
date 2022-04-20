#include <iostream>
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    int num;
    cin >> num;
    int tmp = num;

    unsigned int sum = 0;

    while (num>0) {
      sum += (num%10)*(num%10);
      num /= 10;
    }

    if (tmp == sum) {
      cout << 1 << endl;
    }
    else {
      cout << 0 << endl;
    }
  }

  return 0;
}
