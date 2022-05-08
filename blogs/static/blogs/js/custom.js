let images = document.querySelectorAll('.card-img-top')
for(let img of images) {
    img.addEventListener('click', () => 
        document.getElementById('exampleModal').querySelector('img').src = img.src)
}