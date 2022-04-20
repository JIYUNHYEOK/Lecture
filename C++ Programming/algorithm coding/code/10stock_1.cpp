#include <iostream>
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    int count, prev, curr;
    int cnt = 0;
    cin >> count;

    bool flag = false;

    for (int j=0; j<count; j++) {

      cin >> curr;

      if (j==0) {
        prev = curr;
        continue;
      }

      if (prev == curr) {
        continue;
      }
      else if (curr > prev) {
        flag = true;
      }
      else if (prev > curr) {
        if (flag == true) {
          cnt++;
        }
        flag = false;
      }
      prev = curr;
    }

    cout << cnt << endl;
  }

  return 0;
}
