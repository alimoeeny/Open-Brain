//alert('We would have menu sometime!');
var menuHTML = '<a href="index.html">Home</a> - <a href="about.html">About</a> - <a href="neurons.html"> Neurons </a> ';
var menu = document.createElement('div');
//menu.width = 200;
//menu.height = 30;
menu.setAttribute('Id', 'mainmenu');
menu.innerHTML = menuHTML;
document.getElementsByTagName('Body')[0].appendChild(menu);


