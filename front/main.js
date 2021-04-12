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