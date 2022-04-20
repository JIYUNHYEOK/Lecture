#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    int num;
    cin >> num;
    int size = num/2;

    for (int x=0; x<num; x++) {
      for (int y=0; y<num; y++) {
        if (max(abs(x-size), abs(y-size)) %2 == 0) {
          cout << "0";
        }
        else {
          cout << "1";
        }
      }
      cout << endl;
    }
  }

  return 0;
}
