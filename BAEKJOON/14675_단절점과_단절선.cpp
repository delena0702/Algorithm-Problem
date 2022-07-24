#include <iostream>

using namespace std;

int arr[100001];
int N, Q;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 0; i < N - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        arr[a]++;
        arr[b]++;
    }

    cin >> Q;
    for (int i = 0; i < Q; i++)
    {
        int t, k;
        cin >> t >> k;
        if (t == 1 && arr[k] == 1)
            cout << "no\n";
        else
            cout << "yes\n";
    }

    return 0;
}