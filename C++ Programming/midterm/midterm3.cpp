#include <iostream>
#include <cmath>
using namespace std;

void printDiamond(int size)

{
    int radius = size/2;
    int condition = (size+1)/2;

    for (int y = radius; y>=-radius; y--) {
        for (int x = -radius; x<=radius; x++) {
            if (abs(x) + abs(y) >= condition) {
                cout << '*';
            }
            else {
                cout << '+';
            }
        }
        cout << endl;
    }
    
}

int main()
{
    int size;
    cin >> size;
    printDiamond(size);
    return 0;
}
