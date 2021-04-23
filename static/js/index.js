const options = {
  bottom: '64px', // default: '32px'
  right: '32px', // default: '32px'
  left: 'unset', // default: 'unset'
  time: '0.5s', // default: '0.3s'
  mixColor: '#fff', // default: '#fff'
  backgroundColor: '#fff',  // default: '#fff'
  buttonColorDark: '#100f2c',  // default: '#100f2c'
  buttonColorLight: '#fff', // default: '#fff'
  saveInCookies: false, // default: true,
  label: '🌓', // default: ''
  autoMatchOsTheme: true // default: true
}

const darkmode = new Darkmode(options);
darkmode.showWidget();

function addDarkmodeWidget() {
        new Darkmode().showWidget();
      }



$('button.darkmode-toggle').click(()=>{
    $(["[class*='navbar-light'], [class*='navbar-dark']"]).each((i,ele)=>{
        $(ele).toggleClass('navbar-light navbar-dark');
    })
    $(["[class*='text-light'], [class*='text-dark']"]).each((i,ele)=>{
        $(ele).toggleClass('text-light text-dark');
    })
    $(["[class*='bg-light'], [class*='bg-dark']"]).each((i,ele)=>{
        $(ele).toggleClass('bg-light bg-dark');
    })
    $(["[class*='badge-light'], [class*='badge-dark']"]).each((i,ele)=>{
        $(ele).toggleClass('badge-light badge-dark');
    })
})

