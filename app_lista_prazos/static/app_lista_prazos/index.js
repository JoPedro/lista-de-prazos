let prazoAtual

const cadastrar = document.getElementById('cadastrar')
const adicionarTab = document.getElementById('adicionar-tab')
const excluirTab = document.getElementById('excluir-tab')
const overlay = document.getElementsByClassName('overlay')[0]
const fecharAdicionar = document.getElementById('fechar-adicionar')
const fecharExcluir = document.getElementById('fechar-excluir')
const checkbox = document.getElementsByName('agora')[0]
const dateInput = document.getElementsByName('data_de_vencimento')[0]

cadastrar.addEventListener('click', () => toggleSidebarDisplay(adicionarTab))
fecharAdicionar.addEventListener('click', () => toggleSidebarDisplay(adicionarTab))
fecharExcluir.addEventListener('click', () => toggleSidebarDisplay(excluirTab))

checkbox.addEventListener('change', function () {
    dateInput.disabled = this.checked
})

function toggleSidebarDisplay(tab) {
    tab.style.display = tab.style.display === 'block' ? 'none' : 'block'
    overlay.style.display = overlay.style.display === 'block' ? 'none' : 'block'
}

function excluirPrazo(prazo) {
    toggleSidebarDisplay(excluirTab)
    prazoAtual = prazo
}
