const data={
    bas: "1q2w3e4r",
    bank: "123456"
}

const route = "192.168.1.10/"

function login(){
    const user = document.getElementById("user_box")["value"]
    const password = document.getElementById("password_box")["value"]
    let check = true;
    if(user !== "" && password !== "")
    {
        fetch(route + "find_user", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username:user,passwd:password }),
            }).then((response) => response.json()).then((datas) => {
            if(datas["result"]==="1")
            {
                sessionStorage.setItem('status','loggedIn') 
                // window.location.replace("main.html");    
            }
            else if (datas["result"]==="2")
            {
                var popup = document.getElementById("myPopup");
                popup.classList.toggle("show");
                setTimeout(() => { popup.classList.toggle("show"); }, 1000);
            }
            else 
            {
                // console.log("test");
                var popup = document.getElementById("myPopup2");
                popup.classList.toggle("show");
                setTimeout(() => { popup.classList.toggle("show"); }, 1000);
            }
        });
        // Object.keys(data).forEach(id => {
        //     if(id===user)
        //     {
        //         check = false;
        //         if(data[id] === password)
        //         {
        //             sessionStorage.setItem('status','loggedIn') 
        //             window.location.replace("main.html");    
        //         }
        //         else
        //         {
        //             var popup = document.getElementById("myPopup");
        //             popup.classList.toggle("show");
        //             setTimeout(() => { popup.classList.toggle("show"); }, 1000);
        //         }
        //         return;
        //     }   
        //     });
        // if(check)
        // {
        //     // console.log("test");
        //     var popup = document.getElementById("myPopup2");
        //     popup.classList.toggle("show");
        //     setTimeout(() => { popup.classList.toggle("show"); }, 1000);
        // }  
    }
    else
    {
        alert("Please inform all");
    }

    
}