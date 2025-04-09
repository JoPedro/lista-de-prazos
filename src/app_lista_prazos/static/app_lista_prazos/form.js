function changeDateInput() {
    const checkbox = document.getElementsByName('agora')[0]
    const dateInput = document.getElementsByName('data_de_vencimento')[0]

    // Checar ao carregar página
    dateInput.disabled = checkbox.checked

    checkbox.addEventListener('change', function () {
        dateInput.disabled = this.checked;
    })
}