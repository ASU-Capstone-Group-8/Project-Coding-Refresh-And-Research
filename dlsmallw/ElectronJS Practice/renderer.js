
const nodeVersion = document.getElementById('node-version')
nodeVersion.innerHTML = versions.node()

const chromeVersion = document.getElementById('chrome-version')
chromeVersion.innerHTML = versions.chrome()

const electronVersion = document.getElementById('electron-version')
electronVersion.innerHTML = versions.electron()

document.getElementById('btnSwitch').addEventListener('click',()=>{
    if (document.documentElement.getAttribute('data-bs-theme') == 'dark') {
        document.documentElement.setAttribute('data-bs-theme','light')
    }
    else {
        document.documentElement.setAttribute('data-bs-theme','dark')
    }
})