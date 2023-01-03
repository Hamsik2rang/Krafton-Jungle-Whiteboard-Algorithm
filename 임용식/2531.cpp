#include<iostream>
#include<vector>
#include<memory.h>
#include<algorithm>
using namespace std;

#define MAXN 300001
#define MAXD 3001

int N, d, k, c;
int flag, coupon, cnt, maxi = 0;
int sushi[MAXN];
int check[MAXD];
vector<int> eat;

int main()
{
	// N:���ü� d:�ʹ������� k:�������� C:������ȣ
	cin >> N >> d >> k >> c;

	for (int i = 0; i < N; i++)
	{
		cin >> sushi[i];
	}

	// �����̵� ������
	for (int i = 0; i < N; i++)
	{
		flag = false;
		coupon = true;
		for (int j = i; j < i + k; j++)
		{
			if (check[sushi[j % N]] == 1)
			{
				flag++; // �̹� ���� �ʹ��� ��� �ߺ� �� ǥ��	
			}
			else
			{
				check[sushi[j % N]] = 1; // ó�� �Ծ�� �ʹ��� ��� üũ		
			}

			if (sushi[j % N] == c)
			{
				coupon = 0;
			}
		}

		maxi = max(maxi, k - flag + coupon); //�������� ���� �� �ִ� �ִ����� - �ߺ����� + ��������	
		memset(check, 0, sizeof(check)); // üũ �ʱ�ȭ
	}

	cout << maxi;
}