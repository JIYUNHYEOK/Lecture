#include <iostream>
#define max(a,b) ((a>=b) ? a : b)
#define min(a,b) ((a<=b) ? a : b)
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    int a, b, c, d;
    int max, min;
    cin >> a >> b >> c >> d;

    if (c>=b || a>=d) {
      max = (b-a) + (d-c);
      min = 0;
    } else {
      min = min(b,d) - max(a,c);
      max = max(b,d) - min(a,c);
    }
    cout << min << " " << max << endl;
  }

  return 0;
}
