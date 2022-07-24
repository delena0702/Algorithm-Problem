#include <iostream>
#define LIMIT 200

using namespace std;

char input[LIMIT + 1];

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> input;

    int cnt[4] = {1, 0, 0, 2};
    int temp;
    for (int i = 0; i < LIMIT && input[i] != '\0'; i++)
    {
        switch (input[i]) {
        case 'A': swap(cnt[0], cnt[1]); break;
        case 'B': swap(cnt[0], cnt[2]); break;
        case 'C': swap(cnt[0], cnt[3]); break;
        case 'D': swap(cnt[1], cnt[2]); break;
        case 'E': swap(cnt[1], cnt[3]); break;
        case 'F': swap(cnt[2], cnt[3]); break;
        }
    }

    for (int i=0;i<4; i++) {
        if (cnt[i] == 1) {
            cout << (i + 1) << '\n';
            break;
        }
    }

    for (int i=0;i<4; i++) {
        if (cnt[i] == 2) {
            cout << (i + 1) << '\n';
            break;
        }
    }

    return 0;
}