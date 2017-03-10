#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int count, sec, min, hour, tmp;
  cin >> count;
  for(int i = 0; i < count; i++){
    cin >> tmp;
    sec = tmp % 100;
    tmp /= 100;
    min = tmp % 100;
    tmp /= 100;
    hour = tmp;
    if(hour > 12 && hour != 24){
      cout << setfill('0') << setw(2) <<  (hour-12) << ":" << setw(2) << min << ":" << setw(2) << sec<< " PM" << endl;
    } else if ( hour == 00 || hour == 24){
      cout << setfill('0') << setw(2) <<  12 << ":" << setw(2) << min << ":" << setw(2) << sec << " AM" << endl;
    } else {
      cout << setfill('0') << setw(2) <<  hour << ":" << setw(2) << min << ":" << setw(2) << sec << " AM" << endl;
    }
  }
  return 0;
}