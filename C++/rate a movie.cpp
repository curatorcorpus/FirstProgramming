#include <iostream>
using namespace std;

string Movie_rating(string title, string rate)
{
	cout << endl;
	cout << title << endl << rate; 
}

int main()
{
	string title;
	string rate;
	cout << "Enter A Title Of A Movie: ";
	getline(cin, title);
	cout << "Rate your movie out of 5: ";
	getline(cin, rate);
	cout << Movie_rating(title, rate);
	return 0;
}
