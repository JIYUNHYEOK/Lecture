#include <iostream>
using namespace std;

int main() {
  int times;
  cin >> times;

  for (int i=0; i<times; i++) {
    int ax1, ay1, ax2, ay2, bx1, by1, bx2, by2;
    int sizeax, sizeay, sizebx, sizeby, intersectx, intersecty;
    int area, length;
    cin >> ax1 >> ay1 >> ax2 >> ay2;
    cin >> bx1 >> by1 >> bx2 >> by2;

    sizeax = ax2 - ax1;
    sizeay = ay2 - ay1;
    sizebx = bx2 - bx1;
    sizeby = by2 - by1;

    intersectx = min(ax2, bx2) - max(ax1, bx1);
    intersecty = min(ay2, by2) - max(ay1, by1);

    if (intersectx >=0 && intersecty >=0) {
      area = sizeax*sizeay + sizebx*sizeby - intersectx*intersecty;
      length = 2*(sizeax+sizeay+sizebx+sizeby-intersectx-intersecty);
    } else {
      area = sizeax*sizeay + sizebx*sizeby;
      length = 2*(sizeax+sizeay+sizebx+sizeby);
    }

    cout << area << " " << length << endl;
  }


  return 0;
}
