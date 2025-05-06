const cadastrar = document.getElementById('cadastrar')
const adicionarTab = document.getElementById('adicionar-tab')
const fecharAdicionarTab = document.getElementById('fechar-adicionar-tab')
const overlay = document.getElementById('semi-black-overlay')

cadastrar.addEventListener('click', toggleSidebarDisplay)
fecharAdicionarTab.addEventListener('click', toggleSidebarDisplay)

function toggleSidebarDisplay() {
    adicionarTab.style.display = adicionarTab.style.display === 'block' ? 'none' : 'block'
    overlay.style.display = overlay.style.display === 'block' ? 'none' : 'block'
}
