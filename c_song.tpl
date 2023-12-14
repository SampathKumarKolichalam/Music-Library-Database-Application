<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insert Song</title>
</head>
<body>
    <h1>Create Song</h1>
    <form action="/create/song" method="post">
    <label for="album_id">ALBUM ID:</label>
        <label for="title">Song Title:</label>
        <input type="text" id="title" name="title" required>
        <button type="Submit">Create</button>
    </form>
    <a href="/song">Back</a>
</body>
</html>
