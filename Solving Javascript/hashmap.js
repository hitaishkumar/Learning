console.log(" Hashmap")
let num = "djkfhsufhw98ehru024t34gjvh98hgwouvhs"
var arr = num.split("");
var ob = new Object();
for(let i = 0; i < arr.length; i++) {
   if (ob[arr[i]]) {
    ob[arr[i]] ++;
   }
   else {
    ob[arr[i]] = 1
   }
}
maxx = Math.max(...Object.values(ob))
Object.keys(ob).forEach(element => {
  if(ob[element] == maxx)  {
    console.log(element,'element is the most frequent in ', num)
  }  
});