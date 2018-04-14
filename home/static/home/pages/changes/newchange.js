function fnChose(a,b){
    document.getElementById('t'+a).style = "";
    document.getElementById("sectionTwoTitle").innerHTML =b
    for(i=1;i<=6;i++){
        s='t'+i
        if(i != a){
            document.getElementById(s).style = "display: none;";
        }
    }
}
function fnReq(c,d,e){
    for(i=1;i<=c;i++){
        document.getElementsByName("temp"+d+"_rank"+i+"_res")[0].required = e;
    }
}
function fnTemplate(){
    var e = document.getElementById("selectTemplate");
    var selectTemplate = e.options[e.selectedIndex].value;
    if (selectTemplate == 'License by User') {
        fnChose(1,'License by User');
        fnReq(16,1,true)
        fnReq(6,2,false)
        fnReq(5,3,false)
        fnReq(5,4,false)
        fnReq(11,5,false)
        fnReq(2,6,false)
    } else if (selectTemplate == 'License by Exchange') {
        fnChose(2,'License by Exchange');
        fnReq(16,1,false)
        fnReq(6,2,true)
        fnReq(5,3,false)
        fnReq(5,4,false)
        fnReq(11,5,false)
        fnReq(2,6,false)
    } else if (selectTemplate == 'Release') {
        fnChose(3,'Release');
        fnReq(16,1,false)
        fnReq(6,2,false)
        fnReq(5,3,true)
        fnReq(5,4,false)
        fnReq(11,5,false)
        fnReq(2,6,false)
    } else if (selectTemplate == 'APS Update') {
        fnChose(4,'APS Update');
        fnReq(16,1,false)
        fnReq(6,2,false)
        fnReq(5,3,false)
        fnReq(5,4,true)
        fnReq(11,5,false)
        fnReq(2,6,false)
    } else if (selectTemplate == 'Feeds.ini/gltrade.ini') {
        fnChose(5,'Feeds.ini/gltrade.ini');
        fnReq(16,1,false)
        fnReq(6,2,false)
        fnReq(5,3,false)
        fnReq(5,4,false)
        fnReq(11,5,true)
        fnReq(2,6,false)
    } else if (selectTemplate == 'File.ini') {
        fnChose(6,'File.ini');
        fnReq(16,1,false)
        fnReq(6,2,false)
        fnReq(5,3,false)
        fnReq(5,4,false)
        fnReq(11,5,false)
        fnReq(2,6,true)
    }else{
        for(i=1;i<=6;i++){
            document.getElementById('t'+i).style = "display: none;";
        }
        fnReq(16,1,false)
        fnReq(6,2,false)
        fnReq(5,3,false)
        fnReq(5,4,false)
        fnReq(11,5,false)
        fnReq(2,6,false)
    }
}

function freeTxt(c,b){
    var e = document.getElementsByName("temp"+c+"_rank"+b+"_res")[0];
    var a = e.options[e.selectedIndex].value;
    if (a == 'Yes') {
        document.getElementsByName("temp"+c+"_rank"+b+"_res_req")[0].style = "";
        document.getElementsByName("temp"+c+"_rank"+b+"_res_req")[0].disabled = false;
        document.getElementsByName("temp"+c+"_rank"+b+"_res_req")[0].required = true;
    } else {
        document.getElementsByName("temp"+c+"_rank"+b+"_res_req")[0].style = "display: none";
        document.getElementsByName("temp"+c+"_rank"+b+"_res_req")[0].disabled = true;
        document.getElementsByName("temp"+c+"_rank"+b+"_res_req")[0].required = false;
    }
}

