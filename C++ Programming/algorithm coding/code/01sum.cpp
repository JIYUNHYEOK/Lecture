#include <iostream>
using namespace std;

int main() {

  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    int sum = 0;
    int count;
    cin >> count;

    for (int j=0; j<count; j++) {
      int num;
      cin >> num;
      sum += num;
    }

    cout << sum << endl;
  }

  return 0;
}
