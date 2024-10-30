document.addEventListener('DOMContentLoaded', (event) => {
    const video = document.getElementById('video');
    const startButton = document.getElementById('startBtnRegister');
    const stopButton = document.getElementById('stopBtnRegister');
    const registerButton = document.getElementById('registerButton');
    const nameInput = document.getElementById('name');
    const canvas_video = document.createElement('canvas');
    const captureButton = document.getElementById('captureButton');
    const capturedImage = document.getElementById('capturedImage');

    canvas_video.style.maxWidth = "100%";
    canvas_video.style.maxHeight = "100%";
    canvas_video.style.display = "none";

    // 启动摄像头的函数
    const startCamera = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
        } catch (error) {
            console.error('Error accessing camera:', error);
        }
    };

    // 停止摄像头的函数
    const stopCamera = () => {
        const stream = video.srcObject;
        const tracks = stream.getTracks();

        tracks.forEach(track => track.stop());
        video.srcObject = null;
    };

    // 拍照函数
    const capturePhoto = () => {
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        return canvas.toDataURL('image/jpeg');
    };

    // 点击“Start Camera”按钮启动摄像头
    startButton.addEventListener('click', startCamera);

    // 点击“Stop Camera”按钮停止摄像头
    stopButton.addEventListener('click', stopCamera);

    // 点击“拍照”按钮
    captureButton.addEventListener('click', () => {
        const photoDataUrl = capturePhoto();
        capturedImage.src = photoDataUrl;
        capturedImage.style.display = 'block';
    });

    // 点击“Register”按钮
    registerButton.addEventListener('click', () => {
        const name = nameInput.value;
        const photoDataUrl = capturedImage.src;
        sendRegistrationData(name, photoDataUrl);
    });

    // 发送数据到后端
    const sendRegistrationData = (name, photoDataUrl) => {
        const requestData = {
            "name": name,
            "frame": photoDataUrl,
        };

        $.ajax({
            type: 'POST',
            url: '/fvdb/register',
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify(requestData),
            success: function (data) {
                alert(data.message);
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    };
});