//Template 1 ----------------------------------
function temp1_rank1_res_fn(){
    var e = document.getElementsByName("temp1_rank1_res")[0];
    var a = e.options[e.selectedIndex].value;

    var g = document.getElementsByName("temp1_rank4_res")[0];
    var b = g.options[g.selectedIndex].value;

    var h = document.getElementsByName("temp1_rank7_res")[0];
    var c = h.options[h.selectedIndex].value;

    var i = document.getElementsByName("temp1_rank10_res")[0];
    var d = i.options[i.selectedIndex].value;

    if( a != b){
        document.getElementsByName("temp1_rank5_res")[0].disabled = true;
    }else{
        document.getElementsByName("temp1_rank5_res")[0].disabled = false;
        document.getElementsByName("temp1_rank5_res")[0].required = true;
    }

    if( a != c){
        document.getElementsByName("temp1_rank8_res")[0].disabled = true;
    }else{
        document.getElementsByName("temp1_rank8_res")[0].disabled = false;
        document.getElementsByName("temp1_rank8_res")[0].required = true;
    }

    if( a != d){
        document.getElementsByName("temp1_rank11_res")[0].disabled = true;
    }else{
        document.getElementsByName("temp1_rank11_res")[0].disabled = false;
        document.getElementsByName("temp1_rank11_res")[0].required = true;
    }
}
function temp1_rank3_res_fn(){
    var e = document.getElementsByName("temp1_rank3_res")[0];
    var a = e.options[e.selectedIndex].value;
    if (a == 'No') {
        document.getElementsByName("temp1_rank3_res_req")[0].style = "display: none";
        document.getElementsByName("temp1_rank3_res_req")[0].disabled = true;
        document.getElementsByName("temp1_rank3_res_req")[0].required = false;

        document.getElementsByName("temp1_rank4_res")[0].disabled = true;
        document.getElementsByName("temp1_rank5_res")[0].disabled = true;
        document.getElementsByName("temp1_rank4_res")[0].required = false;
        document.getElementsByName("temp1_rank5_res")[0].required = false;
    } else {
        document.getElementsByName("temp1_rank3_res_req")[0].style = "";
        document.getElementsByName("temp1_rank3_res_req")[0].disabled = false;
        document.getElementsByName("temp1_rank3_res_req")[0].required = true;

        document.getElementsByName("temp1_rank4_res")[0].disabled = false;
        document.getElementsByName("temp1_rank5_res")[0].disabled = false;
        document.getElementsByName("temp1_rank4_res")[0].required = true;
        document.getElementsByName("temp1_rank5_res")[0].required = true;
    }
}
function temp1_rank4_res_fn(){
    var e = document.getElementsByName("temp1_rank4_res")[0];
    var a = e.options[e.selectedIndex].value;

    var f = document.getElementsByName("temp1_rank1_res")[0];
    var b = f.options[f.selectedIndex].value;

    if( a != b){
        document.getElementsByName("temp1_rank5_res")[0].disabled = true;
        document.getElementsByName("temp1_rank5_res")[0].required = false;
    }else{
        document.getElementsByName("temp1_rank5_res")[0].disabled = false;
        document.getElementsByName("temp1_rank5_res")[0].required = true;
    }
}
function temp1_rank5_res_fn(){
    freeTxt(1,5)
}
function temp1_rank6_res_fn(){
    var e = document.getElementsByName("temp1_rank6_res")[0];
    var a = e.options[e.selectedIndex].value;
    if (a == 'No') {
        document.getElementsByName("temp1_rank6_res_req")[0].style = "display: none";
        document.getElementsByName("temp1_rank6_res_req")[0].disabled = true;
        document.getElementsByName("temp1_rank6_res_req")[0].required = false;

        document.getElementsByName("temp1_rank7_res")[0].disabled = true;
        document.getElementsByName("temp1_rank8_res")[0].disabled = true;
        document.getElementsByName("temp1_rank7_res")[0].required = false;
        document.getElementsByName("temp1_rank8_res")[0].required = false;
    }else{
        document.getElementsByName("temp1_rank6_res_req")[0].style = "";
        document.getElementsByName("temp1_rank6_res_req")[0].disabled = false;
        document.getElementsByName("temp1_rank6_res_req")[0].required = true;

        document.getElementsByName("temp1_rank7_res")[0].disabled = false;
        document.getElementsByName("temp1_rank8_res")[0].disabled = false;
        document.getElementsByName("temp1_rank7_res")[0].required = true;
        document.getElementsByName("temp1_rank8_res")[0].required = true;
    }
}
function temp1_rank7_res_fn(){
    var e = document.getElementsByName("temp1_rank7_res")[0];
    var a = e.options[e.selectedIndex].value;

    var f = document.getElementsByName("temp1_rank1_res")[0];
    var b = f.options[f.selectedIndex].value;

    if(a!=b){
        document.getElementsByName("temp1_rank8_res")[0].disabled = true;
        document.getElementsByName("temp1_rank8_res")[0].required = false;
    }else{
        document.getElementsByName("temp1_rank8_res")[0].disabled = false;
        document.getElementsByName("temp1_rank8_res")[0].required = true;
    }
}
function temp1_rank8_res_fn(){
    freeTxt(1,8)
}
function temp1_rank9_res_fn(){
    var e = document.getElementsByName("temp1_rank9_res")[0];
    var a = e.options[e.selectedIndex].value;
    if (a == 'No') {
        document.getElementsByName("temp1_rank9_res_req")[0].style = "display: none";
        document.getElementsByName("temp1_rank9_res_req")[0].disabled = true;
        document.getElementsByName("temp1_rank9_res_req")[0].required = false;

        document.getElementsByName("temp1_rank10_res")[0].disabled = true;
        document.getElementsByName("temp1_rank11_res")[0].disabled = true;
        document.getElementsByName("temp1_rank10_res")[0].required = false;
        document.getElementsByName("temp1_rank11_res")[0].required = false;
    }else{
        document.getElementsByName("temp1_rank9_res_req")[0].style = "";
        document.getElementsByName("temp1_rank9_res_req")[0].disabled = false;
        document.getElementsByName("temp1_rank9_res_req")[0].required = true;

        document.getElementsByName("temp1_rank10_res")[0].disabled = false;
        document.getElementsByName("temp1_rank11_res")[0].disabled = false;
        document.getElementsByName("temp1_rank10_res")[0].required = true;
        document.getElementsByName("temp1_rank11_res")[0].required = true;
    }
}
function temp1_rank10_res_fn(){
    var e = document.getElementsByName("temp1_rank10_res")[0];
    var a = e.options[e.selectedIndex].value;

    var f = document.getElementsByName("temp1_rank1_res")[0];
    var b = f.options[f.selectedIndex].value;

    if(a!=b){
        document.getElementsByName("temp1_rank11_res")[0].disabled = true;
        document.getElementsByName("temp1_rank11_res")[0].required = false;
    }else{
        document.getElementsByName("temp1_rank11_res")[0].disabled = false;
        document.getElementsByName("temp1_rank11_res")[0].required = true;
    }
}
function temp1_rank11_res_fn(){
    freeTxt(1,11)
}
function temp1_rank12_res_fn(){
    freeTxt(1,12)
}
function temp1_rank13_res_fn(){
    freeTxt(1,13)
    var e = document.getElementsByName("temp1_rank13_res")[0];
    var a = e.options[e.selectedIndex].value;
    if (a == 'No') {
        document.getElementsByName("temp1_rank14_res")[0].disabled = true;
        document.getElementsByName("temp1_rank14_res")[0].required = false;
    } else {
        document.getElementsByName("temp1_rank14_res")[0].disabled = false;
        document.getElementsByName("temp1_rank14_res")[0].required = true;
    }
}
function temp1_rank14_res_fn(){
    freeTxt(1,14)
}
function temp1_rank15_res_fn(){
    freeTxt(1,15)
}
function temp1_rank16_res_fn(){
    freeTxt(1,16)
}

