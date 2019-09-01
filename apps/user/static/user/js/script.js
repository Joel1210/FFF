$(document).ready(function () {

    //For the modal changing Display Name
    document.getElementById('changeDN').addEventListener('click', function () {
        document.querySelector('.bg-modal-DN').style.display = 'flex';
    });

    document.querySelector('.close-DN').addEventListener('click', function () {
        document.querySelector('.bg-modal-DN').style.display = 'none';
        console.log("hitting X")
    });

            //To have modal show up right away if there was a validation error
    var elementExistsDN = document.getElementById("showDN");


    if (elementExistsDN != null) {
        document.querySelector('.bg-modal-DN').style.display = 'flex';
        console.log('element exists DN?' + elementExistsDN)

    }
    if(elementExistsDN){
        document.querySelector('.bg-modal-DN').style.display = 'flex';
        console.log('element exists DN?' + elementExistsDN)
    }



    //For the modal changing Password
    document.getElementById('changePW').addEventListener('click', function () {
        document.querySelector('.bg-modal-PW').style.display = 'flex';
    });

    document.querySelector('.close-PW').addEventListener('click', function () {
        document.querySelector('.bg-modal-PW').style.display = 'none';
        console.log("hitting X")
    });
            //To have modal show up right away if there was a validation error
    var elementExistsPW = document.getElementById("showPW");

    if (elementExistsPW != null) {
        document.querySelector('.bg-modal-PW').style.display = 'flex';
        console.log('element exists PW?' + elementExistsPW)

    }
    if(elementExistsPW){
        document.querySelector('.bg-modal-PW').style.display = 'flex';
        console.log('element exists PW?' + elementExistsPW)
    }

    //For the modal changing Email
    document.getElementById('changeEmail').addEventListener('click', function () {
        document.querySelector('.bg-modal-Email').style.display = 'flex';
    });

    document.querySelector('.close-Email').addEventListener('click', function () {
        document.querySelector('.bg-modal-Email').style.display = 'none';
        console.log("hitting X")
    });
            //To have modal show up right away if there was a validation error
    var elementExistsEmail = document.getElementById("showEmail");

    if (elementExistsEmail != null) {
        document.querySelector('.bg-modal-Email').style.display = 'flex';
        console.log('element exists EMAIL?' + elementExistsEmail)

    }
    if(elementExistsEmail){
        document.querySelector('.bg-modal-Email').style.display = 'flex';
        console.log('element exists EMAIL?' + elementExistsEmail)
    }

    //For the modal changing Last Name
    document.getElementById('changeLastName').addEventListener('click', function () {
        document.querySelector('.bg-modal-LastName').style.display = 'flex';
    });

    document.querySelector('.close-LastName').addEventListener('click', function () {
        document.querySelector('.bg-modal-LastName').style.display = 'none';
        console.log("hitting X")
    });
            //To have modal show up right away if there was a validation error
    var elementExistsLastName = document.getElementById("showLastName");

    if (elementExistsLastName != null) {
        document.querySelector('.bg-modal-LastName').style.display = 'flex';
        console.log('element exists LAST NAME?' + elementExistsLastName)

    }
    if(elementExistsLastName){
        document.querySelector('.bg-modal-LastName').style.display = 'flex';
        console.log('element exists LAST NAME?' + elementExistsLastName)
    }
    //For the modal changing First Name
    document.getElementById('changeFirstName').addEventListener('click', function () {
        document.querySelector('.bg-modal-FirstName').style.display = 'flex';
    });

    document.querySelector('.close-FirstName').addEventListener('click', function () {
        document.querySelector('.bg-modal-FirstName').style.display = 'none';
        console.log("hitting X")
    });
            //To have modal show up right away if there was a validation error
    var elementExistsFirstName = document.getElementById("showFirstName");

    if (elementExistsFirstName != null) {
        document.querySelector('.bg-modal-FirstName').style.display = 'flex';
        console.log('element exists FIRST NAME?' + elementExistsFirstName)

    }
    if(elementExistsLastName){
        document.querySelector('.bg-modal-FirstName').style.display = 'flex';
        console.log('element exists FIRST NAME?' + elementExistsFirstName)
    }

});