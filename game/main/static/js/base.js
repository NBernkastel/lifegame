function toggleMenu() {
  var menu = document.querySelector('.menu');
  menu.classList.toggle('active');
}

var form = document.getElementById("dayform");
var input = document.getElementById("dayinput");

// Обрабатываем событие отправки формы
form.addEventListener("submit", function(event) {
  event.preventDefault(); // Отменяем стандартное поведение формы
  submitForm();
});

// Обрабатываем событие нажатия клавиши в поле ввода
input.addEventListener("keydown", function(event) {
  if (event.keyCode === 13) { // Проверяем, является ли нажатая клавиша "Enter"
    event.preventDefault(); // Отменяем стандартное поведение поля ввода
    submitForm();
  }
});

// Функция отправки формы
function submitForm() {
  // Здесь вы можете выполнить необходимые действия перед отправкой формы, например, валидацию данных

  // Отправка POST-запроса
  form.submit();
}