const data={
    bas: "1q2w3e4r",
    bank: "123456"
}

const route = "192.168.1.12/"

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
        fetch(route + "USER/find_user", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username:user,passwd:password }),
            }).then((response) => response.json()).then((datas) => {
            if(datas["result"]==="1" || datas["result"]==="2")
            {
                alert("This user already register");
                check = true;
            }
            else 
            {
                if(password1 !== password2)
                {
                    alert("please check your confirm password")
                }
                else
                {
                    fetch(route + "USER/register", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ username:user,passwd:password }),
                        }).then((response) => console.log(response)).then(jj=>{console.log("success");});
                }
            }
        });
        // let check = false;
        // Object.keys(data).forEach(id => {
        //     if(user === id)
        //     {
        //         alert("This user already register");
        //         check = true;
        //     }
        // });
        // if(!check)
        // {
        //     if(password1 !== password2)
        //     {
        //         alert("please check your confirm password")
        //     }
        //     else
        //     {
        //         alert("register Success")
        //     }
        // } 
    }
}