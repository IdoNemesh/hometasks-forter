function login_status(network, status)
{
  if (status)
  {
    console.log("Logged in to " + network);
  }
  else
  {
    console.log("Not logged in to " + network);
  }
};

if (document.URL === "https://www.macsales.com" || document.URL === "https://www.macsales.com/")
{
  let google = document.createElement("img");
  google.onload = function(){login_status('Google', true)};
  google.onerror = function(){login_status('Google', false)};
  google.src = "https://accounts.google.com/CheckCookie?continue=https%3A%2F%2Fwww.google.com%2Fintl%2Fen%2Fimages%2Flogos%2Faccounts_logo.png&followup=https%3A%2F%2Fwww.google.com%2Fintl%2Fen%2Fimages%2Flogos%2Faccounts_logo.png&chtml=LoginDoneHtml&checkedDomains=youtube&checkConnection=youtube%3A291%3A1";
};
