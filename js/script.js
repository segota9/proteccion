

const toBase64 = file => new Promise(((resolve, reject) => {
    // Convert image to base 64
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = error => reject(error);
}));

function createImage(base64) {
   // Publish the images received.
    image = createImageDom(base64["image"])
    var maindiv2 = document.getElementById("mainDiv2");
    maindiv2.appendChild(image);
}

function createImageDom(base64) {
    var image = new Image();

    image.setAttribute("src" , base64);
    image.setAttribute("class" , "img-thumbnail");
    image.setAttribute("alt" , "Responsive image");
    image.setAttribute("style" , "height: 150px; " +
        "width: 100px; ");

    return image;
}

var ImagesArray = [];
    
function loadfile(event) {
    // Load images.
    for (let idx in event.target.files) {
        var file_ = event.target.files[idx];

        if (file_ !== undefined){
            ImagesArray.push(file_);
            console.log(ImagesArray);
            addImageDom(file_);
        }
    }
}

function addImageDom(file) {
     // Publish uploaded images
    var tagImage = document.createElement("img");
    tagImage.src = URL.createObjectURL(file);
    tagImage.setAttribute("style", "height: 150; width: 100px;");
    tagImage.setAttribute("class", "img-thumbnail");
    tagImage.style.height = "150px";
    tagImage.style.width  = "100px";

    var maindiv = document.getElementById("mainDiv");
    maindiv.appendChild(tagImage);
}

function sendImages() {
    // Send uploaded images to the server.
    for (let idx in ImagesArray){
        file = ImagesArray[idx];
        uploadImage(file);
    }
}

function postRequest(imageBase64) {
    // Post method used for communication with the server.
    var req = new XMLHttpRequest();
    var data = JSON.stringify({image: imageBase64});

    req.open("POST", "http://54.165.29.213/9999", true);

    req.onreadystatechange = function (aEvt) {
        if (req.status == 200 && req.readyState == 4){
            console.log(req.readyState);
            console.log("wiiiiiiiiii");
            console.log(req.response);
            createImage(JSON.parse(req.response));
        }else{
            console.log("Error loading page\n");
        };
    };

    req.send(data);
}

var convertToBase64 = function(file, callback){
    toBase64(file).then(res => {
        callback(res);
    }).catch(err => {
        console.log(err);
    });
};

var uploadImage = function(file){
    convertToBase64(file, function(imageBase64){
        postRequest(imageBase64);
    });
};



function sendEmail() {
  Email.send({
    Host: "smtp.gmail.com",
    Username: "enviarproteccion2@gmail.com",
    Password: "Proteccion123*",
    To: 'enviarproteccion2@gmail.com',
    From: "sender@email_address.com",
    Subject: "contact me",
    Body: "Well that was easy!!",
  })
    .then(function (message) {
      alert("mail sent successfully")
    });
}
