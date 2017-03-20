#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <string>

using namespace std;

struct splitRes{
  string a;
  string b;
};
struct coordinate{
  int x;
  int y;
  int cr;// used to identify col or row (col = 1; row = 2, 0 = unInit);
};

const int INFINITY = 1000000000; //choosing an arbitrary large int (out of range) to represent infinity;

struct node{
  bool active;
  bool visited;
  int steps;
  int x;
  int y;
  coordinate parent;
};

splitRes split(string raw){
  splitRes res;
  int pos = raw.find(',');
  res.a = raw.substr(0, pos);
  res.b = raw.substr(pos+1);
  return res;
}

vector<node> getRelCol(vector<vector<node>> &list, int col, coordinate parent){
  vector<node> res;
  int steps = 0;
  if(parent.y >= 0){
    steps = list[parent.y][parent.x].steps + 1;
  }
  for(int i = 0; i < list.size(); i++){
    if(list[i][col].active && !list[i][col].visited){
      //Not visited but active in col
      list[i][col].visited = true;
      list[i][col].steps = steps;
      list[i][col].parent = parent;
      list[i][col].parent.cr = 1;
      res.push_back(list[i][col]);
    }else if (list[i][col].active){
      //We are active but visited (check if this parent is shorter path)
      if(list[i][col].steps > steps){
        list[i][col].steps = steps;
        list[i][col].parent = parent;
        list[i][col].parent.cr = 1;
      }
    }
  }
  return res;
}

vector<node> getRelRow(vector<vector<node>> &list, int row, coordinate parent){
  vector<node> res;
  int steps = 0;
  if(parent.y >= 0){
    steps = list[parent.y][parent.x].steps; //latteral movements inside the movie have 0 cost :)
  }
  for(int i = 0; i < list[row].size(); i++){
    if(list[row][i].active && !list[row][i].visited){
      list[row][i].visited = true;
      list[row][i].steps = steps;
      list[row][i].parent = parent;
      list[row][i].parent.cr = 2;
      res.push_back(list[row][i]);
    }else if(list[row][i].active){
      //We are already entered check to see if we have a shorter path
      if(list[row][i].steps > steps){
        list[row][i].steps = steps;
        list[row][i].parent = parent;
        list[row][i].parent.cr = 2;
      }
    }
  }
  return res;
}

int search(vector<vector<node>> list, int movieA, int movieB){
  int res = INFINITY;
  queue<node> q;
  vector<node> tmp;
  coordinate parent;
  node current;
  //Start breadth first search (modified)
  parent.x = -1;
  parent.y = -1;
  parent.cr = 0;
  //Initialize the queue;
  tmp = getRelRow(list, movieA, parent);
  for(int i = 0; i < tmp.size(); i++){
    q.emplace(tmp[i]);
  }
  while(!q.empty()){
    current = q.front();
    q.pop();
    parent = current.parent;
    parent.x = current.x;
    parent.y = current.y;
    if(parent.cr == 1){
      //we need to do a row search
      tmp = getRelRow(list, parent.y, parent);
    }else{
      //we need to do a col search
      tmp = getRelCol(list, parent.x, parent);
    }
    for(int i = 0; i < tmp.size(); i++){
      q.emplace(tmp[i]);
    }
  }
  //All distances are set (we must do all as we are looking for optimal path)
  for(int i = 0; i < list[movieB].size(); i++){
    if(list[movieB][i].active && list[movieB][i].steps < res){
      res = list[movieB][i].steps;
    }
  }
  return res;
}

int main() {
  int n, m, o, p, counter, score;
  string tmp;
  splitRes tmpSplit;
  map<string, int> actorsRaw;
  map<string, int> actors;
  map<string, int> movies;
  cin >> n >> m >> o >> p;
  getline(cin, tmp);
  //Read in Raw Actor list
  for(int i = 0; i < n; i++){
    getline(cin, tmp);
    if(actorsRaw.find(tmp) != actorsRaw.end()){
      actorsRaw[tmp] += 1;
    }else{
      actorsRaw[tmp] = 1;
    }
  }
  //Remove all extraneous values (any count less than 2 is a dead end edge)
  counter = 0;
  for(map<string, int>::iterator it = actorsRaw.begin(); it != actorsRaw.end(); ++it){
    if(it->second >= 2){
      actors[it->first] = counter;
      counter++;
    }
  }
  //Read in the movie list
  for(int i = 0; i < m; i++){
    getline(cin, tmp);
    movies[tmp] = i;
  }

  //Init the adjacency list
  vector<vector<node>> aList(movies.size(), vector<node>(actors.size()));
  for(int i = 0; i < movies.size(); i++){
    for(int j = 0; j < actors.size(); j++){
      aList[i][j].active = false;
      aList[i][j].steps = INFINITY;
      aList[i][j].visited= false;
      aList[i][j].x = j;
      aList[i][j].y = i;
    }
  }

  //Read in movie correlation list
  for(int i = 0; i < o; i++){
    getline(cin, tmp);
    tmpSplit = split(tmp);
    if(actors.find(tmpSplit.a) != actors.end()){
      aList[movies[tmpSplit.b]][actors[tmpSplit.a]].active = true;
    }
  }

  //Play the game
  for(int i = 0; i < p; i++){
    getline(cin, tmp);
    tmpSplit = split(tmp);
    score = search(aList, movies[tmpSplit.a], movies[tmpSplit.b]);
    if(score != INFINITY){
      cout << score << endl;
    }else{
      cout << "No Connection" << endl;
    }
  }

  return 0;
}