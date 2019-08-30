$(document).ready(function(){
    document.getElementById('edit').addEventListener('click', function(){
        document.querySelector('.bg-modal').style.display = 'flex';
    });

    document.querySelector('.close').addEventListener('click', function(){
        document.querySelector('.bg-modal').style.display = 'none';
    });
});