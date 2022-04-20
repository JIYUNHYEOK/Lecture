#include <iostream>
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    unsigned int num, ans;
    cin >> num;

    while (num/10 > 0) {
      ans = 1;
      
      while (num/10 > 0) {
        if (num%10 != 0) {
          ans *= (num%10);
          num /= 10;
        }
        else {
          num /= 10;
        }
      }
      
      ans *= num;
      num = ans;
    }

    cout << num << endl;
  }

  return 0;
}
