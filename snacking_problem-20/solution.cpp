#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
  map<int, string> valueMap;
  map<string, int> keyMap;
  int total, current, num, lookingFor;
  string name;
  cin >> total;
  cin >> num;
  for(int i = 0; i < num; i++){
    cin >> name >> current;
    valueMap[current] = name;
    keyMap[name] = current;
  }
  cin >> num;
  for(int i = 0; i < num ; i++){
    cin >> name;
    current = keyMap[name];
    lookingFor = total - current;
    auto it = valueMap.find(lookingFor);
    if(it != valueMap.end()){
      cout << valueMap[lookingFor] << endl;
    }else{
      cout << "There is no matching snack Joe" << endl;
    }
  }
  return 0;
}