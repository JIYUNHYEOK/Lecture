#include <iostream>
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    int n, a, b;
    cin >> n >> a >> b;
    int cnt = 0;  // counter
    int side = n;
    int current = 0; // current value

    for (int j=0; j<side; j++) { // to right
      current++;
      cnt++;

      if (cnt>=a && cnt <=b) {
        cout << current << " ";
      }
    }
      side--;

      while (side > 0) {

        for (int k=0; k<side; k++) { // down
          current += n;
          cnt++;
          if (cnt>=a && cnt<=b) {
            cout << current << " ";
          }
        }

        for (int k=0; k<side; k++) { // left
          current--;
          cnt++;
          if (cnt>=a && cnt<=b) {
            cout << current << " ";
          }
        }
        side--;

        for (int k=0; k<side; k++) { // up
          current -= n;
          cnt++;
          if (cnt>=a && cnt<=b) {
            cout << current << " ";
          }
        }

        for (int k=0; k<side; k++) {
          current++;
          cnt++;
          if (cnt>=a && cnt<=b) {
            cout << current << " ";
          }
        }
        side--;
      }

      cout << endl;
  }

  return 0;
}
