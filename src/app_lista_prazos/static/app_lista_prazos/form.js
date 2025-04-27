const cadastrar = document.getElementById('cadastrar')
const fechar = document.getElementById('fechar')
const checkbox = document.getElementsByName('agora')[0]
const dateInput = document.getElementsByName('data_de_vencimento')[0]
const aside = document.getElementsByTagName('aside')[0]
const overlay = document.getElementsByClassName('overlay')[0]

cadastrar.addEventListener('click', toggleSidebarDisplay)
fechar.addEventListener('click', toggleSidebarDisplay)

checkbox.addEventListener('change', function () {
    dateInput.disabled = this.checked
})

function toggleSidebarDisplay() {
    aside.style.display = aside.style.display === 'block' ? 'none' : 'block'
    overlay.style.display = overlay.style.display === 'block' ? 'none' : 'block'
}
