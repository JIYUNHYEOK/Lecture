#include <iostream>
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    int num;
    cin >> num;
    int size = num/2;

    for (int y=size; y>=-size; y--) {
      for (int x=-size; x<=size; x++) {
        if (abs(y)==size) {
          if (abs(x)==size || x==0) {
            cout << '+';
          } else {
            cout << '-';
          }
        } else if (y==0) {
          if (abs(x)==size) {
            cout << '+';
          } else if (x==0) {
            cout << '*';
          } else {
            cout << '-';
          }
        } else {
          if (abs(x)==size || x==0) {
            cout << '|';
          } else if (abs(x) == abs(y)) {
            if (x*y>0) {
              cout << '/';
            } else {
              cout << '\\';
            }
          } else {
            cout << '.';
          }
        }
      }
      cout << endl;
    }
  }

  return 0;
}
