#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

struct SplitVal{
  string lh;
  string rh;
};

SplitVal split(string raw){
  SplitVal res;
  int pos = raw.find(',');
  res.lh = raw.substr(0, pos);
  res.rh = raw.substr(pos+2);
  return res;
}

int trace(vector<int> &list, int start){
  while(list[start] != -1){
    start = list[start];
  }
  return start;
}

int main() {
  int tmpCounter, totalFactions;
  string tmpName;
  //Read in total number of characters
  cin >> tmpCounter;
  cin.get();
  //Init our data
  map<string, int> ref;
  map<int, string> rlookup;
  vector<int> data(tmpCounter);

  //Init character sets
  for( int i = 0; i < tmpCounter; i++){
    getline(cin, tmpName);
    ref[tmpName] = i;
    rlookup[i] = tmpName;
    data[i] = -1;
  }

  //Init allegiances
  SplitVal tmpAlleginace;
  cin >> tmpCounter;
  cin.get();
  for(int i = 0; i < tmpCounter; i++){
    getline(cin, tmpName);
    tmpAlleginace = split(tmpName);
    data[ref[tmpAlleginace.lh]] = ref[tmpAlleginace.rh];
  }

  //Report Number of Unique Factions
  totalFactions = 0;
  for(int i = 0; i < data.size(); i++){
    if(data[i] == -1) totalFactions ++;
  }
  cout << "There are " << totalFactions << " factions playing the game of thrones" << endl;

  //Respond to all queryies
  cin >> tmpCounter;
  cin.get();
  for(int i = 0;  i < tmpCounter; i++){
    getline(cin, tmpName);
    cout << rlookup[trace(data, ref[tmpName])] << endl;
  }

  return 0;
}