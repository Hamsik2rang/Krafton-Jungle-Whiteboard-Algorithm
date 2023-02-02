#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>

using namespace std;

struct Info
{
	int in = 0;
	int out = 0;
	int accumulatedTime = 0;
	int fee = 0;
};

int convertTimeToInt(string time)
{
	int hour = stoi(time.substr(0, 2)) * 60;
	int min = stoi(time.substr(3, time.length()));
	int result = hour + min;
	return result;
}

bool convertRecord(string record, int& outTime, int& outCarNum)
{
	istringstream iss(record);
	string time, carNum, status;
	iss >> time >> carNum >> status;
	outTime = convertTimeToInt(time);
	outCarNum = stoi(carNum);

	return status == "IN";
}

void setFee(vector<int>& fees, Info& info)
{
	int accumulatedTime = info.accumulatedTime;
	info.fee += fees[1];
	if (accumulatedTime > fees[0])
	{
		info.fee += (int)ceil(((float)accumulatedTime - fees[0]) / fees[2]) * fees[3];
	}
}

// [0] : 기본 시간
// [1] : 기본 요금
// [2] : 단위 시간(분)
// [3] : 단위 요금(원)
vector<int> solution(vector<int> fees, vector<string> records)
{
	vector<int> answer;
	map<int, Info> infoMap;

	for (const auto& record : records)
	{
		int time, carNum;
		bool isIn;
		isIn = convertRecord(record, time, carNum);
		if (isIn)
		{
			infoMap[carNum].in = time;
		}
		else
		{
			infoMap[carNum].out = time;
			infoMap[carNum].accumulatedTime += infoMap[carNum].out - infoMap[carNum].in;
		}
	}
	for (auto& info : infoMap)
	{
		if (info.second.in >= info.second.out)
		{
			info.second.out = 23 * 60 + 59;
			info.second.accumulatedTime += info.second.out - info.second.in;
		}
		setFee(fees, info.second);
		answer.push_back(info.second.fee);
	}

	return answer;
}