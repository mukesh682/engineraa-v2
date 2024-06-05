document.getElementById('assessment-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const study_hours = document.getElementById('study_hours').value;
    const attendance = document.getElementById('attendance').value;
    const assignments_completed = document.getElementById('assignments_completed').value;
    const previous_grades = document.getElementById('previous_grades').value;
    const extracurricular = document.getElementById('extracurricular').value;
    
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            study_hours: study_hours,
            attendance: attendance,
            assignments_completed: assignments_completed,
            previous_grades: previous_grades,
            extracurricular: extracurricular
        }),
    })
    .then(response => response.json())
    .then(data => {
        window.location.href = '/learning-path';
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
