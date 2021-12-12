// 在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

#include <iostream>

using namespace std;

int walkSearch(int arr[][4], int N, int target) 
{
    int i = 0;
    int j = 3;
    while (i<N && j>=0) {
        if (arr[i][j] == target) {
            cout << i << ',' << j << endl;

            return 0;
        }
        if (arr[i][j] < target) {
            i++;
        } else {
            j--;
        }
    }
    cout << "-1" << endl;
    return -1;
}


int main()
{
    int arry[4][4]= {{ 1,5,7,9 },{ 4,6,10,15 },{ 8,11,12,19 },{ 14,16,18,21 }};
    walkSearch(arry, 4, 15);
    // yangSearch(arry, 4, 15, 0, 3);
    return 0;
}