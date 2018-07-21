/**
 * Created by Administrator on 2017/12/9.
 **/
function myFunction(n){
    if(n===1){return 1;}
    var result=n+myFunction(n-1);
    return result;
}
function mymaxfunction(){
    if (arguments.length>0){
        document.write("有不止一个参数</br>");
        var long=arguments.length;
        // document.write(long)
        var max=-Infinity;
        var i = 0;
        for (;i<long;i++) {
            // document.write(arguments[i]);
            if (arguments[i] > max) {
                max = arguments[i]
            }
        }
        return max
    }
}
var a=mymaxfunction(100,2,3,4,5,6,7,8,8,2,34,23,43,2,432,4,32,4,32,432,54,3,3244,23,65,34,23,432);
document.write(a);