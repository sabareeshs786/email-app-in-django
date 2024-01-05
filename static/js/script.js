/*

inspiration: 
https://dribbble.com/shots/2292415-Daily-UI-001-Day-001-Sign-Up

*/

let form = document.querySelecter('form');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  return false;
});

setTimeout(function(){
  if($('#msg').length > 0){
    $('#msg').remove();
  }
}, 2000);