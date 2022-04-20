#include <iostream>
#include <climits>
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    int count;
    cin >> count;

    int max = INT_MIN;
    int min = INT_MAX;
    for (int j=0; j<count; j++) {
      int num;
      cin >> num;

      if (num > max) {
        max = num;
      }
      if (min > num) {
        min = num;
      }
    }
    cout << max << " " << min << endl;
  }

  return 0;
}
