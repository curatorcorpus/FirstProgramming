#include <iostream>
using namespace std;

bool prime(int&x)
{
    if (x%2==1)
        return true;
    else
        return false;
}

int main()
{
    for (int i = 0; i < 100; i++)
        if ( prime(i) )
            cout << i << endl;

    return 0;
}
