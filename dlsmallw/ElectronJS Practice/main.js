// Primary entry point for the application

const { app, BrowserWindow, Menu } = require('electron');
const path = require('node:path');

const isMac = process.platform === 'darwin';
const isDev = process.env.NODE_ENV !== 'production';

const createWindow = () => {
    const win = new BrowserWindow({
        width: isDev ? 1200 : 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        }
    })

    if (isDev) {
        win.webContents.openDevTools();
    }

    win.loadFile('index.html')
}

const createAboutWindow = () => {
    const aboutWin = new BrowserWindow({
        title: 'About Window',
        width: 800,
        height: 600
    })

    aboutWin.loadFile('about.html')
}

const menu = [
    {
        label: app.name,
        submenu: [
            {
                label: 'About',
                click: createAboutWindow
            }
        ]
    },
    {
        role: 'fileMenu',
    },
]

app.whenReady().then(() => {
    createWindow()

    const mainMenu = Menu.buildFromTemplate(menu);
    Menu.setApplicationMenu(mainMenu);

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow()
    })
})



app.on('window-all-closed', () => {
    if (!isMac) app.quit()
})