const header = document.querySelector ('.main-header');

window.addEventListener('scroll', () => {
    const scrollPos = window.scrollY;
    if (scrollPos > 5){
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
})

var checkbox = document.querySelector( '#menu-btn' );
var icon = document.querySelector( '#menu-icon' );
var listener = function( e ) {
  if( e.target != checkbox && e.target != icon ) {
    checkbox.checked = false;
    document.removeEventListener( 'click', listener );
  }
};

checkbox.addEventListener( 'click', function(){
  if( this.checked ) {
    document.addEventListener( 'click', listener );
  } 
});