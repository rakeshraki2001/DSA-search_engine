const fs = require('fs');
const { removeStopwords } = require('stopword');

const freqMap = (array) => {
  const map = {};
  array.forEach(item => {
     if(map[item]){
        map[item]++;
     }else{
        map[item] = 1;
     }
  });
  return map;
};
function keywords(filename){
  fs.readFile(filename, (err, data) => {
    if (err) console.log("error");
    s=data.toString('utf-8');
    let oldString = s.replace( /\n/g," ").replace( /\r/g, "").replace(/[^A-Za-z]+/g, ' ').split(" ");
    let newString = removeStopwords(oldString,[''])
    let keys=newString.sort();
    console.log(keys.length)
    allkeys = [allkeys, ...keys]
    console.log(allkeys.length)
    allkeys.sort()
    }
  )
}

keywords("./problemstatements/problem1.txt")
keywords("./problemstatements/problem2.txt")
