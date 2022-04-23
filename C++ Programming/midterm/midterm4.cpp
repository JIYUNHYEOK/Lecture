#include <iostream>
using namespace std;
const int SET_SIZE = 101;

int countElementOfUnion(int setA[], int setB[], int sizeA, int sizeB)
{
    int count = sizeB; // 집합 setA, setB의 합집합의 원소의 개수
    int ans[SET_SIZE];

    for(int i=0; i<sizeB; i++) ans[i] = setB[i];

    for (int i=0; i<sizeA; i++) {
        for (int j=0; j<sizeB; j++) {
            if (setA[i] == setB[j]) {
                break;
            }
            if (j == sizeB-1) {
                ans[count++] = setA[i];
            }
        }
    }

    return count;
}

int main()
{
    int setA[SET_SIZE], setB[SET_SIZE];  // 집합 A, B의 원소를 저장하는 배열
    int sizeA, sizeB;           // 집합 A, B에 속하는 원소의 개수

    cin >> sizeA;
    for(int i =0; i<sizeA; i++)
        cin >> setA[i];
    cin >> sizeB;
    for(int i =0; i<sizeB; i++)
        cin >> setB[i];

    cout << countElementOfUnion(setA, setB, sizeA, sizeB) << endl;

    return 0;
}
