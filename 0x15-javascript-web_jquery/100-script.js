// Select the <header> element
// Update the text color to red

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Header Color</title>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const header = document.querySelector('header');
            
            header.style.color = '#FF0000';
        });
    </script>
</head>
<body>
    <header>This is the header</header>
</body>
</html>
