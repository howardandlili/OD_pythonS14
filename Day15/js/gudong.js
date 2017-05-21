/**
 * Created by Administrator on 2017/5/22.
 */
function fun1() {
    var tag =document.getElementById('i1');
    var content = tag.innerText;
    var f = content.charAt(0);
    var l = content.substring(1,content.length);
    var new_content = l + f;
    tag.innerText = new_content;
    // content = new_content;
}
setInterval(fun1,500);