//Template 2 ----------------------------------
function temp2_rank1_res_fn(){
    freeTxt(2,1)
}
function temp2_rank2_res_fn(){
    freeTxt(2,2)
}
function temp2_rank3_res_fn(){
    freeTxt(2,3)
}
function temp2_rank4_res_fn(){
    freeTxt(2,4)
}
function temp2_rank5_res_fn(){
    freeTxt(2,5)
}
function temp2_rank6_res_fn(){
    freeTxt(2,6)
}

//Template 3 ----------------------------------
function temp3_rank4_res_fn(){
    freeTxt(3,4)
}
function temp3_rank5_res_fn(){
    freeTxt(3,5)
}

//Template 4 ----------------------------------
function temp4_rank3_res_fn(){
    freeTxt(4,3)
}

//Template 5 ----------------------------------
function temp5_rank3_res_fn(){
    freeTxt(5,3)
}
function temp5_rank4_res_fn(){
    freeTxt(5,4)
}
function temp5_rank5_res_fn(){
    freeTxt(5,5)
}
function temp5_rank6_res_fn(){
    freeTxt(5,6)
}
function temp5_rank7_res_fn(){
    freeTxt(5,7)
}
function temp5_rank8_res_fn(){
    freeTxt(5,8)
}
function temp5_rank9_res_fn(){
    freeTxt(5,9)
}
function temp5_rank10_res_fn(){
    freeTxt(5,10)
}
function temp5_rank11_res_fn(){
    freeTxt(5,11)
}


