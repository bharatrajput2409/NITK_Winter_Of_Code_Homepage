var login_sellector=document.querySelector(".login-sellector");
var register_sellector=document.querySelector(".register-sellector");


login_sellector.addEventListener("click",()=>{
    login_sellector.style.borderBottom = "0px";
    register_sellector.style.borderBottom = "2px solid rgba(219,219,219,1)";
    document.querySelector(".login-register-slider").style.transform = "translateX(0px)";
});
register_sellector.addEventListener("click",()=>{
    login_sellector.style.borderBottom = "2px solid rgba(219,219,219,1)";
    register_sellector.style.borderBottom = "0px";
    document.querySelector(".login-register-slider").style.transform = "translateX(-50%)";
});

var loginorregister=document.querySelector("input#loginorregister");
var switchtoregister;
if(loginorregister.value==0){
      switchtoregister=setInterval(registerswitch,500);
}
function registerswitch(){
    login_sellector.style.borderBottom = "2px solid rgba(219,219,219,1)";
    register_sellector.style.borderBottom = "0px";
    document.querySelector(".login-register-slider").style.transform = "translateX(-50%)";
    clearInterval(switchtoregister);
}
var registererror=document.querySelector(".registererror");
function validateregister(form){
    registererror.innerHTML="";
    var regpadtt = /^[0-9][0-9][0-9][0-9][0-9][0-9]$/;
    if(form.username.value.match(regpadtt)){
        console.log("username correct");
    }else{
        console.log(form.username.value)
        registererror.innerHTML="Registration Number should be 6 digit"
        return false;
    }
    if(form.password1.value!=form.password2.value){
        registererror.innerHTML="Both password does not matched !"
        return false;
    }
    if(form.password1.value.length<7){
        registererror.innerHTML="Password should be greater then 6 charactor !"
        return false;
    }
    var regbatch = /^[0-9][0-9][0-9][0-9]$/;
    if(form.batch.value.match(regbatch)){
        console.log("username correct");
    }else{
        console.log(form.username.value)
        registererror.innerHTML="Batch should be 4 digit"
        return false;
    }
    return true;
}
function checkforavailableusername(value){
    xml=new XMLHttpRequest();
    console.log(value)
    xml.open("GET",'/ajex/checkforavailableusername/'+value,true);
    xml.onload=function(){
        if (this.status==200){
            if(this.responseText=="1"){
                registererror.innerHTML= '<span style="color: red;">Usename is Not available</span>'
            }else{
                registererror.innerHTML= '<span style="color: green;">Usename is available</span>'
            }
            
        }
    }
    xml.send()
}