#include <iostream>
using namespace std;

int main(){
  int times;
  cin >> times;
  
  for (int i=0; i<times; i++) {
    int a,b,c;
    cin >> a >> b >> c;

    if (a<=b) {
      if (b<=c) {
        cout << a << " " << b << " " << c << endl;
      }
      else if (a<=c) {
        cout << a << " " << c << " " << b << endl;
      }
      else {
        cout << c << " " << a << " " << b << endl;
      }
    }
    else {
      if (c<=b) {
        cout << c << " " << a << " " << b << endl;
      }
      else if (a<=c) {
        cout << b << " " << a << " " << c << endl;
      }
      else {
        cout << b << " " << c << " " << a << endl;
      }
    }
  }

  return 0;
}
