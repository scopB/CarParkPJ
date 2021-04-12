const data={
    bas: "1q2w3e4r",
    bank: "123456"
}

function register()
{
    user=document.getElementById("username_box")["value"];
    password1=document.getElementById("password1_box")["value"];
    password2=document.getElementById("password2_box")["value"];
    
    if(user === "" || password1 === "" || password2 === "")
    {
        alert("Please inform all");
    }
    else{
        let check = false;
        Object.keys(data).forEach(id => {
            if(user === id)
            {
                alert("This user already register");
                check = true;
            }
        });
        if(!check)
        {
            if(password1 !== password2)
            {
                alert("please check your confirm password")
            }
            else
            {
                alert("register Success")
            }
        } 
    }
}