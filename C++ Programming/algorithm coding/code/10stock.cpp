#include <iostream>
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    int count, prev, curr;
    int cnt = 0;
    bool flag = false;
    cin >> count;

    for (int j=0; j<count; j++) {
      cin >> curr;

      if (j==0) {
        prev = curr;
        continue;
      }

      if (flag == true) {
        if (prev > curr) {
          cnt++;
          flag = false;
        }
      } else {
        if (curr > prev) {
          flag = true;
        }
      }

      prev = curr;
    }

    cout << cnt << endl;
  }

  return 0;
}
