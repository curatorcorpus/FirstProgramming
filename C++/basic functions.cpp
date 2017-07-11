#include <iostream>
using namespace std;

bool true_or_false(string str)
{
	if(str == "10")
	{
		return true;
	}
	else
	{
		return false;
	}
}

int main()
{
	string str = "";
	string result;
	cout << "Enter Value: ";
	cin >> str;
	cout << true_or_false(str);
}