//Tooltip (Help)
$(function () {
    //Tooltip
    $('[data-toggle="tooltip"]').tooltip({
        container: 'body'
    });
    //Popover
    $('[data-toggle="popover"]').popover();
})

//Error msg
document.addEventListener("DOMContentLoaded", function() {
    var elements = document.getElementsByTagName("textarea");
    var elements2 = document.getElementsByTagName("select");
    for (var i = 0; i < elements.length; i++) {
        elements[i].oninvalid = function(e) {
            e.target.setCustomValidity("");
            if (!e.target.validity.valid) {
                e.target.setCustomValidity("This field cannot be left blank");
            }
        };
        elements[i].oninput = function(e) {
            e.target.setCustomValidity("");
        };
    }

    for (var i = 0; i < elements2.length; i++) {
        elements2[i].oninvalid = function(e) {
            e.target.setCustomValidity("");
            if (!e.target.validity.valid) {
                e.target.setCustomValidity("Please select something");
            }
        };
        elements2[i].oninput = function(e) {
            e.target.setCustomValidity("");
        };
    }
})

function fn11(){
    for(i=1;i<=6;i++){
        document.getElementById('t'+i).style = "display: none;";
    }
    fnReq(16,1,false)
    fnReq(6,2,false)
    fnReq(5,3,false)
    fnReq(5,4,false)
    fnReq(11,5,false)
    fnReq(2,6,false)
}
window.onload = fn11()

