#include <iostream>
using namespace std;

int main()
{
    int numData;
    int data;
    int sum = 1;

    cin >> numData;
    for(int i = 0; i < numData; i++)
    {
        cin >> data;
        sum = ((sum%100)*(data%100))%100;
    }

    cout << sum << endl;

    return 0;
}

