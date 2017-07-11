#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	char str[80];
	strcpy(str,"there ");
	strcat(str,"string ");
	strcat(str,"are ");
	strcat(str,"concatenated.");
	puts(str);
}
