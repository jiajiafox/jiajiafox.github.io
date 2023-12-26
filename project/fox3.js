var str = "第一題";
document.writeln(str+"<br>");
for(i=0;i<30;i++){
    if (i%2==0){
        document.writeln(i+"<br>");
    }}

var strb = "第二題";
document.writeln(strb+"<br>");
for(j=0;j<30;j++){
    if(j%2==0 && j%3!=0){
        document.writeln(j+"<br>");
    }} 

var strc = "第三題";
document.writeln(strc+"<br>");
var k = 0;
while(k<30){
    if(k%2!=0)
        document.writeln(k+"<br>");
    k++;
}


