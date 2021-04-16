const route = "192.168.1.10/"

var park = {
  1: "1",
  2: "1",
  3: "1",
}

let count = 0;

console.log(sessionStorage.getItem('status'));
if (sessionStorage.getItem('status') === 'loggedIn'){
  //redirect to page
  // alert("Is Login : True");
  }
else{
  window.location.replace("login.html")
  //show validation message
  //  alert("Is Login : False");
}


function logout()
{
  sessionStorage.setItem('status','loggedOut')
  window.location.replace("login.html")    
}

function getstatus()
{
  var i = 0;
  fetch(route + "find_all", {
        method: "GET",
        headers: { "Content-Type": "application/json" },

    }).then((response) => response.json())
    .then((datas) => {
      datas.forEach(data => {
        park[data["idName"]] = data["light"];
        if(data["light"] === "0")
        {
          i++;
        }
      });
      count = i;
    })
}

function changestatus()
{
  Object.keys(park).forEach((zone)=>
  {
    var status = document.getElementById('status_pk'+zone);
    var cl = document.getElementById('card_pk'+zone)
    if(park[zone] === '0')
    {
        
        status.innerText = 'Available';
        cl.style.backgroundColor = "hsl(101, 61%, 50%)";
    }
    else
    {
        status.innerText = 'Not Available';
        cl.style.backgroundColor = "red";
    }
  });
}

function setnumber()
{
  var desti = document.getElementById('count');
  const no = count.toString()
  desti.innerText = "Available :"+ no;
}

function sentinfo(x)
{
  console.log("lul");
  if(park[x] === "0")
  {
    if(confirm("Want to reserve this"))
    {
      fetch(route+"update_light",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ idName:parseInt(x)}),
      }).then((response) => console.log(response)).then(jj=>{console.log("success");});
    }
  }
}

setInterval(() => {
  // get_empty();
  // console.log("test");
  getstatus();
  changestatus();
  setnumber();
},1000);