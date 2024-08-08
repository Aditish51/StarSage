document.addEventListener('DOMContentLoaded', function() {
    let a1f = document.querySelectorAll('.a1f');
    const answer = document.getElementById('ans');
    const next = document.getElementById('next');
    a1f.forEach(button => {
        button.addEventListener('click', function() {
            // Compare innerHTML values after trimming whitespace
            if (button.innerHTML.trim() === answer.innerHTML.trim()) {
                button.classList.add('matched');
                button.classList.remove('not-matched');
                next.style.display= 'block';

            } else {
                button.classList.add('not-matched');
                button.classList.remove('matched');
            }
        });
    });
});