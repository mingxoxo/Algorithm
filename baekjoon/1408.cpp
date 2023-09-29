// 24
// https://www.acmicpc.net/problem/1408

#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    std::string input;
    int hh, mm, ss;
    int start, now;
    char colon;
    
    {
        cin >> input;
        stringstream s(input);
    
        s >> hh >> colon >> mm >> colon >> ss;
        start = hh * 3600 + mm * 60 + ss;
    }
    {
        cin >> input;
        stringstream s(input);
        
        s >> hh >> colon >> mm >> colon >> ss;
        now = hh * 3600 + mm * 60 + ss;
    }
    
    int result = start < now ? now - start : 24 * 3600 - (start - now);
    
    cout << setfill('0'); 
    cout << setw(2) << result / 3600 << ":"
         << setw(2) << result % 3600 / 60 << ":"
         << setw(2) << result % 3600 % 60 << std::endl;
    
    return 0;   
}
