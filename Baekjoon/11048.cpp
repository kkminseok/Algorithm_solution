#include<iostream>
#include<algorithm>
using namespace std;

int arr[1001][1001];
int dp[1001][1001];	

void Solve()
{
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			cin >> arr[i][j];
			if (i == 0 && j == 0)
				dp[0][0] = arr[0][0];
			if (i == 0 && j != 0)
				dp[i][j] = dp[i][j - 1] + arr[i][j];
			if (j == 0 && i != 0)
				dp[i][j] = dp[i - 1][j] + arr[i][j];
		}
	}
	for (int i = 1; i < n; ++i)
	{
		for (int j = 1; j < m; ++j)
		{
			dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + arr[i][j];
		}
	}
	cout << dp[n-1][m-1];
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	Solve();
	return 0;
}