function fn12(){
    var e = document.getElementById("selectTemplate");
    var selectTemplate = e.options[e.selectedIndex].value;
    if (selectTemplate == 'License by User') {
        fnChose(1,'License by User');
        fnReq(16,1,true)
        fnReq(6,2,false)
        fnReq(5,3,false)
        fnReq(5,4,false)
        fnReq(11,5,false)
        fnReq(2,6,false)
    } else if (selectTemplate == 'License by Exchange') {
        fnChose(2,'License by Exchange');
        fnReq(16,1,false)
        fnReq(6,2,true)
        fnReq(5,3,false)
        fnReq(5,4,false)
        fnReq(11,5,false)
        fnReq(2,6,false)
    } else if (selectTemplate == 'Release') {
        fnChose(3,'Release');
        fnReq(16,1,false)
        fnReq(6,2,false)
        fnReq(5,3,true)
        fnReq(5,4,false)
        fnReq(11,5,false)
        fnReq(2,6,false)
    } else if (selectTemplate == 'APS Update') {
        fnChose(4,'APS Update');
        fnReq(16,1,false)
        fnReq(6,2,false)
        fnReq(5,3,false)
        fnReq(5,4,true)
        fnReq(11,5,false)
        fnReq(2,6,false)
    } else if (selectTemplate == 'Feeds.ini/gltrade.ini') {
        fnChose(5,'Feeds.ini/gltrade.ini');
        fnReq(16,1,false)
        fnReq(6,2,false)
        fnReq(5,3,false)
        fnReq(5,4,false)
        fnReq(11,5,true)
        fnReq(2,6,false)
    } else if (selectTemplate == 'File.ini') {
        fnChose(6,'File.ini');
        fnReq(16,1,false)
        fnReq(6,2,false)
        fnReq(5,3,false)
        fnReq(5,4,false)
        fnReq(11,5,false)
        fnReq(2,6,true)
    }else{
        for(i=1;i<=6;i++){
            document.getElementById('t'+i).style = "display: none;";
        }
        fnReq(16,1,false)
        fnReq(6,2,false)
        fnReq(5,3,false)
        fnReq(5,4,false)
        fnReq(11,5,false)
        fnReq(2,6,false)
    }
}
window.onload = fn12()

function fn13(){
    var e = document.getElementById("selectTemplate");
    var selectTemplate = e.options[e.selectedIndex].value;
    if (selectTemplate == 'License by User') {
        freeTxt(1,3)
        freeTxt(1,5)
        freeTxt(1,6)
        freeTxt(1,8)
        freeTxt(1,9)
        freeTxt(1,11)
        freeTxt(1,12)
        freeTxt(1,13)
        freeTxt(1,14)
        freeTxt(1,15)
        freeTxt(1,16)
    } else if (selectTemplate == 'License by Exchange') {
        freeTxt(2,1)
        freeTxt(2,2)
        freeTxt(2,3)
        freeTxt(2,4)
        freeTxt(2,5)
        freeTxt(2,6)
    } else if (selectTemplate == 'Release') {
        freeTxt(3,4)
        freeTxt(3,5)
    } else if (selectTemplate == 'APS Update') {
        freeTxt(4,3)
    } else if (selectTemplate == 'Feeds.ini/gltrade.ini') {
        freeTxt(5,3)
        freeTxt(5,4)
        freeTxt(5,5)
        freeTxt(5,6)
        freeTxt(5,7)
        freeTxt(5,8)
        freeTxt(5,9)
        freeTxt(5,10)
        freeTxt(5,11)
    }
}
window.onload = fn13()

function fn14() {
    var e = document.getElementsByName('temp1_rank3_res')[0];
    var selectTemplate = e.options[e.selectedIndex].value;
    if (selectTemplate=='No'){
        document.getElementsByName('temp1_rank4_res')[0].required = false;
        document.getElementsByName('temp1_rank4_res')[0].disabled = true;
        document.getElementsByName('temp1_rank5_res')[0].required = false;
        document.getElementsByName('temp1_rank5_res')[0].disabled = true;
    }
    e = document.getElementsByName('temp1_rank6_res')[0];
    selectTemplate = e.options[e.selectedIndex].value;
    if(selectTemplate=='No'){
        document.getElementsByName('temp1_rank7_res')[0].required = false;
        document.getElementsByName('temp1_rank7_res')[0].disabled = true;
        document.getElementsByName('temp1_rank8_res')[0].required = false;
        document.getElementsByName('temp1_rank8_res')[0].disabled = true;
    }
    e = document.getElementsByName('temp1_rank9_res')[0];
    selectTemplate = e.options[e.selectedIndex].value;
    if(selectTemplate=='No'){
        document.getElementsByName('temp1_rank10_res')[0].required = false;
        document.getElementsByName('temp1_rank10_res')[0].disabled = true;
        document.getElementsByName('temp1_rank11_res')[0].required = false;
        document.getElementsByName('temp1_rank11_res')[0].disabled = true;
    }
}
window.onload= fn14()
