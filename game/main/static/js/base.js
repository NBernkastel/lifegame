function toggleMenu() {
  var menu = document.querySelector('.menu');
  menu.classList.toggle('active');
}

var taskform = document.getElementById("taskform");
var check = document.querySelectorAll("#terms")

check.forEach(function (check) {
  check.addEventListener("change", function (event) {
    submitForm();
  });
})

// Функция отправки формы
function submitForm() {
    // Здесь вы можете выполнить необходимые действия перед отправкой формы, например, валидацию данных
    // Отправка POST-запроса
    taskform.submit();
  }
