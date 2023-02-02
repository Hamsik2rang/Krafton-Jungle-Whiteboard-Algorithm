#include <string>
#include <vector>
#include <sstream>

using namespace std;

bool IsPrime(long long x)
{
    if (x == 1)
    {
        return false;
    }
    for (long long i = 2; i * i <= x; i++)
    {
        if (x % i == 0)
        {
            return false;
        }
    }
    return true;
}

int solution(int n, int k)
{
    int answer = 0;
    string converted = "";

    while (n)
    {
        converted = (char)(n % k + '0') + converted;
        n /= k;
    }
    stringstream ss(converted);
    string temp;
    vector<string> buffer;
    while (getline(ss, temp, '0'))
    {
        if (temp == "")
        {
            continue;
        }
        buffer.push_back(temp);
    }

    for (const auto& e : buffer)
    {
        if (IsPrime(stoll(e)))
        {
            answer++;
        }
    }

    return answer;
}
