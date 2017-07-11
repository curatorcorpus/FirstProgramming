#include <iostream>
using namespace std;

extern int a, b;
extern int c;
extern float f;

int main()
{	
// Variable Definition
	int a, b;
	int c;
	float f;
	// Actual Initialization
	a = 10;
	b = 20;
	c = a + b;
	
	cout << c << endl ;
	
	f = 70.0/3.0;
	cout << f << endl ;
	
	cout << "Manners Maketh Man!" << endl;
	return 0;
}
