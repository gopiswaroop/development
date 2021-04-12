function addNew(){
    var newName = prompt('whaat name would u like to add')
    roster.push(newName)
}
function remove(){
    var remName = prompt("what name to remove")
    var index = roster.indexof(remName);
    roster.splice(index,1)
}

function display(){
    console.log(roster);
}

var start = prompt("would you like start the roster web app?y/n")
var request = "empty";

if (start === 'y'){
  while(request !== "quit"){
      request = prompt("please select an option: add,remove,display, or quit")
      if(request === 'add'){
          addNew()
      }else if (request === 'display'){
          display();
      }else if (request === 'remove'){
          remove();
      }else{
          alert("not recognized")
          // request = "quit"
      }
  }
}
alert("thanks for using the web app!please refresh tto start over")