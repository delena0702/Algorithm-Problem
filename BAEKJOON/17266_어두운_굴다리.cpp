#include <iostream>

using namespace std;

int N, M;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N >> M;

    int n, b, answer;
    cin >> n;
    answer = n;
    b = n;
    
    for (int i=1;i<M; i++) {
        cin >> n;
        answer = max(answer, (n - b + 1)/2);
        b = n;
    }
    answer = max(answer, N - b);

    cout << answer;

    return 0;
}