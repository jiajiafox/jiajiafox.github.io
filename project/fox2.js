function alary(x){
    if(x>60000){
        return "就任" ;
    }else{
        return "不就任" ;
    }}
var msg=alary(100000);
document.writeln(msg);