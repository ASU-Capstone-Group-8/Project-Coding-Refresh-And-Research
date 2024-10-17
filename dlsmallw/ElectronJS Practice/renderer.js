

const nodeVersion = document.getElementById('node-version')
nodeVersion.innerText = versions.node()

const chromeVersion = document.getElementById('chrome-version')
chromeVersion.innerHTML = versions.chrome()

const electronVersion = document.getElementById('electron-version')
electronVersion.innerHTML = versions.electron()