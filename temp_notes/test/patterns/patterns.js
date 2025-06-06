var rows = 5;


function pattern1() {
    for (let i = 0; i < rows; i++) {
      var str = "";
      for (let j = 0; j < rows; j++) {
          str = str + " * ";
      }
      
      console.log(str);
    }    
}

function pattern2() {
    for (let i = 0; i < rows; i++) {
      var str = "";
      for (let j = 0; j < i; j++) {
          str = str + " * ";
      }
      
      console.log(str);
    }    
}

function pattern3() {
    for (let i = 1; i <= rows; i++) {
      var str = "";
      for (let j = 1; j <= i; j++) {
          str = str + " " + j + " ";
      }
      
      console.log(str);
    }    
}

function pattern4() {
    for (let i = 1; i <= rows; i++) {
      var str = "";
      for (let j = 1; j <= i; j++) {
          str = str + " " + i + " ";
      }
      
      console.log(str);
    }    
}

function pattern5() {
    for (let i = 1; i <= rows; i++) {
      var str = "";
      for (let j = 1; j <= rows - i + 1; j++) {
          str = str + " * ";
      }
      
      console.log(str);
    }    
}

function pattern6() {
    for (let i = 1; i <= rows; i++) {
      var str = "";
      for (let j = 1; j <= rows - i + 1; j++) {
          str = str + " " + j + " ";
      }
      
      console.log(str);
    }    
}

function pattern7() {
    for (let i = 0; i < rows; i++) {
      var str = "";
      
      for (let j = 0; j < rows - i + 1; j++) {
          str = str + "  ";
      }
      
      for (let j = 0; j < 2 * i + 1; j++) {
          str = str + " * ";
      }
      
      for (let j = 0; j < rows - i + 1; j++) {
          str = str + "  ";
      }
      
      console.log(str);
    }    
}

function pattern8() {
    for (let i = 0; i < rows; i++) {
      var str = "";
      
      for (let j = 0; j < i; j++) {
          str = str + "  ";
      }
      
      for (let j = 0; j < 2*rows - (2*i + 1); j++) {
          str = str + " * ";
      }
      
      for (let j = 0; j < i; j++) {
          str = str + "  ";
      }
      
      console.log(str);
    }    
}

function pattern10() { 
  for (let i = 1; i <= 2*rows - 1; i++) {
     
      var stars = i;
      if (i>rows) stars = 2*rows - i 
       var str = "";
      for (let j = 1; j <= stars; j++) {
          str = str + "*";
      }
      
      console.log(str);
    }   
}

function pattern11() {
    
    let start = 1;
    for (let i = 1; i <= rows; i++) {
      var str = "";
     
     if(i%2 == 0) {
       start = 1;
     } else { 
       start = 0;
     }
      
      for (let j = 1; j <= i; j++) {
          str = str + start;
          start = 1 - start;
      }
      
      console.log(str);
    }    
}

function pattern12() {
  
  let space = 2 * (rows - 1);
    
    for (let i = 1; i <= rows; i++) {
      var str = "";
     
      
      for (let j = 1; j <= i; j++) {
          str = str + j;
      }
      
      for (var j = 1; j <= space; j++) {
        str = str + "_";
      }
      
      for (let j = i; j >= 1; j--) {
          str = str + j;
      }
      console.log(str);
      space = space - 2;
    }    
}


function pattern13() {
  let num = 1
    for (let i = 1; i <= rows; i++) {
      var str = "";
     
      
      for (let j = 1; j <= i; j++) {
          str = str + num;
          num = num + 1;
      }
    
      console.log(str);
    }    
}

function pattern14() {

    for (let i = 1; i <= rows; i++) {
      var str = "";
      
      for (let j = 0; j < i; j++) {
          str = str + String.fromCharCode(65 + j);
      }
    
      console.log(str);
    }    
}


function pattern15() {

    for (let i = 0; i < rows; i++) {
      var str = "";
      
      for (let j = 0; j < rows - i; j++) {
          str = str + String.fromCharCode(65 + j);
      }
    
      console.log(str);
    }    
}


function pattern16() {

   
    for (let i = 0; i < rows; i++) {
      var char = "";
      var str = String.fromCharCode(65 + i);
      for (let j = 0; j <= i; j++) {
          char = char + str;
      }
      console.log(char);
    }    
}

function pattern17() {

   
    for (let i = 0; i < rows; i++) {
      var str = "";
      
      for (var j = 0; j < rows - i - 1; j++) {
        str = str + "_";
      }
      
      // let char = String.fromCharCode(65);
      for (var j = 0; j < 2 * i + 1; j++) {
        str = str + String.fromCharCode(65 + j);
      }
      
      
      for (var j = 0; j < rows - i - 1; j++) {
        str = str + "_";
      }
     
      console.log(str);
    }    
}

function pattern18() {

   
    for (let i = 0; i < rows; i++) {
      var str = "";
      
      for (var j = rows - i ; j <= rows; j++) {
        str = str + String.fromCharCode(65 + rows - i);
      }
    
     
      console.log(str);
    }    
}
console.log(pattern1());
