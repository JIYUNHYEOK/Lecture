#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    float hour, minute;
    cin >> hour >> minute;

    int h = (360/12)*hour + (360/12)*((float)minute/60);
    int m = (360/60)*minute;

    int angle = abs(h-m);

    if (angle > 180) {
      angle = (360-angle);
    }

    cout << angle << endl;
  }

  return 0;
}