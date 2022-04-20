#include <iostream>
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    int count;
    cin >> count;

    int min, max;

    for (int j=0; j<count; j++) {
      int num;
      cin >> num;

      if (j==0) {
        min, max = num;
      }

      min = min>num ? num : min;
      max = num>max ? num : max;
    }
    cout << max << " " << min << endl;
  }

  return 0;
}
