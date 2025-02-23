const toastTrigger = document.getElementById('liveToastBtn');
const toastLiveExample = document.getElementById('liveToast');

if (toastTrigger) {
  const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample);
  toastTrigger.addEventListener('click', () => {
    toastBootstrap.show();
  });
}

document.addEventListener("DOMContentLoaded", function () {
    const toastLiveExample = document.getElementById("liveToast");
    const generatedPassword = document.getElementById("generatedPassword").value;

    if (generatedPassword == "None") {
        // pass
    } else {
        const toast = new bootstrap.Toast(toastLiveExample);
        toast.show();
    }
});

// Обновляем значение длины пароля при изменении ползунка
document.addEventListener('DOMContentLoaded', function () {
    const rangeInput = document.getElementById('customRange3');
    const passwordLengthValue = document.getElementById('passwordLengthValue');
    if (rangeInput && passwordLengthValue) {
        rangeInput.addEventListener('input', function () {
            passwordLengthValue.textContent = this.value;
        });
    }
});