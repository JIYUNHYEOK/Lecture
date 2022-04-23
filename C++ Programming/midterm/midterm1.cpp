#include <iostream>
using namespace std;

int main()
{
    int a, b, c;
    int median;         // 중간값
    
    cin >> a >> b >> c;

    median = (a<=b) ? ((b<=c) ? b : ((a<=c) ? c : a)) : ((c<=b) ? b : ((a<=c) ? a : c));

    // if (a<=b) {
    //     if (b<=c) {
    //         median = b;
    //     } else {
    //         if (a<=c) {
    //             median = c;
    //         } else {
    //             median = a;
    //         }
    //     }
    // } else {
    //     if (c<=b) {
    //         median = b;
    //     } else {
    //         if (a<=c) {
    //             median = a;
    //         } else {
    //             median = c;
    //         }
    //     }
    // }

    cout << median << endl;

    return 0;
}
