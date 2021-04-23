const options = {
  bottom: '64px', // default: '32px'
  right: '32px', // default: '32px'
  left: 'unset', // default: 'unset'
  time: '0.3s', // default: '0.3s'
  mixColor: '#fff', // default: '#fff'
  backgroundColor: '#fff',  // default: '#fff'
  buttonColorDark: '#100f2c',  // default: '#100f2c'
  buttonColorLight: '#fff', // default: '#fff'
  saveInCookies: true, // default: true,
  label: '🌓', // default: ''
  autoMatchOsTheme: true // default: true
}

const darkmode = new Darkmode(options);
darkmode.showWidget();

function addDarkmodeWidget() {
        new Darkmode().showWidget();
      }


//dark mode for bootstrap form
$('button.darkmode-toggle').click(()=>{
    if (localStorage.getItem('active') == 'true'){
        localStorage.setItem('active', false);
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
    } else {
        localStorage.setItem('active', true);
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
    }
})

//dark mode for bootstrap form localStorage
if (localStorage.getItem('active') == 'true'){
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
}




