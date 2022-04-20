#include <iostream>
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    int count, num;
    cin >> count;

    long sum = 1;

    for (int j=0; j<count; j++) {
      cin >> num;
      sum = ((sum%10)*(num%10))%10;
    }
    cout << sum << endl;
  }

  return 0;
}