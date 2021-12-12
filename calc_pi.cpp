#include <iostream>

using namespace std;

int main()
{
    double x = 0.0;
    double y = 0.0;
    double cnt = 0.0;
    int N = 100000;
    for(int i=0; i<N; i++) {
        x = 1.0 - 2.0 * random()/RAND_MAX;
        y = 1.0 - 2.0 * random()/RAND_MAX;
        if(x*x + y*y < 1) {
            cnt += 1.0;
        }
    }
    cout << 4.0*cnt / N << endl;
    return 0;
}