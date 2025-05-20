document.querySelectorAll('.action-link').forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const action = e.target.dataset.action; // 'like', 'share' и т.д.

    // Удаляем старое скрытое поле (если было)
    const oldField = document.querySelector('input[name="action"]');
    if (oldField) oldField.remove();

    // Добавляем новое скрытое поле в форму
    const input = document.createElement('input');
    input.type = 'hidden';	
    input.name = 'prev_message';  // Ключ для POST-запроса
    input.value = action;
    document.getElementById('modal').appendChild(input);

    // Отправляем форму
    // document.getElementById('hiden_form').submit();
  });
});