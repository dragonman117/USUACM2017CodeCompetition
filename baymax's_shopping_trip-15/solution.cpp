#include <iostream>

using namespace std;

int main() {
  int t, n, c, m, current, free, tmp;
  cin >> t;
  for(int i = 0; i < t; i++){
    cin >> n >> c >> m;
    current = n/c;
    free = current;
    while(free >= m){
      tmp = free/m;
      current += tmp;
      free = tmp;
    }
    cout << current << endl;
  }
  return 0;
}